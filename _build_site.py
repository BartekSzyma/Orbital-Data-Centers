# -*- coding: utf-8 -*-
"""Generator statycznej strony HTML z vaultu Obsidian (Orbital Data Centers).
Obsluguje: [[wikilinki]] (#sekcje, |aliasy), ![[embed]] obrazow, Mermaid,
tabele GFM, <abbr>, tagi #, backlinki, interaktywny graf sieci, wyszukiwarke.
Wyjscie: katalog SITE (repo pod GitHub Pages).
"""
import re, os, glob, json, shutil, html
import markdown
import yaml

VAULT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(VAULT, "..", "Orbital-Data-Centers"))

SKIP_FILES = {"_build_network.py", "_build_site.py"}

# -------------------- pomocnicze --------------------
def slugify(s):
    s = s.strip().lower()
    s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE)
    return s.strip("-")

def anchor_slug(s):
    # slug naglowka/sekcji - spojny po obu stronach linku
    s = s.strip().lower()
    s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE)
    return s.strip("-")

def read(path):
    return open(path, encoding="utf-8").read()

def split_front(txt):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:
            fm = {}
        return fm, m.group(2)
    return {}, txt

# -------------------- zbierz strony --------------------
# page key = basename bez .md ; rekord: dict
pages = {}          # key -> record
basename_to_key = {}  # do rozwiazywania linkow

def reg_page(path, group):
    base = os.path.splitext(os.path.basename(path))[0]
    txt = read(path)
    fm, body = split_front(txt)
    # tytul
    if fm.get("tytul"):
        title = str(fm["tytul"]).strip().strip('"')
    else:
        h1 = re.search(r"^#\s+(.+)$", body, re.M)
        title = h1.group(1).strip() if h1 else base
    # outpath
    if base == "00 - MOC":
        out = "index.html"
    elif group == "temat":
        out = slugify(base) + ".html"
    else:  # spolka / indeks (w folderze spolki)
        out = "spolki/" + base + ".html"
    rec = dict(key=base, path=path, group=group, title=title, body=body,
               fm=fm, out=out)
    pages[base] = rec
    basename_to_key[base] = base
    return rec

for f in sorted(glob.glob(os.path.join(VAULT, "[0-9]*.md"))):
    base = os.path.splitext(os.path.basename(f))[0]
    reg_page(f, "moc" if base == "00 - MOC" else "temat")

for f in sorted(glob.glob(os.path.join(VAULT, "Spolki", "*.md"))):
    base = os.path.splitext(os.path.basename(f))[0]
    group = "indeks" if base.startswith("_") else "spolka"
    reg_page(f, group)

# -------------------- rozwiazywanie linkow --------------------
def resolve_target(target):
    """[[Spolki/rocket-lab]] / [[03 - fizyka...]] / [[_slownik]] -> page key lub None"""
    t = target.strip()
    t = t.split("/")[-1]  # odetnij prefiks folderu
    if t in pages:
        return t
    # czasem alias z .md
    if t.endswith(".md") and t[:-3] in pages:
        return t[:-3]
    return None

def relhref(from_out, to_out):
    d = os.path.dirname(from_out)
    rel = os.path.relpath(to_out, d if d else ".")
    return rel.replace("\\", "/")

# zbieramy krawedzie podczas renderu
edges = set()   # (src_key, dst_key)

def render_wikilinks(body, rec):
    out_links = []
    def repl(m):
        inner = m.group(1)
        # embed obrazu obsluzony osobno; tu zwykle linki
        if "|" in inner:
            target, alias = inner.split("|", 1)
        else:
            target, alias = inner, None
        section = None
        if "#" in target:
            target, section = target.split("#", 1)
        target = target.strip()
        key = resolve_target(target) if target else rec["key"]
        # link wewnatrz tej samej strony: [[#sekcja]]
        if target == "" and section:
            key = rec["key"]
        if key is None:
            # nierozwiazany - pokaz jako tekst
            label = alias if alias else (target + ("#" + section if section else ""))
            return f'<span class="broken-link" title="nierozwiazany link">{html.escape(label)}</span>'
        dst = pages[key]
        href = relhref(rec["out"], dst["out"])
        if section:
            href += "#" + anchor_slug(section)
        if alias:
            label = alias
        elif section:
            label = section
        else:
            label = dst["title"]
        out_links.append(key)
        return f'<a href="{href}" class="wikilink">{html.escape(label)}</a>'
    body = re.sub(r"\[\[([^\]]+)\]\]", repl, body)
    for k in out_links:
        if k != rec["key"]:
            edges.add((rec["key"], k))
    return body

def render_embeds(body, rec):
    # ![[assets/...]]  -> <img>  (sciezka wzgledem folderu noty)
    def repl(m):
        inner = m.group(1)
        if "|" in inner:
            inner = inner.split("|", 1)[0]
        src = inner.strip()
        # noty tematyczne: assets/..  (kopiowane do SITE/assets) -> wzgledem strony root
        href = relhref(rec["out"], src)  # rec.out root -> "assets/.."
        return f'<figure class="embed"><img loading="lazy" src="{href}" alt=""></figure>'
    return re.sub(r"!\[\[([^\]]+)\]\]", repl, body)

# tagi typu "#grafika #architektura"
TAG_LINE = re.compile(r"^(#[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ/-]+(?:\s+#[\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ/-]+)*)\s*$", re.M)
def render_tag_lines(body):
    def repl(m):
        tags = m.group(1).split()
        chips = " ".join(f'<span class="tag">{html.escape(t)}</span>' for t in tags)
        return f'\n<p class="tagline">{chips}</p>\n'
    return TAG_LINE.sub(repl, body)

MERMAID_RE = re.compile(r"```mermaid\s*\n(.*?)\n```", re.S)
def extract_mermaid(body):
    blocks = []
    def repl(m):
        blocks.append(m.group(1))
        return f"\n\x00MERM{len(blocks)-1}\x00\n"
    return MERMAID_RE.sub(repl, body), blocks

def add_heading_ids(htmltext):
    def repl(m):
        level, attrs, inner = m.group(1), m.group(2), m.group(3)
        # tekst bez tagow do slugu
        text = re.sub(r"<[^>]+>", "", inner)
        text = html.unescape(text)
        hid = anchor_slug(text)
        if "id=" in attrs:
            return m.group(0)
        return f'<h{level}{attrs} id="{hid}">{inner}</h{level}>'
    return re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", repl, htmltext, flags=re.S)

MD_EXT = ["extra", "sane_lists", "nl2br"]

def render_body(rec):
    body = rec["body"]
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)   # usun markery
    body, merm = extract_mermaid(body)
    body = render_embeds(body, rec)
    body = render_wikilinks(body, rec)
    body = render_tag_lines(body)
    htmltext = markdown.markdown(body, extensions=MD_EXT, output_format="html5")
    # przywroc mermaid
    def merm_repl(m):
        idx = int(m.group(1))
        return f'<pre class="mermaid">{html.escape(merm[idx])}</pre>'
    htmltext = re.sub(r"<p>\x00MERM(\d+)\x00</p>", merm_repl, htmltext)
    htmltext = re.sub(r"\x00MERM(\d+)\x00", merm_repl, htmltext)
    htmltext = add_heading_ids(htmltext)
    return htmltext

# render wszystkich (zbiera edges)
for rec in pages.values():
    rec["html"] = render_body(rec)

# -------------------- backlinki --------------------
backlinks = {k: [] for k in pages}
for (src, dst) in edges:
    if dst in pages and src in pages:
        backlinks[dst].append(src)

# -------------------- nawigacja --------------------
themes = [p for p in pages.values() if p["group"] == "temat"]
themes.sort(key=lambda p: p["key"])
spolki = [p for p in pages.values() if p["group"] == "spolka"]
def co_tryb(p):
    return p["fm"].get("tryb", "")
deep = sorted([p for p in spolki if co_tryb(p) == "deep"], key=lambda p: p["title"])
lite = sorted([p for p in spolki if co_tryb(p) == "lite"], key=lambda p: p["title"])
indeksy = sorted([p for p in pages.values() if p["group"] == "indeks"], key=lambda p: p["key"])
moc = pages["00 - MOC"]

def nav_html(cur_out):
    def li(p):
        href = relhref(cur_out, p["out"])
        active = ' class="active"' if p["out"] == cur_out else ""
        return f'<li><a{active} href="{href}">{html.escape(p["title"])}</a></li>'
    home = relhref(cur_out, "index.html")
    graf = relhref(cur_out, "graf.html")
    parts = [f'<a class="nav-home" href="{home}">Orbital Data Centers</a>']
    parts.append('<div class="nav-search"><input id="searchbox" type="search" placeholder="Szukaj... (/)" autocomplete="off"><div id="search-results"></div></div>')
    parts.append(f'<a class="nav-graf" href="{graf}">Graf sieci powiązań</a>')
    parts.append('<div class="nav-sec"><span class="nav-h">Sekcje</span><ol>' + "".join(li(p) for p in themes) + "</ol></div>")
    parts.append('<div class="nav-sec"><span class="nav-h">Spółki - omówienie pełne</span><ul>' + "".join(li(p) for p in deep) + "</ul></div>")
    parts.append('<div class="nav-sec"><span class="nav-h">Spółki - omówienie skrótowe</span><ul>' + "".join(li(p) for p in lite) + "</ul></div>")
    parts.append('<div class="nav-sec"><span class="nav-h">Indeksy</span><ul>' + "".join(li(p) for p in indeksy) + "</ul></div>")
    return "\n".join(parts)

GROUP_LABEL = {"moc": "Mapa raportu", "temat": "Sekcja", "spolka": "Spółka",
               "indeks": "Indeks"}

PAGE_TMPL = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - Orbital Data Centers</title>
<link rel="stylesheet" href="{css}">
<script>window.SITE_ROOT="{root}";</script>
</head>
<body>
<button id="menu-toggle" aria-label="Menu">&#9776;</button>
<nav id="sidebar">{nav}</nav>
<main>
<article class="page" data-group="{group}">
<div class="crumbs"><span class="badge badge-{group}">{glabel}</span></div>
<div class="content">{content}</div>
{backlinks}
</article>
<footer>Wygenerowano z vaultu Obsidian - raport tematyczny. Wykresy: Mermaid. Dane i źródła w treści notatek.</footer>
</main>
<script src="{search_idx}"></script>
<script src="{app}"></script>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
mermaid.initialize({{startOnLoad:true, theme:"neutral", securityLevel:"loose"}});
</script>
</body>
</html>
"""

def backlinks_html(rec):
    bl = sorted(set(backlinks[rec["key"]]))
    if not bl:
        return ""
    items = []
    for k in bl:
        p = pages[k]
        href = relhref(rec["out"], p["out"])
        items.append(f'<li><span class="badge badge-{p["group"]} mini">{GROUP_LABEL[p["group"]]}</span> <a href="{href}">{html.escape(p["title"])}</a></li>')
    return ('<section class="backlinks"><h2>Linkują tutaj</h2>'
            f'<p class="bl-count">{len(bl)} powiązanych notatek</p><ul>' + "".join(items) + "</ul></section>")

# -------------------- zapis stron --------------------
if os.path.isdir(SITE):
    # nie kasujemy .git
    for entry in os.listdir(SITE):
        if entry == ".git":
            continue
        p = os.path.join(SITE, entry)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
os.makedirs(os.path.join(SITE, "spolki"), exist_ok=True)
os.makedirs(os.path.join(SITE, "static"), exist_ok=True)

for rec in pages.values():
    css = relhref(rec["out"], "static/style.css")
    appjs = relhref(rec["out"], "static/app.js")
    sidx = relhref(rec["out"], "static/search-index.js")
    depth = rec["out"].count("/")
    root = "../" * depth
    page = PAGE_TMPL.format(
        title=html.escape(rec["title"]), css=css, nav=nav_html(rec["out"]),
        group=rec["group"], glabel=GROUP_LABEL[rec["group"]],
        content=rec["html"], backlinks=backlinks_html(rec),
        search_idx=sidx, app=appjs, root=root)
    dst = os.path.join(SITE, rec["out"])
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(page)

# -------------------- assets --------------------
def copytree(src, dst):
    if os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
copytree(os.path.join(VAULT, "assets"), os.path.join(SITE, "assets"))
copytree(os.path.join(VAULT, "Spolki", "assets"), os.path.join(SITE, "spolki", "assets"))
# statyczne zrodla (css/js)
for f in glob.glob(os.path.join(VAULT, "_static_src", "*")):
    bn = os.path.basename(f)
    if bn == "README_REPO.md":
        shutil.copy(f, os.path.join(SITE, "README.md"))
        continue
    shutil.copy(f, os.path.join(SITE, "static", bn))
# .nojekyll - by GitHub Pages serwowal pliki z _ i nie odpalal Jekylla
open(os.path.join(SITE, ".nojekyll"), "w").close()

# --- provenance: kopia zrodel vaultu + skryptow buildu (reprodukowalnosc) ---
vsrc = os.path.join(SITE, "vault")
os.makedirs(os.path.join(vsrc, "Spolki"), exist_ok=True)
for f in glob.glob(os.path.join(VAULT, "*.md")):
    shutil.copy(f, vsrc)
for f in glob.glob(os.path.join(VAULT, "Spolki", "*")):
    if os.path.isfile(f):
        shutil.copy(f, os.path.join(vsrc, "Spolki"))
# uwaga: assety NIE sa kopiowane do vault/ (sa juz w /assets i /spolki/assets) - oszczednosc miejsca
for f in ("_build_network.py", "_build_site.py"):
    shutil.copy(os.path.join(VAULT, f), SITE)
copytree(os.path.join(VAULT, "_static_src"), os.path.join(SITE, "_static_src"))

# -------------------- graf --------------------
GROUP_COLOR = {"moc": "#e6447a", "temat": "#2f81f7", "spolka": "#3fb950", "indeks": "#a371f7"}
# graf jest nieskierowany (bez strzalek) - scal wzajemne linki A->B i B->A w jedna krawedz,
# by nie rysowac podwojnych linii miedzy tymi samymi notatkami (backlinki zostaja kierunkowe)
uedges = {tuple(sorted((s, d))) for (s, d) in edges}
nodes = []
for k, p in pages.items():
    deg = len([1 for (s, d) in uedges if s == k or d == k])
    nodes.append({"id": k, "label": p["title"], "group": p["group"],
                  "url": p["out"], "val": deg})
edges_j = [{"from": s, "to": d} for (s, d) in sorted(uedges)]
graph_js = "window.GRAPH=" + json.dumps({"nodes": nodes, "edges": edges_j}, ensure_ascii=False) + ";"
open(os.path.join(SITE, "static", "graph-data.js"), "w", encoding="utf-8").write(graph_js)

# -------------------- search index --------------------
sidx = []
for k, p in pages.items():
    text = re.sub(r"<!--.*?-->", "", p["body"], flags=re.S)
    text = re.sub(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), text)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[#*>`!\[\]()]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()[:6000]
    sidx.append({"t": p["title"], "u": p["out"], "g": p["group"], "s": text})
open(os.path.join(SITE, "static", "search-index.js"), "w", encoding="utf-8").write(
    "window.SEARCH=" + json.dumps(sidx, ensure_ascii=False) + ";")

# -------------------- graf.html --------------------
graf_page = """<!DOCTYPE html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Graf sieci powiązań - Orbital Data Centers</title>
<link rel="stylesheet" href="static/style.css">
<script src="https://cdn.jsdelivr.net/npm/vis-network@9.1.9/standalone/umd/vis-network.min.js"></script>
</head><body>
<button id="menu-toggle" aria-label="Menu">&#9776;</button>
<nav id="sidebar">{nav}</nav>
<main>
<article class="page" data-group="graf">
<div class="crumbs"><span class="badge badge-moc">Graf</span></div>
<div class="content">
<h1>Graf sieci powiązań</h1>
<p>Interaktywna mapa wszystkich notatek i powiązań między nimi. Kolor węzła oznacza typ
(<span class="g-moc">mapa</span>, <span class="g-temat">sekcja</span>,
<span class="g-spolka">spółka</span>, <span class="g-indeks">indeks</span>); rozmiar - liczbę powiązań.
Kliknij węzeł, aby otworzyć notatkę. Przeciągaj, przewijaj, aby przybliżyć.</p>
<div class="graf-legend">
<span class="badge badge-moc">Mapa raportu</span>
<span class="badge badge-temat">Sekcje (15)</span>
<span class="badge badge-spolka">Spółki (26)</span>
<span class="badge badge-indeks">Indeksy</span>
</div>
<div id="net"></div>
</div>
</article>
</main>
<script src="static/graph-data.js"></script>
<script src="static/app.js"></script>
<script src="static/graf.js"></script>
</body></html>
"""
open(os.path.join(SITE, "graf.html"), "w", encoding="utf-8").write(
    graf_page.format(nav=nav_html("graf.html")))

print("Strony:", len(pages), "| krawedzie:", len(edges), "| SITE:", SITE)

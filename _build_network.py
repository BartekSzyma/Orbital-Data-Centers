# -*- coding: utf-8 -*-
"""Wstrzykuje dwie brakujace warstwy sieci powiazan do vaultu:
   1. temat -> temat  (## Powiazane watki)  -- kuratorowane krawedzie
   2. spolka -> spolka (## Powiazane spolki) -- peers wspoldzielacy temat
Idempotentny: pracuje miedzy markerami <!-- network:* -->.
"""
import re, glob, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

# --- mapy tematow ---
THEME_FILE = {
    "wprowadzenie-definicje-i-architektury": "01 - wprowadzenie-definicje-i-architektury",
    "weryfikacja-tez-sceptycznego-artykulu": "02 - weryfikacja-tez-sceptycznego-artykulu",
    "fizyka-orbitalna-orbity-i-operacje": "03 - fizyka-orbitalna-orbity-i-operacje",
    "energetyka-kosmiczna-i-fotowoltaika-orbitalna": "04 - energetyka-kosmiczna-i-fotowoltaika-orbitalna",
    "chlodzenie-i-radiacyjne-odprowadzanie-ciepla": "05 - chlodzenie-i-radiacyjne-odprowadzanie-ciepla",
    "promieniowanie-i-elektronika-rad-hard-vs-cots": "06 - promieniowanie-i-elektronika-rad-hard-vs-cots",
    "lacznosc-optyczne-isl-downlink-i-latencja": "07 - lacznosc-optyczne-isl-downlink-i-latencja",
    "niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu": "08 - niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu",
    "ekonomika-i-koszty-calkowite-tco": "09 - ekonomika-i-koszty-calkowite-tco",
    "gracze-i-projekty": "10 - gracze-i-projekty",
    "regulacje-prawo-kosmiczne-debris-i-itu": "11 - regulacje-prawo-kosmiczne-debris-i-itu",
    "naziemny-bottleneck-energetyczny-i-sieciowy": "12 - naziemny-bottleneck-energetyczny-i-sieciowy",
    "sentyment-spoleczny-i-moratoria-na-centra-danych": "13 - sentyment-spoleczny-i-moratoria-na-centra-danych",
    "zrownowazony-rozwoj-i-srodowisko": "14 - zrownowazony-rozwoj-i-srodowisko",
    "bezpieczenstwo-geopolityka-i-realizm-10-letni": "15 - bezpieczenstwo-geopolityka-i-realizm-10-letni",
}
THEME_SHORT = {
    "wprowadzenie-definicje-i-architektury": "Wprowadzenie i architektury",
    "weryfikacja-tez-sceptycznego-artykulu": "Weryfikacja tez sceptyka",
    "fizyka-orbitalna-orbity-i-operacje": "Fizyka orbitalna",
    "energetyka-kosmiczna-i-fotowoltaika-orbitalna": "Energetyka kosmiczna",
    "chlodzenie-i-radiacyjne-odprowadzanie-ciepla": "Chłodzenie",
    "promieniowanie-i-elektronika-rad-hard-vs-cots": "Promieniowanie i elektronika",
    "lacznosc-optyczne-isl-downlink-i-latencja": "Łączność optyczna",
    "niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu": "Niezawodność i serwisowanie",
    "ekonomika-i-koszty-calkowite-tco": "Ekonomika i TCO",
    "gracze-i-projekty": "Gracze i projekty",
    "regulacje-prawo-kosmiczne-debris-i-itu": "Regulacje i debris",
    "naziemny-bottleneck-energetyczny-i-sieciowy": "Naziemny bottleneck",
    "sentyment-spoleczny-i-moratoria-na-centra-danych": "Sentyment i moratoria",
    "zrownowazony-rozwoj-i-srodowisko": "Środowisko",
    "bezpieczenstwo-geopolityka-i-realizm-10-letni": "Bezpieczeństwo i geopolityka",
}

# --- kuratorowana siec temat -> temat: (cel, uzasadnienie krawedzi) ---
THEME_EDGES = {
"wprowadzenie-definicje-i-architektury": [
    ("fizyka-orbitalna-orbity-i-operacje", "architektury free-flyer i konstelacji wynikają z wyboru orbity i operacji"),
    ("energetyka-kosmiczna-i-fotowoltaika-orbitalna", "głównym motorem napędowym jest tania, ciągła energia słoneczna"),
    ("ekonomika-i-koszty-calkowite-tco", "czy wizja gigawatowych chmur jest opłacalna rozstrzyga rachunek TCO"),
    ("gracze-i-projekty", "kto realnie buduje opisane tu architektury (SpaceX, Google, Starcloud)"),
    ("naziemny-bottleneck-energetyczny-i-sieciowy", "motywacja popytowa: niedobór mocy i kolejki przyłączeniowe na Ziemi"),
],
"weryfikacja-tez-sceptycznego-artykulu": [
    ("ekonomika-i-koszty-calkowite-tco", "tezy o koszcie wyniesienia i \"2x drożej\" rozwija analiza TCO"),
    ("energetyka-kosmiczna-i-fotowoltaika-orbitalna", "teza o panelach 200 MW = masa/powierzchnia paneli to fizyka PV"),
    ("chlodzenie-i-radiacyjne-odprowadzanie-ciepla", "teza o chłodzeniu w próżni to mechanizm radiacyjnego oddawania ciepła"),
    ("promieniowanie-i-elektronika-rad-hard-vs-cots", "teza o drogiej elektronice rad-hard to koszt vs COTS"),
    ("lacznosc-optyczne-isl-downlink-i-latencja", "tezy o Starlink i latencji to warstwa łączności ISL/downlink"),
    ("fizyka-orbitalna-orbity-i-operacje", "teza o widoczności 5 minut to geometria przelotu SSO"),
],
"fizyka-orbitalna-orbity-i-operacje": [
    ("energetyka-kosmiczna-i-fotowoltaika-orbitalna", "wybór orbity (dawn-dusk vs LEO) decyduje o nasłonecznieniu 24/7"),
    ("chlodzenie-i-radiacyjne-odprowadzanie-ciepla", "orientacja platformy steruje celowaniem radiatorów w zimną przestrzeń"),
    ("promieniowanie-i-elektronika-rad-hard-vs-cots", "wysokość orbity wprost wyznacza roczną dawkę promieniowania"),
    ("niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu", "deorbitacja, EOL i serwis to operacje cyklu życia platformy"),
    ("regulacje-prawo-kosmiczne-debris-i-itu", "zasada 5 lat na deorbit i ryzyko debris to ramy regulacyjne operacji"),
],
"energetyka-kosmiczna-i-fotowoltaika-orbitalna": [
    ("fizyka-orbitalna-orbity-i-operacje", "insolacja i cykle eklips zależą od geometrii orbity"),
    ("chlodzenie-i-radiacyjne-odprowadzanie-ciepla", "bilans mocy zamyka się dopiero z bilansem cieplnym (radiatory)"),
    ("ekonomika-i-koszty-calkowite-tco", "koszt i masa systemu energetycznego wchodzą wprost do TCO"),
    ("naziemny-bottleneck-energetyczny-i-sieciowy", "przewaga energetyczna orbity ma sens wobec niedoboru mocy na Ziemi"),
    ("zrownowazony-rozwoj-i-srodowisko", "carbon intensity solar orbital vs naziemny miks energetyczny"),
],
"chlodzenie-i-radiacyjne-odprowadzanie-ciepla": [
    ("energetyka-kosmiczna-i-fotowoltaika-orbitalna", "każdy wat mocy obliczeniowej trzeba odprowadzić jako ciepło"),
    ("fizyka-orbitalna-orbity-i-operacje", "orientacja radiatorów edge-on do Słońca to zagadnienie operacji"),
    ("promieniowanie-i-elektronika-rad-hard-vs-cots", "rosnące TDP akceleratorów AI napędza wymaganą powierzchnię radiatora"),
    ("niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu", "radiatory rozkładane to element niezawodności i serwisu"),
    ("ekonomika-i-koszty-calkowite-tco", "setki ton radiatora na MW to realny koszt w rachunku startowym"),
],
"promieniowanie-i-elektronika-rad-hard-vs-cots": [
    ("fizyka-orbitalna-orbity-i-operacje", "wybór orbity to wybór środowiska radiacyjnego (TID)"),
    ("niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu", "dawka skumulowana wyznacza żywotność i MTBF elektroniki"),
    ("ekonomika-i-koszty-calkowite-tco", "rad-hard vs COTS to kompromis koszt/wydajność wchodzący do TCO"),
    ("weryfikacja-tez-sceptycznego-artykulu", "weryfikuje tezę o elektronice rad-hard \"kilkaset razy droższej\""),
    ("bezpieczenstwo-geopolityka-i-realizm-10-letni", "dual-use i kontrola eksportu chipów rad-hard"),
],
"lacznosc-optyczne-isl-downlink-i-latencja": [
    ("wprowadzenie-definicje-i-architektury", "OISL spina satelity w \"jeden komputer\" - sedno architektury"),
    ("gracze-i-projekty", "petabitowa siatka laserowa Starlink jako backbone ODC SpaceX"),
    ("weryfikacja-tez-sceptycznego-artykulu", "obala tezy o Starlink i o downlink bottleneck (kompresja semantyczna)"),
    ("regulacje-prawo-kosmiczne-debris-i-itu", "pasma RF i koordynacja częstotliwości to domena ITU"),
    ("bezpieczenstwo-geopolityka-i-realizm-10-letni", "jamming, spoofing i cyber to ryzyka warstwy łączności"),
],
"niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu": [
    ("fizyka-orbitalna-orbity-i-operacje", "deorbitacja i wymiana modułów to operacje końca życia"),
    ("promieniowanie-i-elektronika-rad-hard-vs-cots", "żywotność sprzętu zależy od dawki promieniowania i MTBF"),
    ("ekonomika-i-koszty-calkowite-tco", "cykl odświeżania vs żywotność platformy decyduje o ekonomice"),
    ("regulacje-prawo-kosmiczne-debris-i-itu", "EOL i deorbit to wymogi anty-debris"),
    ("chlodzenie-i-radiacyjne-odprowadzanie-ciepla", "rozkładane radiatory i brak hot-swap to wyzwania niezawodności"),
],
"ekonomika-i-koszty-calkowite-tco": [
    ("weryfikacja-tez-sceptycznego-artykulu", "tu rozstrzygają się kosztowe tezy sceptycznego artykułu"),
    ("fizyka-orbitalna-orbity-i-operacje", "koszt wyniesienia masy na orbitę to punkt wyjścia rachunku"),
    ("energetyka-kosmiczna-i-fotowoltaika-orbitalna", "koszt i masa systemu energetycznego to duża część CAPEX"),
    ("niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu", "żywotność i cykl odświeżania sterują OPEX i amortyzacją"),
    ("gracze-i-projekty", "finansowanie i założenia break-even konkretnych graczy"),
    ("naziemny-bottleneck-energetyczny-i-sieciowy", "punktem odniesienia jest koszt naziemnego DC"),
],
"gracze-i-projekty": [
    ("wprowadzenie-definicje-i-architektury", "architektury, które realizują opisani gracze"),
    ("lacznosc-optyczne-isl-downlink-i-latencja", "SpaceX wykorzystuje istniejący backbone laserowy Starlink"),
    ("ekonomika-i-koszty-calkowite-tco", "finansowanie i progi opłacalności poszczególnych projektów"),
    ("regulacje-prawo-kosmiczne-debris-i-itu", "wnioski FCC i autoryzacje konstelacji"),
    ("bezpieczenstwo-geopolityka-i-realizm-10-letni", "wyścig USA-Chiny: prywatni gracze vs państwowe konstelacje"),
],
"regulacje-prawo-kosmiczne-debris-i-itu": [
    ("fizyka-orbitalna-orbity-i-operacje", "zasada 5 lat na deorbit kształtuje operacje na orbicie"),
    ("lacznosc-optyczne-isl-downlink-i-latencja", "filing i koordynacja pasm ITU dla łączności"),
    ("niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu", "EOL i deorbit jako wymóg ograniczania debris"),
    ("sentyment-spoleczny-i-moratoria-na-centra-danych", "light pollution i \"Not In My Sky\" astronomów"),
    ("zrownowazony-rozwoj-i-srodowisko", "debris jako koszt środowiskowy (Kessler)"),
    ("bezpieczenstwo-geopolityka-i-realizm-10-letni", "jurysdykcja danych i suwerenność na orbicie"),
],
"naziemny-bottleneck-energetyczny-i-sieciowy": [
    ("wprowadzenie-definicje-i-architektury", "to jest popytowa motywacja całej dziedziny ODC"),
    ("energetyka-kosmiczna-i-fotowoltaika-orbitalna", "orbita ma omijać niedobór mocy i kolejki przyłączeniowe"),
    ("ekonomika-i-koszty-calkowite-tco", "koszt naziemnego DC to benchmark dla wariantu orbitalnego"),
    ("sentyment-spoleczny-i-moratoria-na-centra-danych", "protesty i moratoria pogłębiają naziemne wąskie gardła"),
    ("zrownowazony-rozwoj-i-srodowisko", "woda chłodząca i grunt jako lokalne ograniczenia środowiskowe"),
],
"sentyment-spoleczny-i-moratoria-na-centra-danych": [
    ("naziemny-bottleneck-energetyczny-i-sieciowy", "moratoria i protesty to część naziemnego bottlenecku"),
    ("regulacje-prawo-kosmiczne-debris-i-itu", "light pollution łączy sentyment z regulacją astronomiczną"),
    ("zrownowazony-rozwoj-i-srodowisko", "presja ESG i argumenty środowiskowe napędzają sentyment"),
    ("gracze-i-projekty", "narracja \"data centers in space\" jako PR graczy"),
],
"zrownowazony-rozwoj-i-srodowisko": [
    ("naziemny-bottleneck-energetyczny-i-sieciowy", "woda, grunt i energia to wspólna oś środowiskowa"),
    ("regulacje-prawo-kosmiczne-debris-i-itu", "debris i Kessler jako środowiskowy koszt orbity"),
    ("sentyment-spoleczny-i-moratoria-na-centra-danych", "argument ESG spina środowisko z akceptacją społeczną"),
    ("energetyka-kosmiczna-i-fotowoltaika-orbitalna", "carbon intensity solar orbital vs naziemny miks"),
    ("fizyka-orbitalna-orbity-i-operacje", "reentry i burn-up przy deorbitacji modułów"),
],
"bezpieczenstwo-geopolityka-i-realizm-10-letni": [
    ("promieniowanie-i-elektronika-rad-hard-vs-cots", "dual-use elektroniki i kontrola eksportu chipów"),
    ("lacznosc-optyczne-isl-downlink-i-latencja", "jamming, spoofing i cyber w warstwie łączności"),
    ("niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu", "resilience orbity vs Ziemia to też niezawodność"),
    ("gracze-i-projekty", "wyścig USA-Chiny i timeline demonstratorów"),
    ("regulacje-prawo-kosmiczne-debris-i-itu", "data sovereignty i jurysdykcja danych"),
]
}

# --- parsuj deskryptory spolek z MOC ---
moc = open("00 - MOC.md", encoding="utf-8").read()
DESC = {}
for m in re.finditer(r'\[\[Spolki/([a-z0-9-]+)\|[^\]]+\]\]\s*-\s*(.+)', moc):
    DESC[m.group(1)] = m.group(2).strip()

# --- zbierz tematy spolek ---
companies = {}  # id -> dict(name,ticker,tryb,tematy)
theme_to_co = defaultdict(list)
for f in sorted(glob.glob("Spolki/*.md")):
    base = os.path.basename(f)
    if base.startswith("_"):
        continue
    txt = open(f, encoding="utf-8").read()
    fm = re.search(r'^---\n(.*?)\n---', txt, re.S).group(1)
    def g(k):
        mm = re.search(rf'^{k}:\s*(.*)$', fm, re.M)
        return mm.group(1).strip().strip('"') if mm else ""
    cid = g("company_id")
    tm = re.search(r'^tematy:\s*\[(.*?)\]', fm, re.M)
    tematy = [t.strip().strip('"') for t in tm.group(1).split(",")] if tm and tm.group(1).strip() else []
    companies[cid] = dict(name=g("nazwa_kanoniczna"), ticker=g("ticker"),
                          tryb=g("tryb"), tematy=tematy, file=f)
    for t in tematy:
        theme_to_co[t].append(cid)


def upsert(text, start, end, block):
    """Wstaw lub zamien blok miedzy markerami. Zwraca (text, found)."""
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if pat.search(text):
        return pat.sub(lambda m: block, text), True
    return text, False


def insert_after_intro(text, block):
    """Wstaw blok po sekcjach nawigacyjnych (W skrocie / Spolki powiazane)."""
    heads = list(re.finditer(r'^(##[^#].*)$', text, re.M))
    skip = ("## w skrócie", "## spółki powiązane")
    for h in heads:
        title = h.group(1).strip().lower()
        if not any(title.startswith(s) for s in skip):
            return text[:h.start()] + block + "\n" + text[h.start():]
    return text.rstrip() + "\n\n" + block + "\n"


# ============ 1. TEMAT -> TEMAT ============
for theme, edges in THEME_EDGES.items():
    fn = THEME_FILE[theme] + ".md"
    text = open(fn, encoding="utf-8").read()
    lines = ["<!-- network:watki:start -->", "## Powiązane wątki", "",
             "> Mapa powiązań tematycznych - jak ten wątek łączy się z resztą raportu.", ""]
    for tgt, why in edges:
        lines.append(f"- [[{THEME_FILE[tgt]}|{THEME_SHORT[tgt]}]] - {why}")
    lines.append("<!-- network:watki:end -->")
    block = "\n".join(lines)
    text, found = upsert(text, "<!-- network:watki:start -->", "<!-- network:watki:end -->", block)
    if not found:
        text = insert_after_intro(text, block)
    open(fn, "w", encoding="utf-8").write(text)
    print("watki:", fn, "(replaced)" if found else "(inserted)")

# ============ 2. SPOLKA -> SPOLKA ============
for cid, c in companies.items():
    peers = defaultdict(list)  # peer_id -> [shared themes]
    for t in c["tematy"]:
        for other in theme_to_co[t]:
            if other != cid:
                peers[other].append(t)
    if not peers:
        continue
    # sortuj wg liczby wspolnych watkow malejaco, potem alfabetycznie
    ordered = sorted(peers.items(), key=lambda kv: (-len(kv[1]), companies[kv[0]]["name"]))
    lines = ["<!-- network:peers:start -->", "## Powiązane spółki", "",
             "> Inne notowane spółki z raportu dzielące z tą firmą co najmniej jeden wątek tematyczny "
             "(wspólny rynek, technologia lub łańcuch wartości).", ""]
    for pid, shared in ordered:
        pc = companies[pid]
        label = f"{pc['name']} ({pc['ticker']})"
        shared_lbl = "; ".join(THEME_SHORT[t] for t in shared)
        desc = DESC.get(pid, "")
        desc_part = f" - {desc}" if desc else ""
        lines.append(f"- [[Spolki/{pid}|{label}]]{desc_part}  \n  *Wspólne wątki: {shared_lbl}.*")
    lines.append("<!-- network:peers:end -->")
    block = "\n".join(lines)
    text = open(c["file"], encoding="utf-8").read()
    text, found = upsert(text, "<!-- network:peers:start -->", "<!-- network:peers:end -->", block)
    if not found:
        # wstaw przed slowniczkiem spolki, inaczej przed zrodlami, inaczej dopisz
        anchor = re.search(r'<!-- spolki:slownik:start -->', text)
        if not anchor:
            anchor = re.search(r'<!-- spolki:zrodla:start -->', text)
        if anchor:
            text = text[:anchor.start()] + block + "\n\n" + text[anchor.start():]
        else:
            text = text.rstrip() + "\n\n" + block + "\n"
    open(c["file"], "w", encoding="utf-8").write(text)
    print("peers:", os.path.basename(c["file"]), len(ordered), "peers", "(replaced)" if found else "(inserted)")

print("\nDONE. Deskryptorow z MOC:", len(DESC))

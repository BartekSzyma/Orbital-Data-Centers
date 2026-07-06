# Orbitalne centra danych - raport tematyczny

Statyczna wersja HTML pogłębionego raportu o **orbitalnych (kosmicznych) centrach danych** (Orbital Data Centers, ODC), wygenerowana z vaultu Obsidian. Strona jest hostowana na GitHub Pages.

> Punktem wyjścia był polski artykuł sceptyczny "Centra przetwarzania danych na orbicie nie mają sensu", którego tezy raport krytycznie weryfikuje.

## Co tu jest

- **15 sekcji tematycznych** - od definicji i architektur, przez fizykę orbitalną, energetykę, chłodzenie, promieniowanie, łączność, niezawodność, ekonomikę (TCO), graczy i projekty, po regulacje, naziemny bottleneck, sentyment społeczny, środowisko i bezpieczeństwo.
- **26 notatek spółek giełdowych** produkujących podzespoły i technologie dla ODC oraz naziemnej infrastruktury DC (13 omówionych pełnie, 13 skrótowo).
- **Sieć powiązań** między notatkami w czterech warstwach: spółka → temat, temat → spółka, temat → temat oraz spółka → spółka. Każda strona ma na dole sekcję "Linkują tutaj" (backlinki).
- **Interaktywny graf sieci** (`graf.html`) wizualizujący wszystkie 44 węzły i powiązania.
- **Wyszukiwarka** po tytułach i treści (klawisz `/`).
- Wykresy **Mermaid** generowane z twardych liczb oraz figury z paperów i materiałów graczy (nota licencyjna w treści).

## Struktura repozytorium

```
index.html              - mapa raportu (MOC)
NN-*.html               - 15 sekcji tematycznych
spolki/*.html           - notatki spółek + indeksy (słownik, widok GPW/EU)
graf.html               - interaktywny graf sieci powiązań
assets/, spolki/assets/ - grafiki
static/                 - CSS, JS, dane grafu i indeks wyszukiwarki
vault/                  - źródła Markdown (Obsidian) dla reprodukowalności
_build_network.py       - skrypt budujący warstwy linków w vaultcie
_build_site.py          - generator statycznej strony HTML
```

## Reprodukcja

Strona jest generowana z vaultu Obsidian skryptem `_build_site.py` (Python 3, biblioteki `markdown`, `pyyaml`). Wykresy renderuje [Mermaid](https://mermaid.js.org/), graf - [vis-network](https://visjs.org/).

---

*Treść ma charakter informacyjny i edukacyjny; nie stanowi porady inwestycyjnej.*

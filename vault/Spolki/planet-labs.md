---
company_id: "planet-labs"
nazwa_kanoniczna: "Planet Labs PBC"
ticker: "PL"
glowny_listing: "XNYS"
isin: ""
status: "notowana"
tryb: "lite"
ekspozycja_gpw_eu: false
ekspozycja_gpw_eu_nota: ""
tematy: ["gracze-i-projekty"]
skala_zrodel_agregat: "pomaranczowa"
---

# Planet Labs (PL)

<!-- spolki:temat:gracze-i-projekty:start -->
## W kontekscie: Gracze i projekty

Planet Labs PBC (NYSE: PL) to amerykański operator największej komercyjnej konstelacji obserwacji Ziemi i dostawca danych geoprzestrzennych oraz analityki AI. Firma jest wymieniana jako partner Google w ramach [[10 - gracze-i-projekty#Google - Project Suncatcher (TPU na orbicie, partner Planet Labs, demo ~2027)]] - inicjatywy zakładającej umieszczenie akceleratorów TPU na orbicie z demonstratorem planowanym około 2027 r. Rola Planet w tym ekosystemie nie polega jednak na dostarczaniu mocy obliczeniowej dla hyperscalera, lecz wynika z jego unikalnych kompetencji konstelacyjnych: projektowania, budowy i operowania flot satelitarnych na dużą skalę.

Te kompetencje są realne i policzalne. Planet operuje ponad 200 aktywnymi satelitami, a od 2013 r. wystrzelił ponad 650 sztuk, generując codziennie około 25 TB danych (🟠 eoportal / SpaceCapital, 2025). Flota obejmuje platformy PlanetScope, SkySat oraz nową generację Pelican i Tanager. To właśnie tu pojawia się wątek orbitalnego compute: satelity Pelican (Pelican-2 ze stycznia 2025, Pelican-4 z sierpnia 2025) integrują moduły NVIDIA Jetson Orin do przetwarzania AI bezpośrednio na orbicie. 7 kwietnia 2026 r. Planet ogłosił pierwszy udany test onboard AI object detection - wykrywanie samolotów nad Alice Springs w Australii bezpośrednio na Pelican-4 (🟠 AeroMorning, 2026).

Ekspozycja Planet na orbitalne compute jest zatem kompetencyjna, a nie produktowa. Spółka dysponuje "edge" w kosmosie (Jetson na satelitach) oraz naziemnym zapleczem przetwarzania: własną siecią 48 stacji naziemnych w 11 krajach z downlinkiem do około 10 Gbps (🟠 eoportal / OrbitalRadar, 2025). W odróżnieniu od inicjatyw nastawionych na surową moc obliczeniową na orbicie - jak [[10 - gracze-i-projekty#StarCloud (dawniej Lumen Orbit) - działający demonstrator z NVIDIA H100]] czy [[10 - gracze-i-projekty#SpaceX - od Starlink-as-compute przez wniosek o 1 mln satelitów po pionową integrację (TeraFab, xAI, S-1)]] - Planet wnosi do tematu dojrzałą platformę wdrożeniową i heritage operacyjny floty obrazowania, a nie ambicję zostania orbitalnym data center.
<!-- spolki:temat:gracze-i-projekty:end -->

<!-- spolki:grafiki:start -->
## Materiały spółki

> Grafiki z materiałów spółki / IR (prawa właściciela, użycie redakcyjne). Pełny rejestr: `Spolki/assets/_licencje.json`.

![](assets/planet-labs-1-f1c6941fcb974c464f69ec320930e383.jpg)
*![Pelican-2 first light wide](. Źródło: materiały spółki / IR; licencja: materiały spółki / IR - prawa właściciela, użycie redakcyjne.*

![](assets/planet-labs-2-2bbf17532eff92c42a6237505d4c0405.jpg)
*![Pelican AI Insights](. Źródło: materiały spółki / IR; licencja: materiały spółki / IR - prawa właściciela, użycie redakcyjne.*

<!-- spolki:grafiki:end -->


<!-- spolki:pozycja:start -->
## Pozycja rynkowa

Planet jest liderem komercyjnej obserwacji Ziemi pod względem skali konstelacji - codziennie skanuje całą lądową powierzchnię globu w rozdzielczości około 3 m, co daje mu unikalną platformę do wdrażania AI w kosmosie. Skala biznesu pozostaje jednak niewielka jak na rynek "compute": przychód za FY2025 (rok zakończony 31 stycznia 2025) wyniósł 244,4 mln USD, +11% r/r (🔵 Q1 FY2026 earnings release / IR, 2025). Q1 FY2026 (zakończony 30 kwietnia 2025) przyniósł rekordowe 66,3 mln USD, +10% r/r (🔵 Q1 FY2026 earnings release, 2025).

Kluczowy fakt dla inwestora: udział orbitalnego / onboard compute w sprzedaży jest marginalny i NIE UJAWNIONY. Planet nie raportuje osobno przychodów z edge computing; traktuje je jako część stacku Data & AI-Enabled Solutions oraz Satellite Services. Rdzeniem przychodów pozostają subskrypcje obrazowania i analityki, nie zmonetaryzowany produkt "compute na orbicie". W segmencie Satellite Services widać natomiast skalę zdolności konstrukcyjnych - umowa z JSAT na 10 satelitów Pelican o wartości 230 mln USD (🟠 IR / prasa, 2025).

W komercyjnym obrazowaniu Planet konkuruje z Maxar Technologies (WorldView Legion, rozdzielczość 0,3 m, silne kontrakty wywiadowcze), BlackSky Technology (1 m plus analityka AI, szybki tasking) oraz dostawcami SAR - ICEYE i Capella Space (all-weather imaging). Oś konkurencji to rozdzielczość i kontrakty obronne (gdzie Maxar dominuje) kontra częstotliwość rewizyty i skala floty (gdzie przewodzi Planet).
<!-- spolki:pozycja:end -->

<!-- spolki:przekroj:start -->
## Ryzyka

Pierwsze ryzyko jest fizyczne: ograniczenia zasobów na orbicie - mocy, chłodzenia, pasma i radiacji. Onboard AI na Jetson Orin zużywa energię i generuje ciepło, a satelity Planet mają ograniczoną pojemność baterii (około 650 Wh) i moc (około 600 W) (🟠 eoportal, 2025). Mechanizm zagrożenia: duże modele AI uruchamiane masowo na flocie mogą napotykać bariery termiczne i radiacyjne, co spowalnia komercjalizację niszy i odsuwa moment, w którym orbitalne compute zacznie realnie kontrybuować do przychodów. Dopóki to nie nastąpi, linia ta pozostaje kosztem rozwojowym, a nie źródłem marży.

Drugie ryzyko jest technologiczno-konkurencyjne. Onboard edge computing jest na wczesnym etapie, a sukces zależy od zdolności skalowania modeli AI na flocie ponad 200 satelitów. Rywalizacja z dostawcami NTN/Starlink oraz większymi graczami obronnymi (Airbus, Maxar, Northrop Grumman) może przyspieszyć, zanim Planet osiągnie rentowność tej niszy - co grozi tym, że spółka poniesie nakłady badawczo-rozwojowe, lecz wartość przechwycą partnerzy dysponujący mocą obliczeniową lub kontraktami obronnymi. W relacji z Google w ramach Suncatcher pozycja Planet jest pozycją dostawcy kompetencji konstelacyjnych, nie właściciela monetyzowanej warstwy compute.
<!-- spolki:przekroj:end -->

<!-- network:peers:start -->
## Powiązane spółki

> Inne notowane spółki z raportu dzielące z tą firmą co najmniej jeden wątek tematyczny (wspólny rynek, technologia lub łańcuch wartości).

- [[Spolki/alphabet|Alphabet Inc. (GOOGL)]] - Project Suncatcher (TPU na orbicie)  
  *Wspólne wątki: Gracze i projekty.*
- [[Spolki/nvidia|NVIDIA Corporation (NVDA)]] - Akceleratory GPU (COTS) - ładunek obliczeniowy on-orbit  
  *Wspólne wątki: Gracze i projekty.*
- [[Spolki/rocket-lab|Rocket Lab Corporation (RKLB)]] - Launch (Electron/Neutron) + Space Systems: bus, ogniwa SolAero, komponenty  
  *Wspólne wątki: Gracze i projekty.*
- [[Spolki/voyager-technologies|Voyager Technologies, Inc. (VOYG)]] - Stacje kosmiczne (Starlab), systemy kosmiczne i obronne  
  *Wspólne wątki: Gracze i projekty.*
<!-- network:peers:end -->

<!-- spolki:zrodla:start -->

<!-- spolki:zrodla:end -->

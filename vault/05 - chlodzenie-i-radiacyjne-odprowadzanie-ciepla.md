---
tytul: Chłodzenie i radiacyjne odprowadzanie ciepła
sekcja_idx: 4
source_tier: primary
tematy: ["chlodzenie-i-radiacyjne-odprowadzanie-ciepla"]
data_utworzenia: "2026-06-16"
---

# Chłodzenie i radiacyjne odprowadzanie ciepła

> Notatka raportu "Orbitalne centra danych". Kluczowe źródła: [źródło 1](https://projectgeospatial.org/geospatial-frontiers/the-thermodynamics-of-hype-why-space-wont-save-ais-energy-crisis-yet), [źródło 2](https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf).

## W skrócie

Chłodzenie jest najtwardszym fizycznym ograniczeniem orbitalnych centrów danych i jednocześnie miejscem, gdzie najłatwiej o marketingowy mit "w kosmosie jest zimno, więc chłodzenie jest darmowe". W rzeczywistości próżnia jest izolatorem: nie ma powietrza ani wody, więc jedynym sposobem pozbycia się ciepła jest promieniowanie podczerwone w głąb kosmosu, a tempo tego promieniowania rządzi się prawem Stefana-Boltzmanna (moc rośnie z czwartą potęgą temperatury). Praktyczna konsekwencja dla inwestora: aby odprowadzić zaledwie 1 megawat (MW = milion watów) ciepła odpadowego przy temperaturze bezpiecznej dla chipów, trzeba rozłożyć radiator o powierzchni rzędu 1 200 m², czyli wielkości czterech kortów tenisowych ([Project Geospatial](https://projectgeospatial.org/geospatial-frontiers/the-thermodynamics-of-hype-why-space-wont-save-ais-energy-crisis-yet)). Kto na tym zyskuje: dostawcy lekkich, rozkładanych radiatorów i pętli dwufazowych (np. Starcloud, ESA/Thales). Kto traci lub jest narażony na ryzyko: projekty zakładające skalowanie do gigawatów (GW) na bazie samego dziedzictwa ISS, bo największy lotny system chłodzenia (ISS, ~70-126 kW) trzeba przeskalować o 4-5 rzędów wielkości - a takiego demonstratora w skali MW jeszcze nie ma w kosmosie (NIE UJAWNIONE). Tempo zmian jest powolne i napędzane masą wyniesienia: opłacalność zależy od spadku kosztu startu do okolic 500 USD/kg.


<!-- spolki:related:start -->
## Spółki powiązane

> Notowane spółki produkujące podzespoły/technologie związane z tym tematem. Pełne omówienie: spółki, dla których nisza to >=33% przychodów; skrótowe: zdywersyfikowane konglomeraty. Zob. też [[Spolki/_slownik]] i [[Spolki/_widok-gpw-eu]].

**Producenci kluczowi (>=33% przychodów z niszy - omówienie pełne):**
- [[Spolki/redwire|Redwire Corporation (RDW)]] - Panele ROSA, struktury rozkładane, montaż on-orbit, radiatory Q-Rad
- [[Spolki/vertiv|Vertiv Holdings Co (VRT)]] - Zasilanie i precyzyjne/cieczowe chłodzenie DC

**Pozostali dominujący gracze (nisza to ułamek przychodów - omówienie skrótowe):**
- [[Spolki/northrop-grumman|Northrop Grumman Corporation (NOC)]] - Serwis GEO (MEV/MRV), busy, radiatory, ogniwa
- [[Spolki/airbus|Airbus SE (AIR)]] 🇪🇺 - PV (Sparkwing), optyka (Tesat), busy, serwis (EU)
- [[Spolki/rtx|RTX Corporation (RTX)]] - ADCS (Blue Canyon), termika (Collins Aerospace)
- [[Spolki/eaton|Eaton Corporation plc (ETN)]] - Zasilanie DC (UPS, switchgear) + chłodzenie (Boyd Thermal)
<!-- spolki:related:end -->

<!-- network:watki:start -->
## Powiązane wątki

> Mapa powiązań tematycznych - jak ten wątek łączy się z resztą raportu.

- [[04 - energetyka-kosmiczna-i-fotowoltaika-orbitalna|Energetyka kosmiczna]] - każdy wat mocy obliczeniowej trzeba odprowadzić jako ciepło
- [[03 - fizyka-orbitalna-orbity-i-operacje|Fizyka orbitalna]] - orientacja radiatorów edge-on do Słońca to zagadnienie operacji
- [[06 - promieniowanie-i-elektronika-rad-hard-vs-cots|Promieniowanie i elektronika]] - rosnące TDP akceleratorów AI napędza wymaganą powierzchnię radiatora
- [[08 - niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu|Niezawodność i serwisowanie]] - radiatory rozkładane to element niezawodności i serwisu
- [[09 - ekonomika-i-koszty-calkowite-tco|Ekonomika i TCO]] - setki ton radiatora na MW to realny koszt w rachunku startowym
<!-- network:watki:end -->
## Mechanizm: dlaczego w próżni liczy się tylko promieniowanie

Na Ziemi serwery chłodzi się przez konwekcję - przepływ powietrza lub cieczy zabierający ciepło z gorących powierzchni. W próżni ten mechanizm znika całkowicie. 🔵 Dokumentacja NASA stawia to jednoznacznie: "in a vacuum environment, convection is no longer available and the only mechanism of rejecting heat is radiation" ([NASA NTRS](https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf)). To samo widać na ISS, gdzie podgrzany amoniak krąży przez wielkie radiatory na zewnątrz stacji i oddaje ciepło "by radiation to space" ([NASA ISS ATCS](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf)).

Tempo wypromieniowania opisuje prawo Stefana-Boltzmanna: emitowana moc na jednostkę powierzchni jest proporcjonalna do czwartej potęgi temperatury bezwzględnej (w kelwinach, K - skala zaczynająca się od zera absolutnego). 🔵 NASA zapisuje je jako E = σT⁴, gdzie stała Stefana-Boltzmanna σ wynosi 5,67 (w jednostkach W·m⁻²·K⁻⁴, czyli wat na metr kwadratowy na kelwin do czwartej potęgi) ([NASA NTRS](https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf)). Dla porządku: dokładna wartość CODATA to 5,670374419×10⁻⁸ W·m⁻²·K⁻⁴ (NIE UJAWNIONE w przeglądanych źródłach NASA, podaną tu jako proxy; źródła NASA cytują zaokrąglone 5,67). Implikacja dla inwestora: kluczowa jest temperatura pracy radiatora - im gorętszy radiator, tym dramatycznie mniejszy i lżejszy może być, więc cała ekonomika chłodzenia orbitalnego zależy od tego, jak wysoką temperaturę chipów i pętli akceptujemy.

<abbr title="duża płyta oddająca ciepło do kosmosu przez promieniowanie; im niższa temperatura pracy, tym większy i cięższy musi być.">Radiator</abbr> promieniuje głównie w stronę "głębokiego kosmosu", którego średnia temperatura to około 2,7 K (-270°C). 🔵 Tak opisuje to white paper Starcloud (d. Lumen Orbit): "radiating primarily towards deep space, which has an average temperature of about 2.7 Kelvin or -270°C" ([Starcloud WP](https://lumenorbit.github.io/wp.pdf)). 🔵 NASA podkreśla zarazem odwrotną stronę medalu: całkowite wypromieniowane ciepło jest proporcjonalne do powierzchni radiatora, a "the lower the radiation temperature, the larger the radiator area (and thus the radiator mass, for a given design) must be" ([NASA NTRS](https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf)). To jest sedno problemu: chcąc utrzymać chipy chłodne, trzeba olbrzymich, ciężkich powierzchni.

## Powierzchnia i masa radiatorów na 1 MW; stosunek radiator do panela

Najczęściej cytowana liczba bazowa to powierzchnia radiatora na jednostkę odprowadzanej mocy. 🟠 Project Geospatial podaje ~1 200 m² na 1 MW odprowadzanego ciepła przy temperaturach bezpiecznych dla komercyjnych mikroprocesorów ([Project Geospatial](https://projectgeospatial.org/geospatial-frontiers/the-thermodynamics-of-hype-why-space-wont-save-ais-energy-crisis-yet)). 🟠 Niezależnie SatNews podaje tę samą wartość 1 200 m²/MW przy stabilnych 20°C, porównując ją do "czterech kortów tenisowych" ([SatNews](https://satnews.com/2026/03/17/the-physics-wall-orbiting-data-centers-face-a-massive-cooling-challenge/)). To zbieżność dwóch wtórnych źródeł na konserwatywnym (niskotemperaturowym) końcu skali.

Liczba spada drastycznie, gdy podniesiemy temperaturę radiatora. 🟠 Reguła kciuka z peraspera.us mówi o ~0,1 m² na kW, czyli zaledwie ~100 m²/MW, ale przy ~350 K (około 77°C) ([peraspera.us](https://peraspera.us/realities-of-space-based-compute/)). 🔴 Skrajny przykład w drugą stronę: analiza adsbnetwork podaje aż 24 000 m²/MW "w <abbr title="orbita blisko Ziemi, gdzie radiatory ponoszą dodatkowy &quot;podatek termiczny&quot; od albedo i podczerwieni planety.">LEO</abbr> przy 350 K" ([adsbnetwork](https://www.adsbnetwork.com/mypov/Starcloud/physics.html)) - to wartość odstająca o dwa rzędy wielkości od pozostałych i opatrzona najniższym tierem wiarygodności. 🔴 InfinityTurbine liczy 222 m² dla 100 kW przy strumieniu 450 W/m² (czyli ~2 220 m²/MW) ([InfinityTurbine](https://www.infinityturbine.com/orbital-data-centers-using-cluster-mesh-supercritical-co2-power-systems-by-infinityturbine.html)). Implikacja dla inwestora: nie istnieje jedna "prawdziwa" liczba m²/MW - rozrzut od ~100 do ~24 000 m²/MW pokazuje, że wynik jest sterowany założeniem temperatury i konfiguracji, a nie twardą stałą; każdy biznesplan trzeba czytać przez pryzmat przyjętej temperatury pracy.

```mermaid
xychart-beta
    title "Powierzchnia radiatora na 1 MW (rozrzut zrodel)"
    x-axis ["peraspera 350K", "ProjGeo/SatNews 20C", "InfinityTurbine 450W/m2", "adsbnetwork 350K LEO"]
    y-axis "m2 na MW" 0 --> 24000
    bar [100, 1200, 2220, 24000]
```

*Rys. 24 - Powierzchnia radiatora potrzebna do odprowadzenia 1 MW ciepła wedlug roznych zrodel; wynik sterowany glownie zalozona temperatura. Dane: peraspera.us, Project Geospatial, SatNews, InfinityTurbine, adsbnetwork (notatka).*

Masa to druga oś problemu. 🔵 Radiatory ISS (EETCS) mają dwustronną masę właściwą 2,75 kg/m² i pracują w ~300 K ([CORE/EETCS](https://core.ac.uk/download/pdf/36694932.pdf)). 🔵 NASA wskazuje ~5 kg/m² dla starannie zaprojektowanego radiatora aluminiowego z emisyjnością 0,85 (emisyjność to ułamek od 0 do 1 mówiący, jak skutecznie powierzchnia promieniuje względem ciała doskonale czarnego) ([NASA NTRS](https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf)). 🟠 Forethought podaje dla całego systemu radiatora z pętlą 2,4-3,6 kg/m² (kompozyt z włókna węglowego plus 50% narzutu na pompy, instalację, płyny), co daje 163-346 W/kg w zależności od konfiguracji i temperatury (25°C vs 45°C) ([Forethought](https://www.forethought.org/research/will-we-really-put-data-centers-in-space)). 🟠 Bardziej zachowawczo SpaceComputer przyjmuje typowy zakres 5-10 kg/m² dla radiatorów kosmicznych ([SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/)).

Przeliczone na megawat, masa układu chłodzenia rozjeżdża się równie mocno. 🟠 Project Geospatial szacuje całkowitą masę chłodzenia na ~2 640-14 400 kg/MW ([Project Geospatial](https://projectgeospatial.org/geospatial-frontiers/the-thermodynamics-of-hype-why-space-wont-save-ais-energy-crisis-yet)). 🔴 adsbnetwork twierdzi za to "43 tony minimum na 1 MW" w oparciu o dane ISS, co miałoby stanowić 25% całkowitej masy 1 MW orbitalnego DC ([adsbnetwork](https://www.adsbnetwork.com/mypov/Starcloud/physics.html)). Implikacja dla inwestora: masa radiatorów na 1 MW waha się od ~2,6 t do ~43 t w zależności od źródła i założeń, a ponieważ każdy kilogram trzeba wynieść na orbitę, to właśnie ta liczba decyduje o koszcie kapitałowym - górny koniec zakładałby koszt wyniesienia samego chłodzenia liczony w dziesiątkach milionów dolarów na MW przy dzisiejszych cenach startu.

Co do skali wizji: 🔵 white paper Starcloud podaje, że dla klastra 5 GW potrzebny byłby radiator o boku 1 km × 1 km ([Starcloud WP](https://lumenorbit.github.io/wp.pdf)), przy czym te same dokumenty twierdzą, że "radiatory muszą być mniejsze niż połowa rozmiaru paneli słonecznych" - stosunek radiator do panela ok. 1/2 ([Starcloud WP](https://lumenorbit.github.io/wp.pdf)). Implikacja: panel zbierający energię jest większy niż radiator ją oddający, co odwraca naiwną intuicję, że to chłodzenie zdominuje geometrię stacji - choć liczba 1/2 pochodzi od firmy promującej technologię i jest claimem optymistycznym.

## Technologie: heat pipes, pętle, układy dwufazowe i radiatory rozkładane

🔵 Bazowym, referencyjnym rozwiązaniem jest "heat pipe" (rurka cieplna) - urządzenie całkowicie pasywne, bez ruchomych części, względem którego ocenia się wszystkie inne ([NASA NTRS](https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf)). Działa dzięki parowaniu i skraplaniu czynnika wewnątrz rurki. 🔵 <abbr title="rozwinięta, pasywna pętla przenosząca ciepło od gorącego sprzętu do zewnętrznego radiatora bez pompy mechanicznej.">Loop Heat Pipe</abbr> (LHP, pętlowa rurka cieplna) rozwija ten pomysł: przenosi ciepło dzięki utajonemu ciepłu parowania od gorącego sprzętu do zimnego radiatora zewnętrznego, jest "totally passive (no mechanical pump)" i używa kapilarnego parownika dającego przepływ dwufazowy ([ESA LHP](https://connectivity.esa.int/projects/high-performance-loop-heat-pipe)). 🔵 ESA wskazuje LHP jako rozwiązanie dla "large powerful SATCOM" wymagających radiatorów rozkładanych ([ESA LHP](https://connectivity.esa.int/projects/high-performance-loop-heat-pipe)).

Gdy mocy jest więcej, sięga się po pętle z pompą mechaniczną. 🔵 Mechanically pumped fluid loops (<abbr title="aktywny układ tłoczący płyn pompą, zdolny przenosić ciepło dalej niż heat pipe; preferowany przy dużych mocach.">MPFL</abbr>, pętle płynowe z pompą) działają w trybie jedno- i dwufazowym, transportują ciepło dalej niż heat pipes i są "current technology of choice for high heat flux applications and precision temperature control" w misjach dalekiego kosmosu NASA ([NASA MPFL](https://ntrs.nasa.gov/api/citations/20020013939/downloads/20020013939.pdf)). To one są naturalnym kandydatem do skali MW, bo gęstości mocy chipów AI wymagają precyzyjnej kontroli temperatury.

Radiatory rozkładane (deployable) to sposób na zmieszczenie wielkiej powierzchni w ograniczonej objętości rakiety. 🟠 Panele rozkładane po starcie dają dodatkowe 10-30 m² powierzchni, łączone z pojazdem przez elastyczne interfejsy heat-pipe ([rfessentials](https://rfessentials.com/rf-knowledge-base/how-do-i-design-the-thermal-management-system-for-an-rf-payload-in-a-satellite/)). 🔵 Recenzowane badanie pokazało, że nowatorski radiator rozkładany oferował 220% większą zdolność odprowadzania ciepła niż konwencjonalny montowany na korpusie ([Newswise/Elsevier](https://www.newswise.com/pdf_docs/171748902440796_1-s2.0-S277268352400013X-main.pdf)). 🔵 Praca na konferencji SmallSat opisuje LHP umożliwiające dwufazowy transfer ciepła przez mechanizmy rozkładania i izotermalizację radiatorów integralnych i rozkładanych ([USU SmallSat](https://digitalcommons.usu.edu/smallsat/2024/all2024/203/)).

Na horyzoncie są technologie potencjalnie przełomowe. 🟠 Liquid Droplet Radiator (LDR, radiator z kroplami cieczy) - badania NASA z lat 80. wskazują, że może być nawet 7× lżejszy od konwencjonalnego, a listopadowe (2025) badanie w Applied Thermal Engineering wykazało odprowadzanie do 450 W/kg ([SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/)). 🔴 InfinityTurbine proponuje "CO2 Cluster Mesh" na nadkrytycznym/transkrytycznym CO2 przy ciśnieniu ~80-200 bar, chwaląc się dużą pojemnością cieplną i kompaktowymi rurociągami ([InfinityTurbine](https://www.infinityturbine.com/orbital-data-centers-using-cluster-mesh-supercritical-co2-power-systems-by-infinityturbine.html)). Implikacja dla inwestora: zdecydowana większość dojrzałych komponentów (heat pipes, LHP, MPFL, radiatory ISS) ma już dziedzictwo lotne tier-primary, natomiast najbardziej "uskrzydlające" liczby (LDR 7×, 450 W/kg, CO2 80-200 bar) pochodzą z badań laboratoryjnych lub źródeł słabszego tieru - to opcjonalność, nie pewnik.

![[assets/y04-1-ksc-03pd2293.jpg]]
*Rys. 25 - Chlodzenie: KENNEDY SPACE CENTER, FLA.  -  A worker at Hangar A&E, Cape Canaveral Air Force . Źródło: NASA, licencja: public domain.*
#grafika #chlodzenie-i-radiacyjne-odprowadzanie-ciepla #radiator #chlodzenie

![[assets/y04-2-ksc-03pd2294.jpg]]
*Rys. 26 - Chlodzenie: KENNEDY SPACE CENTER, FLA.  - Workers at Hangar A&E, Cape Canaveral Air Force St. Źródło: NASA, licencja: public domain.*
#grafika #chlodzenie-i-radiacyjne-odprowadzanie-ciepla #radiator #chlodzenie

## Dziedzictwo ISS: pętle amoniakalne w skali kilowatów, skalowane do MW

ISS to jedyny duży, długo działający w kosmosie układ aktywnego chłodzenia i dlatego stanowi punkt odniesienia. 🔵 External Active Thermal Control System (EATCS) zaprojektowano na 35 kW odprowadzania ciepła na pętlę, łącznie 70 kW ([NASA ISS ATCS](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf)). 🔵 Każdy Photovoltaic Radiator (PVR) odprowadza do 14 kW ([NASA ISS ATCS](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf)), waży 740,7 kg i po rozłożeniu mierzy 3,12 m × 13,6 m ([NASA ISS ATCS](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf)). 🔵 Radiatory EETCS mają łączną powierzchnię odprowadzania ~147 m² i odprowadzają 14 kW jako pumpowana pętla amoniakalna ([CORE/EETCS](https://core.ac.uk/download/pdf/36694932.pdf)).

```mermaid
xychart-beta
    title "Zdolnosc chlodzenia ISS (kW)"
    x-axis ["PVR (1 panel)", "EETCS petla", "EATCS calosc", "ISS wszystkie petle"]
    y-axis "kW" 0 --> 126
    bar [14, 14, 70, 126]
```

*Rys. 27 - Maksymalna zdolnosc odprowadzania ciepla podsystemow ISS; punkt odniesienia ledwie ulamek MW. Dane: NASA ISS ATCS, CORE/EETCS, yage.ai (notatka).*

Inne analizy podają zagregowane liczby całej stacji, nieco rozbieżne. 🟠 SpaceComputer mówi o odprowadzaniu do 70 kW przez 422 m² radiatorów amoniakalnych, co daje w praktyce ~166 W/m² - znacznie poniżej teoretycznego maksimum z powodu nasłonecznienia, obciążenia podczerwienią Ziemi i nieefektywności systemu ([SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/)). 🟠 Z kolei analiza yage.ai cytuje "dokumentację NASA": całkowita zdolność chłodzenia ~126 kW, łączna powierzchnia radiatorów ~645 m², łączna masa radiatorów ~9,7 t ([yage.ai](https://yage.ai/share/space-datacenter-thermal-en-20260421.html)). 🔴 adsbnetwork wylicza z tego 51 kg/kW masy radiatora ISS ([adsbnetwork](https://www.adsbnetwork.com/mypov/Starcloud/physics.html)). Implikacja: nawet podstawowe parametry ISS są raportowane w widełkach (70 vs 126 kW; 422 vs 645 m²) zależnie od tego, czy liczy się sam EATCS, czy wszystkie pętle - inwestor powinien wymagać doprecyzowania, którą część systemu przytacza dany pitch.

Czynnik roboczy ma swoje ryzyka. 🟠 EATCS przenosi ładunek 600 funtów (lb) amoniaku w dwóch komorach ([naturalrefrigerationreview](https://naturalrefrigerationreview.com/a-service-call-in-space/)); 🔵 amoniak wybrano za skrajnie niski punkt zamarzania -77°C ([NASA ISS ATCS](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf)). Kluczowa luka: NIE UJAWNIONE są jakiekolwiek lotne demonstratory chłodzenia w skali MW - proxy mówi wprost, że największy lotny system to ISS (~70-126 kW), a osiągnięcie GW wymaga skalowania o 4-5 rzędów wielkości. Implikacja dla inwestora: między obecnym dziedzictwem a wizją GW leży nieprzetestowana w locie przepaść technologiczna - to ryzyko wykonawcze, nie tylko fizyczne.

## Gęstość mocy chipów AI a ekstrakcja ciepła bez wody i powietrza

To, co trzeba schłodzić, rośnie szybciej niż łatwość chłodzenia. 🔵 NVIDIA H100 w wersji SXM ma <abbr title="projektowa moc cieplna układu (np. 700 W dla GPU H100), którą system chłodzenia musi odprowadzić.">TDP</abbr> (Thermal Design Power, projektowa moc cieplna do odprowadzenia) do 700 W ([NVIDIA datasheet](https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf)), a wersja PCIe 300-350 W ([NVIDIA datasheet](https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf)). 🟠 Dla porównania: NVIDIA A100 400 W, AMD MI300X 750 W, Google TPU v5 450 W na chip ([DataBank](https://www.databank.com/resources/blogs/colocation-for-ai-workloads-power-cooling-gpu-density-requirements-explained/)). 🔴 Nowsza NVIDIA B200 Blackwell ma pobierać 1 200 W na sztukę ([qyang](https://qyang.livedoor.blog/archives/13219248.html)).

```mermaid
xychart-beta
    title "TDP akceleratorow AI (W na chip)"
    x-axis ["A100", "TPU v5", "H100 SXM", "MI300X", "B200"]
    y-axis "W (TDP)" 0 --> 1200
    bar [400, 450, 700, 750, 1200]
```

*Rys. 28 - Projektowa moc cieplna (TDP) na pojedynczy akcelerator; wzrost z 400 W do 1200 W zwieksza wymagana powierzchnie radiatora. Dane: NVIDIA datasheet, DataBank, qyang (notatka).*

W skali szafy (rack) liczby są ogromne. 🟠 NVIDIA GB200 NVL72 to 120 kW/rack, GB300 NVL72 to 140 kW/rack ([resistancezero](https://resistancezero.com/article-13.html)); 🔴 pody Google TPU v5 mają działać przy 150 kW/rack ([qyang](https://qyang.livedoor.blog/archives/13219248.html)). Te gęstości na Ziemi wymuszają chłodzenie cieczą, a w próżni - jak przypomina NASA - "the only mechanism of rejecting heat is radiation" ([NASA NTRS](https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf)), bo nie ma ani wody, ani powietrza, tylko przewodzenie do radiatora i wypromieniowanie.

Przeliczenie na powierzchnię radiatora bywa zatrważające. 🔴 arkspace szacuje, że pojedynczy H100 (~350 W) wymaga ~1,1 m² radiatora, a system DGX H100 z ośmioma GPU ponad 16 m² - więcej niż typowe wymiary korpusu satelity ([arkspace](https://arkspace.me/blog/thermal-wall-orbital-data-center-cooling/)). Implikacja dla inwestora: trend rynkowy idzie pod prąd fizyce orbity - chipy AI z generacji na generację grzeją mocniej (700 W → 1 200 W), więc każdy rok zwłoki w starcie projektu oznacza, że trzeba schłodzić cieplejszy sprzęt; przewaga "darmowego heatsinku w próżni" topnieje wraz ze wzrostem TDP, choć te konkretne przeliczenia m²/GPU pochodzą ze źródeł słabego tieru.

## Orientacja radiatorów: edge-on do Słońca, podczerwień i albedo Ziemi

Radiator nie tylko promieniuje ciepło - również je odbiera z otoczenia, dlatego ustawienie ma znaczenie krytyczne. 🟠 Wymóg podstawowy: radiatory muszą być ustawione krawędzią do Słońca (edge-on) i osłonięte od Ziemi ([abgoyal](https://abgoyal.com/posts/space-ai-datacenters/)). Powodem jest strumień słoneczny. 🟠 Bezpośrednie nasłonecznienie to ~1 360-1 367 W/m² ([abgoyal](https://abgoyal.com/posts/space-ai-datacenters/); [MATEC](https://www.matec-conferences.org/articles/matecconf/pdf/2022/18/matecconf_3mce22_02001.pdf)); 🟠 coracleresearch podaje 1 361 W/m² dla LEO ([coracleresearch](https://www.coracleresearch.com/research/02-starship-refilling/)). Jeśli pełna powierzchnia radiatora "patrzy" w Słońce, pochłania więcej ciepła niż odprowadza.

Na niskiej orbicie (LEO, Low Earth Orbit) dochodzi obciążenie od samej Ziemi. 🟠 <abbr title="część światła słonecznego odbita od Ziemi (~30%), dodatkowo nagrzewająca radiatory na niskiej orbicie.">Albedo</abbr> Ziemi (odbite światło słoneczne) to ~30% padającego promieniowania słonecznego ([abgoyal](https://abgoyal.com/posts/space-ai-datacenters/)); 🟠 podczerwień Ziemi (<abbr title="ciepło promieniowane przez samą planetę (~240 W/m²), które obciąża radiatory zwrócone ku Ziemi na niskiej orbicie.">Earth IR</abbr>) to ~240 W/m² ([MATEC](https://www.matec-conferences.org/articles/matecconf/pdf/2022/18/matecconf_3mce22_02001.pdf)), a coracleresearch podaje łącznie albedo plus IR na stronie zwróconej do Ziemi ~240 W/m² ([coracleresearch](https://www.coracleresearch.com/research/02-starship-refilling/)). 🔵 NASA potwierdza, że w warunkach LEO earthshine i albedo "can be the dominant external heat inputs" ([NASA NTRS 1978](https://ntrs.nasa.gov/api/citations/19780014193/downloads/19780014193.pdf)) i wskazuje, że orientacja płaskich radiatorów w płaszczyźnie orbity minimalizuje wszystkie trzy obciążenia zewnętrzne przy najbardziej prawdopodobnych kątach β ([NASA NTRS 1978](https://ntrs.nasa.gov/api/citations/19780014193/downloads/19780014193.pdf)).

Dokładne właściwości optyczne radiatorów ODC w LEO są NIE UJAWNIONE - jako proxy z dziedzictwa ISS/Space Shuttle: absorpcyjność słoneczna ~0,09-0,14 i emisyjność ~0,84-0,92. Implikacja dla inwestora: efektywne ~166 W/m² ISS (zamiast teoretycznych setek W/m²) to nie błąd projektu, lecz cena za nasłonecznienie i podczerwień Ziemi - projekty w LEO ponoszą trwały "podatek termiczny" od bliskości planety, co preferuje orbity wyższe lub staranne pasywne sterowanie orientacją i jest realnym kosztem inżynieryjnym ukrytym w optymistycznych liczbach m²/MW.

## Kontrowersje

**Kontrowersja A: Czy radiator GW to twardy blocker fizyki, czy handlowy trade-off?**

Strona sceptyczna (blocker): 🟠 Project Geospatial liczy 1 200 m²/MW i masę chłodzenia ~2 640-14 400 kg/MW ([Project Geospatial](https://projectgeospatial.org/geospatial-frontiers/the-thermodynamics-of-hype-why-space-wont-save-ais-energy-crisis-yet)). 🟠 chaotropy.com idzie dalej: 1-3 m² na kW, czyli 1-3 mln m² dla gigawata, a własne wyliczenia autora dają "at least 2.2 million m²" dla 1 GW ([chaotropy](https://www.chaotropy.com/why-jeff-bezos-is-probably-wrong-predicting-ai-data-centers-in-space/)).

Strona optymistyczna (trade-off): 🟠 SpaceComputer twierdzi, że przy skalowaniu satelity klasy Starlink z ~20 kW do ~100 kW radiatory stanowią tylko 10-20% masy i ~7% powierzchni planarnej ([SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/)), a dla 1 GW potrzeba "tylko" ~3 950 m² radiatora przy optymistycznych temperaturach, o masie 19 750-39 500 kg przy 5-10 kg/m² ([SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/)). 🔵 Starcloud mówi o radiatorze 1 km × 1 km dla 5 GW ([Starcloud WP](https://lumenorbit.github.io/wp.pdf)). Rozbieżność jest realna i ogromna: ~3 950 m² (SpaceComputer) kontra ~2,2 mln m² (chaotropy) dla 1 GW - różnica niemal trzech rzędów wielkości, wynikająca z założonej temperatury pracy radiatora. To nie spór o fizykę, lecz o to, jak gorące radiatory uda się utrzymać.

**Kontrowersja B: Czy dziedzictwo ISS skaluje się do ODC?**

Strona "nie skaluje się łatwo": 🔵 maksimum EATCS to 70 kW ([NASA ISS ATCS](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf)), czyli ułamek megawata. 🟠 System amoniakalny doświadczył "repeated ammonia leaks" przez ponad 20 lat służby i udokumentowanych awaryjnych napraw EVA (spacerów kosmicznych) ([yage.ai](https://yage.ai/share/space-datacenter-thermal-en-20260421.html)) - co przy skali GW oznaczałoby ekstremalne ryzyko operacyjne.

Strona "heritage jest bazą, nowe technologie pozwalają skalować": 🔵 dokument NASA o radiatorze reaktora wprost twierdzi, że układ chłodzenia podobny do ISS "provides development benefits since that system has space heritage" ([NASA TM-20220012395](https://ntrs.nasa.gov/api/citations/20220012395/downloads/TM-20220012395.pdf)). 🔵 Starcloud deklaruje, że "has not found any insurmountable obstacles" ([Starcloud WP](https://lumenorbit.github.io/wp.pdf)). 🟠 W perspektywie LDR demonstruje 450 W/kg ([SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/)). Spór sprowadza się do tego, czy 4-5 rzędów wielkości skalowania to inżynieryjna ciągłość, czy jakościowy skok - obie strony cytują źródła primary, więc rozstrzygnięcie zależy od przyszłych demonstratorów lotnych (na razie NIE UJAWNIONE).

**Kontrowersja C: Czy "trudniej w próżni" jest prawdą absolutną?**

Strona "tak, trudniej niż na Ziemi": 🟠 systemy konwekcyjne na Ziemi odprowadzają 2 000+ W/m² przy minimalnym narzucie masy, podczas gdy w próżni "there is no fluid medium" ([SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/)) - a radiatory ISS dają w praktyce tylko ~166 W/m² ([SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/)). 🟠 GB300 wymaga "mandatory liquid cooling" już przy 140 kW/rack ([resistancezero](https://resistancezero.com/article-13.html)). Różnica wydajności jest realna: ~166 W/m² (orbita) vs 2 000+ W/m² (Ziemia), czyli ponad rząd wielkości na niekorzyść próżni.

```mermaid
xychart-beta
    title "Strumien odprowadzanego ciepla (W/m2)"
    x-axis ["Radiator ISS (orbita)", "Konwekcja (Ziemia)"]
    y-axis "W/m2" 0 --> 2000
    bar [166, 2000]
```

*Rys. 29 - Praktyczna wydajnosc odprowadzania ciepla: radiator ISS na orbicie vs systemy konwekcyjne na Ziemi. Dane: SpaceComputer (notatka).*

Strona "zależy od porównania; woda i powietrze nie są darmowe": 🟠 SiliconAngle podkreśla, że radiatory to urządzenia pasywne o prostszej konstrukcji i mniejszym zużyciu energii niż naziemne systemy chłodzenia ([SiliconAngle](https://siliconangle.com/2026/03/30/space-data-center-startup-starcloud-raises-170m-1-1b-valuation/)). 🟠 whatthechiphappened akcentuje, że orbita daje próżnię jako heat sink "avoiding evaporative cooling and conserving fresh water" potrzebnej naziemnym DC ([whatthechiphappened](https://news.whatthechiphappened.com/p/semiconductors-next-frontier-starclouds)). Synteza: teza "trudniej w próżni" jest półprawdą - pod względem czystej wydajności na m² faktycznie jest trudniej (166 vs 2 000+ W/m²), ale orbita eliminuje zużycie wody i daje stałe, pasywne chłodzenie radiacyjne; ocena zależy od tego, czy porównujemy wydajność termiczną, czy całkowity koszt operacyjny z wodą i energią pomp.

## Słowniczek pojęć

- **Promieniowanie cieplne (radiacja)** - oddawanie ciepła w postaci podczerwieni; w próżni jedyny możliwy sposób chłodzenia, bo nie ma powietrza ani wody.
- **Prawo Stefana-Boltzmanna (E = σT⁴)** - zasada fizyki mówiąca, że moc wypromieniowana z powierzchni rośnie z czwartą potęgą jej temperatury, więc gorętszy radiator oddaje ciepło dużo skuteczniej.
- **Konwekcja** - chłodzenie przez przepływ powietrza lub cieczy (standard na Ziemi), które w próżni kosmosu w ogóle nie działa.
- **Radiator** - duża płyta oddająca ciepło do kosmosu przez promieniowanie; im niższa temperatura pracy, tym większy i cięższy musi być.
- **Emisyjność** - liczba od 0 do 1 określająca, jak skutecznie powierzchnia promieniuje ciepło w porównaniu z idealnym "ciałem czarnym".
- **Heat pipe (rurka cieplna)** - całkowicie pasywne urządzenie bez ruchomych części, przenoszące ciepło dzięki parowaniu i skraplaniu czynnika wewnątrz rurki.
- **Loop Heat Pipe (LHP, pętlowa rurka cieplna)** - rozwinięta, pasywna pętla przenosząca ciepło od gorącego sprzętu do zewnętrznego radiatora bez pompy mechanicznej.
- **MPFL (pętla płynowa z pompą)** - aktywny układ tłoczący płyn pompą, zdolny przenosić ciepło dalej niż heat pipe; preferowany przy dużych mocach.
- **Układ dwufazowy (two-phase)** - chłodzenie wykorzystujące przemianę cieczy w parę i z powrotem, co pozwala przenieść dużo ciepła przy małym przepływie.
- **Radiator rozkładany (deployable)** - panel składany podczas startu i rozkładany na orbicie, aby zmieścić wielką powierzchnię chłodzącą w ciasnej rakiecie.
- **Earth IR (podczerwień Ziemi)** - ciepło promieniowane przez samą planetę (~240 W/m²), które obciąża radiatory zwrócone ku Ziemi na niskiej orbicie.
- **Albedo** - część światła słonecznego odbita od Ziemi (~30%), dodatkowo nagrzewająca radiatory na niskiej orbicie.
- **Edge-on do Słońca** - ustawienie radiatora krawędzią do Słońca, by pochłaniał jak najmniej promieniowania słonecznego.
- **Gęstość mocy** - ilość ciepła do odprowadzenia z danej powierzchni lub szafy (np. kW na rack); im wyższa, tym trudniejsze chłodzenie.
- **TDP (Thermal Design Power)** - projektowa moc cieplna układu (np. 700 W dla GPU H100), którą system chłodzenia musi odprowadzić.
- **LEO (Low Earth Orbit, niska orbita okołoziemska)** - orbita blisko Ziemi, gdzie radiatory ponoszą dodatkowy "podatek termiczny" od albedo i podczerwieni planety.


## Źródła

- [NASA NTRS 19930007720](https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf) 🔵 - podstawy fizyki radiatorów kosmicznych, Stefan-Boltzmann, heat pipes, kg/m².
- [NASA ISS ATCS overview](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf) 🔵 - architektura chłodzenia ISS (EATCS, PVR), amoniak.
- [CORE / EETCS](https://core.ac.uk/download/pdf/36694932.pdf) 🔵 - parametry radiatorów EETCS ISS (147 m², 2,75 kg/m², 14 kW).
- [Starcloud (Lumen Orbit) white paper](https://lumenorbit.github.io/wp.pdf) 🔵 - wizja 5 GW, radiator 1×1 km, stosunek radiator do panela, deep space 2,7 K.
- [NASA MPFL 20020013939](https://ntrs.nasa.gov/api/citations/20020013939/downloads/20020013939.pdf) 🔵 - pętle płynowe z pompą do wysokich strumieni ciepła.
- [ESA High Performance LHP](https://connectivity.esa.int/projects/high-performance-loop-heat-pipe) 🔵 - loop heat pipe dla dużych SATCOM, radiatory rozkładane.
- [Newswise/Elsevier deployable radiator](https://www.newswise.com/pdf_docs/171748902440796_1-s2.0-S277268352400013X-main.pdf) 🔵 - radiator rozkładany 220% wydajniejszy.
- [USU SmallSat 2024](https://digitalcommons.usu.edu/smallsat/2024/all2024/203/) 🔵 - LHP i izotermalizacja radiatorów rozkładanych.
- [NASA NTRS 19780014193](https://ntrs.nasa.gov/api/citations/19780014193/downloads/19780014193.pdf) 🔵 - earthshine/albedo dominujące w LEO, orientacja radiatorów.
- [NASA TM-20220012395](https://ntrs.nasa.gov/api/citations/20220012395/downloads/TM-20220012395.pdf) 🔵 - dziedzictwo chłodzenia ISS jako baza projektowa.
- [NVIDIA H100 datasheet](https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf) 🔵 - TDP H100 (700 W / 350 W).
- [Project Geospatial](https://projectgeospatial.org/geospatial-frontiers/the-thermodynamics-of-hype-why-space-wont-save-ais-energy-crisis-yet) 🟠 - 1 200 m²/MW, masa chłodzenia, teza sceptyczna.
- [SatNews](https://satnews.com/2026/03/17/the-physics-wall-orbiting-data-centers-face-a-massive-cooling-challenge/) 🟠 - 1 200 m²/MW przy 20°C.
- [peraspera.us](https://peraspera.us/realities-of-space-based-compute/) 🟠 - reguła kciuka ~0,1 m²/kW przy 350 K.
- [Forethought](https://www.forethought.org/research/will-we-really-put-data-centers-in-space) 🟠 - 2,4-3,6 kg/m², 163-346 W/kg.
- [SpaceComputer](https://blog.spacecomputer.io/cooling-for-orbital-compute/) 🟠 - skalowanie do 1 GW, 166 W/m², LDR 450 W/kg, ISS 422 m².
- [yage.ai](https://yage.ai/share/space-datacenter-thermal-en-20260421.html) 🟠 - agregaty ISS (126 kW, 645 m², 9,7 t), przecieki amoniaku.
- [naturalrefrigerationreview](https://naturalrefrigerationreview.com/a-service-call-in-space/) 🟠 - ładunek amoniaku 600 lb.
- [DataBank](https://www.databank.com/resources/blogs/colocation-for-ai-workloads-power-cooling-gpu-density-requirements-explained/) 🟠 - TDP A100/MI300X/TPU v5.
- [resistancezero](https://resistancezero.com/article-13.html) 🟠 - 120-140 kW/rack GB200/GB300, mandatory liquid cooling.
- [abgoyal](https://abgoyal.com/posts/space-ai-datacenters/) 🟠 - orientacja edge-on, strumień słoneczny, albedo 30%.
- [MATEC](https://www.matec-conferences.org/articles/matecconf/pdf/2022/18/matecconf_3mce22_02001.pdf) 🟠 - strumień słoneczny 1367, Earth IR 240 W/m².
- [coracleresearch](https://www.coracleresearch.com/research/02-starship-refilling/) 🟠 - strumienie cieplne w LEO (1361 i ~240 W/m²).
- [chaotropy](https://www.chaotropy.com/why-jeff-bezos-is-probably-wrong-predicting-ai-data-centers-in-space/) 🟠 - 1-3 mln m² i ~2,2 mln m² dla 1 GW.
- [SiliconAngle](https://siliconangle.com/2026/03/30/space-data-center-startup-starcloud-raises-170m-1-1b-valuation/) 🟠 - radiatory pasywne, prostsze niż naziemne.
- [whatthechiphappened](https://news.whatthechiphappened.com/p/semiconductors-next-frontier-starclouds) 🟠 - oszczędność wody, próżnia jako heat sink.
- [adsbnetwork](https://www.adsbnetwork.com/mypov/Starcloud/physics.html) 🔴 - 24 000 m²/MW, 43 t/MW, 51 kg/kW.
- [InfinityTurbine](https://www.infinityturbine.com/orbital-data-centers-using-cluster-mesh-supercritical-co2-power-systems-by-infinityturbine.html) 🔴 - 222 m²/100 kW, CO2 cluster mesh 80-200 bar.
- [qyang](https://qyang.livedoor.blog/archives/13219248.html) 🔴 - B200 1200 W, TPU v5 pody 150 kW/rack.
- [arkspace](https://arkspace.me/blog/thermal-wall-orbital-data-center-cooling/) 🔴 - 1,1 m²/H100, 16 m²/DGX H100.

## Dane źródłowe

- `5,67 W·m⁻²·K⁻⁴` | https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf | primary | "Radiation follows the Stefan-Boltzmann Law E = σT⁴ where σ, the Stefan-Boltzmann constant, = 5.67 W m⁻² K⁻⁴"
- `brak konwekcji w próżni` | https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf | primary | "It should be pointed out that in a vacuum environment, convection is no longer available and the only mechanism of rejecting heat is radiation."
- `radiacja jedynym sposobem (ISS)` | https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | primary | "The heated ammonia circulates through large radiators located on the exterior of the Space Station, releasing the heat by radiation to space"
- `2,7 K (-270°C)` | https://lumenorbit.github.io/wp.pdf | primary | "radiating primarily towards deep space, which has an average temperature of about 2.7 Kelvin or -270°C"
- `T⁴ zależność` | https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf | primary | "the total amount of heat radiated is proportional to the surface area of the radiator. And the lower the radiation temperature, the larger the radiator area (and thus the radiator mass, for a given design) must be."
- `1200 m²/MW` | https://projectgeospatial.org/geospatial-frontiers/the-thermodynamics-of-hype-why-space-wont-save-ais-energy-crisis-yet | secondary | "To reject 1 MW of waste heat into deep space while maintaining safe operating temperatures for commercial microprocessors, an orbital data center requires a radiating surface area of approximately 1,200 square meters."
- `1200 m²/MW (20°C)` | https://satnews.com/2026/03/17/the-physics-wall-orbiting-data-centers-face-a-massive-cooling-challenge/ | secondary | "To dissipate just 1 megawatt (MW) of heat while keeping electronics at a stable 20°C, an ODC would require a radiator surface of approximately 1,200 square meters-roughly the size of four tennis courts."
- `24000 m²/MW (350 K)` | https://www.adsbnetwork.com/mypov/Starcloud/physics.html | weak | "To dissipate 1 MW in LEO: 24,000 m² of radiators at 350 K."
- `100 m²/MW (~350 K)` | https://peraspera.us/realities-of-space-based-compute/ | secondary | "A rule of thumb: roughly 0.1 m² of radiator might be needed per kW of heat to reject, if operating around 350 K."
- `222 m²/100 kW (450 W/m²)` | https://www.infinityturbine.com/orbital-data-centers-using-cluster-mesh-supercritical-co2-power-systems-by-infinityturbine.html | weak | "A = 100,000 W / 450 W/m²; A ≈ 222 m²"
- `163-346 W/kg` | https://www.forethought.org/research/will-we-really-put-data-centers-in-space | secondary | "giving 3.6 kg/m² system mass and ~163 W/kg at 25°C. While our actual best guess... 1.0 mm carbon fibre honeycomb at 1.6 kg/m², same 50% overhead, giving 2.4 kg/m² and ~346 W/kg at 45°C."
- `2,4-3,6 kg/m²` | https://www.forethought.org/research/will-we-really-put-data-centers-in-space | secondary | "For the conservative case we calculate using, 1.5 mm carbon fibre composite panels at 2.4 kg/m², plus 50% overhead for fluid loops, pumps, and plumbing, giving 3.6 kg/m² system mass"
- `2,75 kg/m² (EETCS ISS)` | https://core.ac.uk/download/pdf/36694932.pdf | primary | "These radiators operate at ~300 K and have a two-sided specific mass of 2.75 kg/m²"
- `5-10 kg/m²` | https://blog.spacecomputer.io/cooling-for-orbital-compute/ | secondary | "Scaling that to a 1 GW facility... would require approximately 3,950 m² of radiator at optimistic operating temperatures, with a mass of 19,750 to 39,500 kg at 5-10 kg/m²."
- `2640-14400 kg/MW` | https://projectgeospatial.org/geospatial-frontiers/the-thermodynamics-of-hype-why-space-wont-save-ais-energy-crisis-yet | secondary | "Total Estimated Cooling Mass: ~2,640 kg to ~14,400 kg"
- `43 t/MW (ISS)` | https://www.adsbnetwork.com/mypov/Starcloud/physics.html | weak | "43 tonnes minimum per MW in orbit (ISS data). That is 25% of the total mass of a 1 MW orbital datacenter."
- `1 km × 1 km radiator (5 GW)` | https://lumenorbit.github.io/wp.pdf | primary | "a 1 km by 1 km square of radiator would be required to dissipate the heat"
- `1/2 stosunek radiator do panela` | https://lumenorbit.github.io/wp.pdf | primary | "these radiators need to be less than half the size of the solar arrays"
- `heat pipe pasywny` | https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf | primary | "Heat pipes: The first of these, called the 'heat pipe,' is conventionally considered the base system against which all others are judged. It has the significant advantage of being completely passive, with no moving parts"
- `~5 kg/m² (aluminium, emis. 0,85)` | https://ntrs.nasa.gov/api/citations/19930007720/downloads/19930007720.pdf | primary | "A very carefully designed solid surface radiator made out of aluminum has the following capabilities in principle: The mass is approximately 5 kg/m² with an emissivity of 0.85"
- `LHP dla SATCOM` | https://connectivity.esa.int/projects/high-performance-loop-heat-pipe | primary | "This thermal device is designed for large powerful SATCOM, which should use deployable radiator. It will then allow having highly dissipative payload onboard limited spacecraft volume."
- `LHP pasywny, capillary evaporator` | https://connectivity.esa.int/projects/high-performance-loop-heat-pipe | primary | "The Loop Heat Pipe is a thermal device, which carry heat owing to latent heat of vaporisation, from the hot dissipative equipment to the cold external radiator. This device, totally passive (no mechanical pump), use a capillary evaporator which provides a two phase flow owing to capillary suction."
- `MPFL high heat flux` | https://ntrs.nasa.gov/api/citations/20020013939/downloads/20020013939.pdf | primary | "Mechanically pumped fluid loops have been used in both single phase and two-phase modes to transport heat a greater distance than is possible with heat pipes or capillary pumped loops. It is the current technology of choice for high heat flux applications and precision temperature control for NASA's deep space science missions."
- `10-30 m² (deployable)` | https://rfessentials.com/rf-knowledge-base/how-do-i-design-the-thermal-management-system-for-an-rf-payload-in-a-satellite/ | secondary | "Deployable radiator panels unfold after launch, providing additional 10-30 m² of radiator area. Connected to the spacecraft via flexible heat pipe interfaces."
- `220% więcej (deployable)` | https://www.newswise.com/pdf_docs/171748902440796_1-s2.0-S277268352400013X-main.pdf | primary | "Results showed that the novel deployable radiator offered 220% more heat dissipation capacity than the conventional body-mounted radiator."
- `LDR do 7× lżejszy; 450 W/kg` | https://blog.spacecomputer.io/cooling-for-orbital-compute/ | secondary | "NASA research dating to the 1980s showed LDRs can be up to seven times lighter than conventional radiators. A November 2025 study in Applied Thermal Engineering demonstrated heat dissipation rates of up to 450 W/kg."
- `CO2 80-200 bar` | https://www.infinityturbine.com/orbital-data-centers-using-cluster-mesh-supercritical-co2-power-systems-by-infinityturbine.html | weak | "Supercritical or transcritical CO2; Pressure range: ~80-200 bar; High heat capacity and compact piping"
- `LHP izotermalizacja deployable` | https://digitalcommons.usu.edu/smallsat/2024/all2024/203/ | primary | "Additionally, LHPs allow for two-phase heat transfer across deployment mechanisms, allowing for isothermalization of both integrated and deployable radiators, unlocking the CubeSat Thermal Capacity."
- `70 kW (EATCS)` | https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | primary | "The EATCS is designed to provide 35 kW of heat rejection per loop for a total capability of 70 kW."
- `14 kW (PVR)` | https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | primary | "In total, the PVR can reject up to 14 kW of heat into deep space."
- `740,7 kg (PVR)` | https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | primary | "The PVR weighs 1,633 pounds (740.7 kilograms) and when deployed measures 10.24 feet (3.12 meters) by 44.62 feet (13.6 meters)."
- `3,12 × 13,6 m (PVR)` | https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | primary | "when deployed measures 10.24 feet (3.12 meters) by 44.62 feet (13.6 meters)"
- `147 m² (EETCS)` | https://core.ac.uk/download/pdf/36694932.pdf | primary | "These radiators have a total heat rejection area of approximately 147 m²"
- `14 kW (EETCS)` | https://core.ac.uk/download/pdf/36694932.pdf | primary | "The EETCS is a pumped loop ammonium thermal control system that is designed to reject 14 kW of waste heat to space."
- `422 m² (ammonia-loop ISS)` | https://blog.spacecomputer.io/cooling-for-orbital-compute/ | secondary | "Its External Active Thermal Control System rejects up to 70 kW using 422 m² of ammonia-loop radiators, achieving roughly 166 W/m² in practice"
- `166 W/m² (ISS EATCS)` | https://blog.spacecomputer.io/cooling-for-orbital-compute/ | secondary | "achieving roughly 166 W/m² in practice, well below theoretical maximums because of solar exposure, Earth IR loading, and system inefficiencies"
- `126 kW (ISS, inna analiza)` | https://yage.ai/share/space-datacenter-thermal-en-20260421.html | secondary | "NASA's technical documentation gives these parameters: Total station cooling capacity: ~126 kW; Total radiator panel area: ~645 square meters; Total radiator panel mass: ~9.7 tons"
- `645 m² (ISS, inna analiza)` | https://yage.ai/share/space-datacenter-thermal-en-20260421.html | secondary | "Total radiator panel area: ~645 square meters (slightly larger than a tennis court)"
- `9,7 t (ISS, inna analiza)` | https://yage.ai/share/space-datacenter-thermal-en-20260421.html | secondary | "Total radiator panel mass: ~9.7 tons"
- `51 kg/kW (ISS)` | https://www.adsbnetwork.com/mypov/Starcloud/physics.html | weak | "The ISS uses 51 kg/kW for its radiators"
- `600 lb amoniaku (EATCS)` | https://naturalrefrigerationreview.com/a-service-call-in-space/ | secondary | "a tank which contains a 600 lb ammonia charge in two separate chambers"
- `-77°C (zamarzanie amoniaku)` | https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | primary | "Ammonia has an extremely low freezing point of -107 degrees °F (-77°C) at standard atmospheric pressure"
- `700 W (H100 SXM TDP)` | https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf | primary | "Max thermal design power (TDP): Up to 700W (configurable)"
- `350 W (H100 PCIe TDP)` | https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf | primary | "300-350W (configurable)"
- `400 W (A100 TDP)` | https://www.databank.com/resources/blogs/colocation-for-ai-workloads-power-cooling-gpu-density-requirements-explained/ | secondary | "NVIDIA A100: 400W per GPU"
- `750 W (MI300X TDP)` | https://www.databank.com/resources/blogs/colocation-for-ai-workloads-power-cooling-gpu-density-requirements-explained/ | secondary | "AMD MI300X: 750W per GPU"
- `450 W (TPU v5 TDP)` | https://www.databank.com/resources/blogs/colocation-for-ai-workloads-power-cooling-gpu-density-requirements-explained/ | secondary | "Google TPU v5: 450W per chip"
- `1200 W (B200)` | https://qyang.livedoor.blog/archives/13219248.html | weak | "NVIDIA's B200 Blackwell GPU consumes 1,200W per unit (up from H100's 700W)"
- `120 kW/rack (GB200 NVL72)` | https://resistancezero.com/article-13.html | secondary | "NVIDIA GB200 NVL72: 120 kW/rack"
- `140 kW/rack (GB300 NVL72)` | https://resistancezero.com/article-13.html | secondary | "NVIDIA GB300 NVL72: 140 kW/rack"
- `150 kW/rack (TPU v5 pods)` | https://qyang.livedoor.blog/archives/13219248.html | weak | "Google's TPU v5 pods operate at 150kW per rack"
- `1,1 m²/H100 (~350 W)` | https://arkspace.me/blog/thermal-wall-orbital-data-center-cooling/ | weak | "A single Nvidia H100 GPU consumes approximately 350W in terrestrial data centers. Dissipating this power in space requires roughly 1.1 m² of radiator surface area."
- `16 m²/DGX H100 (8 GPU)` | https://arkspace.me/blog/thermal-wall-orbital-data-center-cooling/ | weak | "A DGX H100 system with eight GPUs needs over 16 m² of radiators, exceeding typical satellite body dimensions"
- `edge-on do Słońca` | https://abgoyal.com/posts/space-ai-datacenters/ | secondary | "the radiators must be edge-on to the sun and shielded from Earth"
- `1360-1367 W/m² (strumień słoneczny)` | https://www.matec-conferences.org/articles/matecconf/pdf/2022/18/matecconf_3mce22_02001.pdf | secondary | "Solar flux (W/m²): 1367"
- `~30% albedo Ziemi` | https://abgoyal.com/posts/space-ai-datacenters/ | secondary | "Earth Albedo: Sunlight reflected off Earth (~30% of incident solar)"
- `240 W/m² (Earth IR)` | https://www.matec-conferences.org/articles/matecconf/pdf/2022/18/matecconf_3mce22_02001.pdf | secondary | "Earth flux (W/m²): 240"
- `earthshine/albedo dominujące w LEO` | https://ntrs.nasa.gov/api/citations/19780014193/downloads/19780014193.pdf | primary | "Under LEO conditions, earthshine and albedo can be the dominant external heat inputs."
- `orientacja w płaszczyźnie orbity` | https://ntrs.nasa.gov/api/citations/19780014193/downloads/19780014193.pdf | primary | "Orienting extendable flat radiators in the orbital plane tends to minimize all three external inputs at most probable β angles"
- `~240 W/m² (albedo+IR, strona do Ziemi)` | https://www.coracleresearch.com/research/02-starship-refilling/ | secondary | "Earth albedo plus outgoing infrared at approximately 240 watts per square meter on the Earth-facing side"
- `1361 W/m² (bezpośrednie słońce LEO)` | https://www.coracleresearch.com/research/02-starship-refilling/ | secondary | "A Starship in LEO sees three incident heat fluxes on its tank walls: direct solar at 1361 watts per square meter"
- `2000+ W/m² (konwekcja na Ziemi)` | https://blog.spacecomputer.io/cooling-for-orbital-compute/ | secondary | "Convective systems remove heat at 2,000+ W/m2 with minimal mass penalty. In the vacuum of space, there is no fluid medium."
- `1-3 mln m² dla GW; 2,2 mln m²` | https://www.chaotropy.com/why-jeff-bezos-is-probably-wrong-predicting-ai-data-centers-in-space/ | secondary | "That implies on the order of 1-3 m² of radiator area per kilowatt, or 1-3 million m² for a gigawatt data center... my calculations for a one gigawatt data center yield a necessary surface area of at least 2.2 million m²"
- `10-20% masy, ~7% powierzchni (100 kW)` | https://blog.spacecomputer.io/cooling-for-orbital-compute/ | secondary | "when scaling a Starlink-class spacecraft from approximately 20 kW to approximately 100 kW (compute-optimized), radiators represent only 10-20% of total mass and roughly 7% of total planform area"
- `3950 m² dla 1 GW; 19750-39500 kg` | https://blog.spacecomputer.io/cooling-for-orbital-compute/ | secondary | "Scaling that to a 1 GW facility... would require approximately 3,950 m² of radiator at optimistic operating temperatures, with a mass of 19,750 to 39,500 kg at 5-10 kg/m²"
- `przecieki amoniaku / EVA naprawy` | https://yage.ai/share/space-datacenter-thermal-en-20260421.html | secondary | "This system has suffered repeated ammonia leaks over its twenty-plus years of service. NASA has documented multiple emergency EVA repairs"
- `ISS heritage development benefits` | https://ntrs.nasa.gov/api/citations/20220012395/downloads/TM-20220012395.pdf | primary | "Utilizing a coolant design similar to that of the ISS radiator coolant system provides development benefits since that system has space heritage."
- `no insurmountable obstacles` | https://lumenorbit.github.io/wp.pdf | primary | "Starcloud has developed a range of concept designs and has not found any insurmountable obstacles"
- `radiatory pasywne, prostsze niż naziemne` | https://siliconangle.com/2026/03/30/space-data-center-startup-starcloud-raises-170m-1-1b-valuation/ | secondary | "The radiators used for the task are passive devices, which means they have a simpler design and use less power than terrestrial cooling systems."
- `oszczędność wody, próżnia jako heat sink` | https://news.whatthechiphappened.com/p/semiconductors-next-frontier-starclouds | secondary | "and the vacuum of space as a heat sink, avoiding evaporative cooling and conserving fresh water that terrestrial data centers would otherwise need."

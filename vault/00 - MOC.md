# Orbitalne / kosmiczne centra danych

> Pogłębiony raport tematyczny (wiki Obsidian). Punktem wyjścia był polski artykuł sceptyczny "Centra przetwarzania danych na orbicie nie mają sensu", którego tezy raport krytycznie weryfikuje.

## O raporcie

Raport powstał metodą wielomodelową: panel zakresu (3 modele) zdefiniował 15 sekcji, badania faktograficzne prowadził agent webowy Kimi (15 przebiegów + 7 wątków odkrywczych), syntezę i redakcję wykonał Opus, kontrolę jakości deterministyczne walidatory. Każda liczba niesie źródło i poziom wiarygodności: 🔵 pierwotne, 🟠 wtórne, 🔴 słabe. Pojęcia techniczne mają dymki (najedź kursorem) i słowniczki; dane zilustrowano własnymi wykresami z twardych liczb oraz figurami z paperów i materiałów graczy.

## Najważniejsze ustalenia

- W styczniu 2026 SpaceX złożył do FCC wniosek na "Orbital Data Center system" - konstelację do **1 mln satelitów** (zob. [[10 - gracze-i-projekty]], [[01 - wprowadzenie-definicje-i-architektury]]).
- Wyścig jest globalny: Blue Origin "Project Sunrise" (~51 600 sat, NIE Amazon), StarCloud (~88 000 sat), chińskie ITU (~96 714 sat), Google "Project Suncatcher" (81 sat TPU, 10 Tbps) (zob. [[10 - gracze-i-projekty]]).
- Sceptyczny artykuł myli liczby: realny udźwig Falcon 9 na SSO to ok. **7541 kg, nie 15 t**; 5500 USD/kg to cena z 2022 (dziś ~7000) (zob. [[02 - weryfikacja-tez-sceptycznego-artykulu]]).
- Największy spór to ekonomika - rozbieżność o **rzędy wielkości**: Starcloud ~20x niższy TCO vs SemiAnalysis ~4x drożej niż na Ziemi (zob. [[09 - ekonomika-i-koszty-calkowite-tco]]).
- Fizyka twarda: w próżni ciepło odprowadza się tylko przez promieniowanie, stąd ogromne radiatory (zob. [[05 - chlodzenie-i-radiacyjne-odprowadzanie-ciepla]]).
- Koszt środowiskowy skali: przy 1 mln satelitów i ~5-letnim cyklu trzeba by deorbitować **~200 000 satelitów rocznie** (zob. [[14 - zrownowazony-rozwoj-i-srodowisko]]).
- Nowe osie: power-beaming jako usługa, arbitraż jurysdykcji danych, kilometrowe panele -7 mag vs astronomia, kompresja semantyczna obalająca tezę o downlinku (zob. [[07 - lacznosc-optyczne-isl-downlink-i-latencja]], [[13 - sentyment-spoleczny-i-moratoria-na-centra-danych]]).

## Sekcje

- [[01 - wprowadzenie-definicje-i-architektury]]
- [[02 - weryfikacja-tez-sceptycznego-artykulu]]
- [[03 - fizyka-orbitalna-orbity-i-operacje]]
- [[04 - energetyka-kosmiczna-i-fotowoltaika-orbitalna]]
- [[05 - chlodzenie-i-radiacyjne-odprowadzanie-ciepla]]
- [[06 - promieniowanie-i-elektronika-rad-hard-vs-cots]]
- [[07 - lacznosc-optyczne-isl-downlink-i-latencja]]
- [[08 - niezawodnosc-serwisowanie-i-cykl-zycia-sprzetu]]
- [[09 - ekonomika-i-koszty-calkowite-tco]]
- [[10 - gracze-i-projekty]]
- [[11 - regulacje-prawo-kosmiczne-debris-i-itu]]
- [[12 - naziemny-bottleneck-energetyczny-i-sieciowy]]
- [[13 - sentyment-spoleczny-i-moratoria-na-centra-danych]]
- [[14 - zrownowazony-rozwoj-i-srodowisko]]
- [[15 - bezpieczenstwo-geopolityka-i-realizm-10-letni]]

<!-- spolki:moc:start -->
## Warstwa spółek giełdowych

Do raportu dodano warstwę **26 notowanych spółek** produkujących podzespoły/technologie dla orbitalnych centrów danych oraz naziemnej infrastruktury DC. Podział wg udziału niszy w przychodach (próg 33%): **13 omówionych pełnie** (pure-playe/core biznesu) i **13 skrótowo** (zdywersyfikowane konglomeraty, dla których nisza to ułamek sprzedaży). Każda notatka spółki linkuje do konkretnych sekcji notatek tematycznych (mapa powiązań). Indeksy: [[Spolki/_slownik]], [[Spolki/_widok-gpw-eu]].

**Omówienie pełne (kluczowi producenci niszy, >=33% przychodów):**
- [[Spolki/rocket-lab|Rocket Lab Corporation (RKLB)]] - Launch (Electron/Neutron) + Space Systems: bus, ogniwa SolAero, komponenty
- [[Spolki/redwire|Redwire Corporation (RDW)]] - Panele ROSA, struktury rozkładane, montaż on-orbit, radiatory Q-Rad
- [[Spolki/voyager-technologies|Voyager Technologies, Inc. (VOYG)]] - Stacje kosmiczne (Starlab), systemy kosmiczne i obronne
- [[Spolki/mda-space|MDA Space Ltd. (MDA)]] - Robotyka kosmiczna (Canadarm), busy, anteny
- [[Spolki/astroscale|Astroscale Holdings Inc. (186A)]] - Pure-play serwisowanie i usuwanie śmieci (ADR)
- [[Spolki/mynaric|Mynaric AG (MYNA)]] - Pure-play terminale laserowe OISL (CONDOR) - WYCOFANA z giełdy, przejęta przez Rocket Lab (2026)
- [[Spolki/bloom-energy|Bloom Energy Corporation (BE)]] - Ogniwa paliwowe SOFC dla centrów danych
- [[Spolki/ge-vernova|GE Vernova Inc. (GEV)]] - Turbiny gazowe i infrastruktura sieciowa dla DC
- [[Spolki/vertiv|Vertiv Holdings Co (VRT)]] - Zasilanie i precyzyjne/cieczowe chłodzenie DC
- [[Spolki/constellation-energy|Constellation Energy Corporation (CEG)]] - Największy operator floty jądrowej w USA (PPA z hyperskalerami)
- [[Spolki/oklo|Oklo Inc. (OKLO)]] - Mikroreaktory (SMR/fission) na potrzeby DC
- [[Spolki/talen-energy|Talen Energy Corporation (TLN)]] - Energia jądrowa (Susquehanna), sąsiedztwo z DC
- [[Spolki/siemens-energy|Siemens Energy AG (ENR)]] - Turbiny gazowe i technologie sieciowe (EU)

**Omówienie skrótowe (dominujący producenci, ale nisza to ułamek przychodów):**
- [[Spolki/nvidia|NVIDIA Corporation (NVDA)]] - Akceleratory GPU (COTS) - ładunek obliczeniowy on-orbit
- [[Spolki/amd|Advanced Micro Devices, Inc. (AMD)]] - Rad-tolerant FPGA/SoC (Versal/Xilinx) + GPU
- [[Spolki/microchip|Microchip Technology Incorporated (MCHP)]] - Rad-hard/rad-tolerant FPGA (RTG4) i mikrokontrolery
- [[Spolki/bae-systems|BAE Systems plc (BA)]] - Rad-hard procesory (RAD750/RAD5545); optyka (Ball)
- [[Spolki/northrop-grumman|Northrop Grumman Corporation (NOC)]] - Serwis GEO (MEV/MRV), busy, radiatory, ogniwa
- [[Spolki/airbus|Airbus SE (AIR)]] - PV (Sparkwing), optyka (Tesat), busy, serwis (EU)
- [[Spolki/rtx|RTX Corporation (RTX)]] - ADCS (Blue Canyon), termika (Collins Aerospace)
- [[Spolki/lockheed-martin|Lockheed Martin Corporation (LMT)]] - Busy satelitarne, serwisowanie, ULA (launch)
- [[Spolki/l3harris|L3Harris Technologies, Inc. (LHX)]] - Terminale laserowe dla obronności (SDA/NRO)
- [[Spolki/eaton|Eaton Corporation plc (ETN)]] - Zasilanie DC (UPS, switchgear) + chłodzenie (Boyd Thermal)
- [[Spolki/schneider-electric|Schneider Electric SE (SU)]] - Zasilanie i chłodzenie DC (EcoStruxure, Motivair)
- [[Spolki/alphabet|Alphabet Inc. (GOOGL)]] - Project Suncatcher (TPU na orbicie)
- [[Spolki/planet-labs|Planet Labs PBC (PL)]] - Partner Google Suncatcher (platformy/obrazowanie)
<!-- spolki:moc:end -->

## Metoda i modele (reprodukowalność)

- Synteza i redakcja: claude-opus-4-8
- Panel (zakres/walidacja/odkrywanie): codex + kimi + claude-opus-4-8
- Wizualizacje: własne wykresy Mermaid z twardych liczb + figury zewnętrzne (arXiv, NASA, materiały graczy) z notą licencyjną.
- Trzeci panelista: najnowszy Opus (Fable niedostępny). Data: 2026-06-16.

## Spis rycin

- Ryc. 1: skala deklarowanych konstelacji ODC wg graczy: wnioski FCC i projekty (SpaceX milion, Starcloud 88 tys., Blue Origin Project Sunrise 51,6 tys., chiński Three-Body 2800, klaster Google Suncatcher 81) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: FCC DA-26-113A1, siliconvalleyinvestclub (Starcloud), GeekWire (Blue Origin), dig.watch (Chiny), arXiv 2511.19468 (Google))
- Ryc. 2: Architektura Axiom Space Orbital Data Center (modul przy stacji komercyjnej) (zrodlo: Axiom Space / ITHome; licencja: materialy prasowe - do uzytku wlasnego)
- Ryc. 3: podwojenie globalnego zużycia prądu przez centra danych w scenariuszu bazowym IEA (415 TWh w 2024 do ok. 945 TWh w 2030) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: IEA - Energy and AI)
- Ryc. 4: ponad dwukrotny wzrost zapotrzebowania centrów danych na moc w USA (z prawie 35 GW w 2024 do 78 GW w 2035) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: BloombergNEF - Power for AI)
- Ryc. 5: Koncepcja modularnego orbitalnego DC Thales Alenia Space ASCEND (zrodlo: Thales Alenia Space / Satellite Today; licencja: materialy prasowe - do uzytku wlasnego)
- Ryc. 6: przepaść mocy między satelitą komunikacyjnym (poniżej 1 kW) a satelitami ODC (platforma K2 Giga 100 kW, Starcloud-3 200 kW) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: spacewar.com (sat. komunikacyjny), PR Newswire (K2 Space Giga), tech-insider (Starcloud-3))
- Ryc. 7: Krzywa kosztu wynoszenia SpaceX - weryfikacja tezy o oplacalnosci (zrodlo: Google Research / arXiv 2511.19468; licencja: arXiv open access - do uzytku wlasnego)
- Ryc. 8: Teza artykułu (15 t = 15000 kg) wobec udźwigu z przewodnika SpaceX dla orbity kołowej 600 km SSO (7541 kg) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Falcon 9 User Guide (Spaceflight Now))
- Ryc. 9: Procesor rad-hard BAE RAD750 (ponad 200 000 USD) wobec górnego szacunku układu COTS/RHBD (1200 USD za sztukę) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: RAD750 cost (MIT DSpace), FactMR rad-hard market)
- Ryc. 10: TCO (8,64 vs 2,37; ~3,6x) i LCOC z redundancją i radiacją (10,91 vs 2,49; ~4,4x) dla GPU B300 w 2026 (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SemiAnalysis - space datacenters)
- Ryc. 11: CAPEX na wat: orbitalnie 51,10 USD/W wobec 15,85 USD/W naziemnie (ponad 3x); analiza pierwszych zasad (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Andrew McCalip - space datacenters)
- Ryc. 12: Wysokości orbit: Google Suncatcher ~650 km, Starcloud (środek pasma 600-850 km), ASCEND/Thales ~1400 km, Bargatin DDSS ~1600 km (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: ISCR arXiv 2604.07760; FCC DOC-419509A1; Hello Future / Orange - ASCEND; Bargatin et al. arXiv 2512.09044)
- Ryc. 13: Roczny udział czasu w świetle słonecznym dla zwykłego LEO, zwykłej SSO i orbity terminatorowej (dawn-dusk) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Andrew McCalip - space datacenters)
- Ryc. 14: Górne wartości budżetów delta-V: kompensacja dragu w LEO, lot w szyku, deorbitacja EOL, roczna korekta orbity, unikanie kolizji (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Jones thesis (RMC))
- Ryc. 15: Google Suncatcher: konfiguracja klastra 81 satelitow na orbicie (zrodlo: Google Research / arXiv 2511.19468; licencja: arXiv open access - do uzytku wlasnego)
- Ryc. 16: Google Suncatcher: dynamika formacji satelitow w klastrze (zrodlo: Google Research / arXiv 2511.19468; licencja: arXiv open access - do uzytku wlasnego)
- Ryc. 17: Wnioskowana liczba satelitów: Google Suncatcher (81), Starcloud (88 000), SpaceX (1 000 000) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: ISCR arXiv 2604.07760; FCC DOC-419509A1; SpaceX Center / wniosek FCC)
- Ryc. 18: Stała słoneczna na orbicie wobec naziemnej insolacji w wybranych lokalizacjach; przewaga orbity to rząd 7-8x (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: NASA GSFC; World Energy Council 2013)
- Ryc. 19: Sprawność kosmicznych ogniw GaAs (triple-junction, AM0/BOL) wobec krzemu naziemnego (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: E3S/ESPC 2017; Mindway; Redwire IR; CAVU; Fraunhofer ISE)
- Ryc. 20: Energetyka: iss065e125924 (zrodlo: NASA; licencja: public domain)
- Ryc. 21: Energetyka: iss065e144542 (zrodlo: NASA; licencja: public domain)
- Ryc. 22: Moc właściwa: krzem naziemny wobec kosmicznych macierzy rolowanych (zmierzone iROSA i deklarowany blanket ROSA); mnożnik 3-5x na masie (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: pv-magazine; ScienceDirect/Yan 2025; Redwire flysheet)
- Ryc. 23: Udział energii padającego Słońca docierający do sieci po pełnym łańcuchu strat przesyłu wiązki w modelu NASA SBSP (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: NASA SBSP report 2024)
- Ryc. 24: Powierzchnia radiatora potrzebna do odprowadzenia 1 MW ciepła wedlug roznych zrodel; wynik sterowany glownie zalozona temperatura (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: peraspera.us, Project Geospatial, SatNews, InfinityTurbine, adsbnetwork (notatka))
- Ryc. 25: Chlodzenie: KENNEDY SPACE CENTER, FLA.  -  A worker at Hangar A&E, Cape Canaveral Air Force (zrodlo: NASA; licencja: public domain)
- Ryc. 26: Chlodzenie: KENNEDY SPACE CENTER, FLA.  - Workers at Hangar A&E, Cape Canaveral Air Force St (zrodlo: NASA; licencja: public domain)
- Ryc. 27: Maksymalna zdolnosc odprowadzania ciepla podsystemow ISS; punkt odniesienia ledwie ulamek MW (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: NASA ISS ATCS, CORE/EETCS, yage.ai (notatka))
- Ryc. 28: Projektowa moc cieplna (TDP) na pojedynczy akcelerator; wzrost z 400 W do 1200 W zwieksza wymagana powierzchnie radiatora (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: NVIDIA datasheet, DataBank, qyang (notatka))
- Ryc. 29: Praktyczna wydajnosc odprowadzania ciepla: radiator ISS na orbicie vs systemy konwekcyjne na Ziemi (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SpaceComputer (notatka))
- Ryc. 30: Roczna dawka TID przy osłonie 5 mm aluminium: LEO-Zero 136, LEO ISS 430, GEO 5930, GTO aż 59 630 rad(Si)/rok. Wybór orbity to wybór ryzyka radiacyjnego (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: laser2cots)
- Ryc. 31: Pasy radiacyjne Van Allena - srodowisko promieniowania na orbicie (zrodlo: NASA; licencja: public domain)
- Ryc. 32: Górne granice cen jednostkowych: COTS 500 USD, rad-tolerant/upscreened 5000 USD, pełny rad-hard klasy V 200 000 USD. Skala liniowa uwypukla, że rad-hard jest o rzędy wielkości droższy (dolne progi to odpowiednio 10, 500 i 10 000 USD) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Hubble)
- Ryc. 33: Koszt pamieci SRAM rad-hard vs COTS - skala roznicy cenowej (zrodlo: UPSat MSc thesis; licencja: akademickie - do uzytku wlasnego)
- Ryc. 34: Próg odporności TID: TPU Trillium 15 krad(Si) bez twardych awarii, Jetson Xavier 22-24 krad (tu 23), Jetson Orin 37-39 krad (tu 38), rad-hard AMD XQR Versal 100-120 krad (tu 110) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: arXiv 2511.19468 (Trillium), ESA/escies (Jetson), AMD DS946 (XQR Versal))
- Ryc. 35: Szacowana żywotność na orbicie LEO: COTS DRAM rzędu miesięcy (około 0,3 roku), COTS GPU około 2 lata, konfiguracja rad-hard 14 nm 10 lat, TPU Trillium do 15 lat. To żywotność decyduje o ekonomii orbitalnego DC (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: arXiv 2605.05615 (LLMSpace), arXiv 2512.09044 (UPenn))
- Ryc. 36: Optyczne lacza miedzysatelitarne (OISL) w konstelacji Suncatcher (zrodlo: Google Research / arXiv 2511.19468; licencja: arXiv open access - do uzytku wlasnego)
- Ryc. 37: Roadmapa przepustowości downlinku na satelitę: od 24 Gbps (V1.5) przez 96 Gbps (V2 Mini) do 1000 Gbps (V3) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SpaceX Starlink Progress Report 2024)
- Ryc. 38: Deklarowana przepustowość pojedynczego łącza laserowego: SDA (cel) 1 Gbps, Telesat 10 Gbps, Kuiper 100 Gbps, Starlink 200 Gbps (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SDA Transport SoW, Telesat Lightspeed, GeekWire, SpaceX)
- Ryc. 39: Mediana latencji LEO (Starlink 26 ms) kontra GEO (Kacific 599 ms, HughesNet 600-800 ms, tu 700 ms) - przewaga o rząd wielkości (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SpaceX Starlink Progress Report 2024, Ookla 2025)
- Ryc. 40: Redukcja objętości downlinku przez przetwarzanie on-orbit: NTT do 80%, SemCom 75%, Kodan 89%, patch-polygons dla obserwacji Ziemi do 99,996% (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: NTT Review, Queen's University Belfast, ACM Kodan, arXiv 2603.20317v1)
- Ryc. 41: Mission Robotic Vehicle (Northrop Grumman) - serwisowanie na orbicie (zrodlo: Northrop Grumman / SatellitePro ME; licencja: materialy prasowe - do uzytku wlasnego)
- Ryc. 42: HPE Spaceborne Computer-2 na ISS - heritage COTS w kosmosie (zrodlo: HPE / SatNews; licencja: materialy prasowe - do uzytku wlasnego)
- Ryc. 43: Oczekiwana osłonięta dawka w misji 5-letniej (750 rad = 0,75 krad), próg pierwszych nieprawidłowości (2 krad) i maksymalna testowana dawka bez trwałych awarii (15 krad) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Google Research - Project Suncatcher)
- Ryc. 44: Cykl odświeżania sprzętu na Ziemi (5-6 lat, środek 5,5) wobec żywotności na orbicie: Starcloud-1 (11 miesięcy = 0,92 roku), górna granica żywotności satelity (5-15 lat) i projektowy czas życia MEV (15 lat) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Horizon Technology, Gunter's Space Page, arXiv 2603.18601, eoPortal)
- Ryc. 45: Szacowany koszt centrum danych 1 GW na orbicie wobec naziemnego (luka około 3x) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: TechCrunch, AskSterling)
- Ryc. 46: Krzywa kosztu USD/kg SpaceX - cena startu determinuje oplacalnosc orbitalnego DC (zrodlo: Google Research / arXiv 2511.19468; licencja: arXiv open access - do uzytku wlasnego)
- Ryc. 47: Rozpiętość założeń kosztu wyniesienia: od 2720 USD/kg (Falcon 9 dziś) do 10 USD/kg (cel skrajnie optymistyczny) - ponad 250-krotna różnica napędzająca cały spór (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SpaceNexus, SemiAnalysis, InfoQ/Google, Starcloud, NextBigFuture)
- Ryc. 48: Koszt obliczeń w kosmosie wobec Ziemi w 2026: TCO 8,64 vs 2,37 (3,6x) oraz LCOC 10,91 vs 2,49 (4,4x) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SemiAnalysis)
- Ryc. 49: Nakłady na wat i zniwelowany koszt energii: CAPEX 51,10 vs 15,85 USD/W oraz LCOE 1167 vs 426 USD/MWh (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: andrewmccalip (interaktywny kalkulator))
- Ryc. 50: Bilans kosztu 40 MW przez 10 lat według Starcloud: 8,2 mln USD w kosmosie wobec 167 mln USD na Ziemi (około 20x taniej) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: whitepaper Starcloud)
- Ryc. 51: Wizualizacja orbitalnego DC Starcloud (d. Lumen Orbit) (zrodlo: Starcloud / Observer; licencja: materialy prasowe - do uzytku wlasnego)
- Ryc. 52: Starcloud-1 - demonstrator z NVIDIA H100 na orbicie (zrodlo: Starcloud / Financial Express; licencja: materialy prasowe - do uzytku wlasnego)
- Ryc. 53: Maksymalna liczba satelitów we wnioskach FCC trzech największych graczy (w tysiącach) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: notatka, wnioski FCC SpaceX (1 000 000), StarCloud (88 000), Blue Origin / Project Sunrise (51 600))
- Ryc. 54: Pozostałe konstelacje: autoryzacja Amazon Leo (>7700), TeraWave (5408), cel ADA Space "Star Compute" (2800), Orbital Chenguang (16) i pierwsza partia chińskiej Three-Body Computing Constellation już na orbicie (12) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: notatka (wnioski FCC, China-in-Space, media państwowe CN))
- Ryc. 55: Pozyskany kapitał / zabezpieczone finansowanie. Uwaga: Orbital Chenguang to 57,7 mld CNY (8,4 mld USD) linii kredytowych, nie wydana gotówka; StarCloud to łączny kapitał (z rundą Series A 170 mln USD); Lonestar to 6,6 mln USD łącznie (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: notatka (Carbon Credits, W.Media, DCD))
- Ryc. 56: Deklarowane cele mocy orbitalnej. StarCloud celuje w 5 GW (macierz słoneczna 4 km kw.), ASCEND w 1 GW przed 2050, a CASC w 1 GW w ramach 15. planu pięcioletniego (2026-2030) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: notatka (Payload Space, Thales Alenia Space, China-in-Space))
- Ryc. 57: Skokowy wzrost przepustowosci na satelite, az do deklarowanego 1 Tbps dla V3 (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Aviation Week (V1.5/V2 Mini), CompareBroadband (V3))
- Ryc. 58: Debris: An Astrobee robotic free-flyer with blue tentacle-like arms (zrodlo: NASA; licencja: public domain)
- Ryc. 59: Debris: Astronaut Suni Williams monitors an Astrobee robotic free-flyer (zrodlo: NASA; licencja: public domain)
- Ryc. 60: Dwudziestokrotny wzrost manewrow unikania kolizji Starlink w trzy lata (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: arXiv 2603.23552)
- Ryc. 61: Skrocenie wymaganego terminu deorbitu satelitow LEO z 25 do 5 lat (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SatelliteToday (regula FCC 5-year))
- Ryc. 62: Prognozowany wzrost rynku ODC z 0,5 mld do 39 mld USD w dekade (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: SalesGlobe)
- Ryc. 63: Zużycie prądu przez centra danych podwaja się z 415 TWh (2024) do 945 TWh (2030) w scenariuszu bazowym IEA (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: IEA - Energy and AI)
- Ryc. 64: Naziemne DC: ARC-2012-ACD12-0020-006 (zrodlo: NASA; licencja: public domain)
- Ryc. 65: Naziemne DC: New NASA 3D Animation Shows Seven Days of Simulated Earth Weather (zrodlo: NASA; licencja: public domain)
- Ryc. 66: Z 1,84 TW aktywnych wniosków o przyłączenie w USA tylko ok. 20% dochodzi do uruchomienia komercyjnego, reszta jest porzucana (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Allianz Research - AI energy)
- Ryc. 67: Czas od zamówienia do dostawy: switchgear 44 tygodnie, transformatory mocy 128 tygodni, GSU 144 tygodnie (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: POWER magazine (za Wood Mackenzie))
- Ryc. 68: Miks zasilania DC pozostaje zdominowany przez paliwa kopalne (ok. 60%), OZE ok. 27%, jądro ok. 15% (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: AIMultiple - AI energy consumption)
- Ryc. 69: Stosunek Amerykanów do budowy centrum danych AI w sąsiedztwie (sondaż Gallup, III.2026) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Gallup)
- Ryc. 70: Stosunek do nowych centrów danych w swoim stanie (Data for Progress, VIII.2025, N=1179; "brak zdania" jako dopełnienie do 100%) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Data for Progress)
- Ryc. 71: Wartość zablokowanych lub opóźnionych projektów DC w USA: suma oraz dwa największe pojedyncze przypadki (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Data Center Watch)
- Ryc. 72: Astronomia: Surface of TRAPPIST-1f (zrodlo: NASA; licencja: public domain)
- Ryc. 73: Astronomia: DSOC's Table Mountain Facility Uplink Laser - Infrared vs. Visible Light (zrodlo: NASA; licencja: public domain)
- Ryc. 74: Porównanie jasności: regulacyjny próg 7 mag i granica widoczności gołym okiem (ok. 6-7 mag) wobec paneli orbitalnych DC (-5 do -7 mag) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: arXiv 2603.28829, IAU CPS techdoc102)
- Ryc. 75: Inwentarz emisji startów rakietowych wstrzykniętych do stratosfery w 2019 r. (sadza i alumina mają nieproporcjonalny wpływ klimatyczno-ozonowy mimo małej masy) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Brown et al. / ORACLE (arXiv 2504.15291))
- Ryc. 76: Srodowisko: Flame Deflector Complete at Launch Complex 39B (zrodlo: NASA; licencja: public domain)
- Ryc. 77: Srodowisko: Flame Deflector Complete at Launch Complex 39B (zrodlo: NASA; licencja: public domain)
- Ryc. 78: Wskaźnik zużycia wody (WUE): przewaga "zero wody" jest realna wobec średniej branżowej, ale niewielka wobec najlepszej naziemnej kolokacji (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Starcloud/ASCEND, EUDCA 2025, Moduledge)
- Ryc. 79: Strumień aluminium na szczycie atmosfery (TOA) z reentry satelitów - wzrost z 2016 r. do scenariusza megakonstelacji (nadwyżka 646% nad źródłami naturalnymi) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Ferreira et al., GRL 2024)
- Ryc. 80: Intensywność emisji amerykańskich centrów danych o wysokiej gęstości (HDC) wobec sieci - benchmark, który orbital ma rzekomo pobić, choć jego rzeczywista carbon intensity pozostaje nieujawniona (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Guidi et al. (Harvard / arXiv))
- Ryc. 81: Skala precedensu Viasat KA-SAT: do 45 tys. zbrickowanych modemów, ponad 100 tys. klientów dotkniętych, 5800 turbin wiatrowych bez monitoringu i ponad 100 tys. żądań DDoS w 5 minut - bez fizycznego dotknięcia satelity (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: The Record, reference-global/BSAFT 2025, CyberScoop (notatka))
- Ryc. 82: Bezpieczenstwo: KSC-2009-1936 (zrodlo: NASA; licencja: public domain)
- Ryc. 83: Bezpieczenstwo: KSC-05pd-0386 (zrodlo: NASA; licencja: public domain)
- Ryc. 84: Obecny koszt Falcon 9 (reusable) 3600 USD/kg wobec progu opłacalności 200 USD/kg; przy 10x reuse ok. 60 USD/kg, przy 100x reuse ok. 15 USD/kg. Dopóki launch nie spadnie do ok. 200 USD/kg, orbita jest droższa od Ziemi (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: arXiv 2511.19468 / Google Project Suncatcher (notatka))
- Ryc. 85: Niezależny analityk Luminix daje orbitalnym DC poniżej 15% szans na opłacalność do 2029-2031 i 30-40% (górna granica 40%) do 2032-2035 (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: Luminix - data centers in space (notatka))
- Ryc. 86: Umieszczenie 1 GW mocy obliczeniowej w kosmosie szacowane na 51 mld USD wobec 16 mld USD na Ziemi (ok. 3,2x drożej) (zrodlo: wlasne opracowanie (Mermaid); licencja: wlasne opracowanie; dane: china-in-space (notatka))


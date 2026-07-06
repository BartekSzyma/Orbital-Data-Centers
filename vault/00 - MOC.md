# Orbitalne / kosmiczne centra danych

> Pogłębiony raport tematyczny (wiki Obsidian). Punktem wyjścia był polski artykuł sceptyczny "Centra przetwarzania danych na orbicie nie mają sensu", którego tezy raport krytycznie weryfikuje.

## O raporcie

Każda liczba niesie źródło i poziom wiarygodności: 🔵 pierwotne, 🟠 wtórne, 🔴 słabe. Pojęcia techniczne mają dymki (najedź kursorem) i słowniczki; dane zilustrowano własnymi wykresami z twardych liczb oraz figurami z paperów i materiałów graczy.

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

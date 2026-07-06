---
tytul: Wprowadzenie, definicje i architektury
sekcja_idx: 0
source_tier: primary
tematy: ["wprowadzenie-definicje-i-architektury"]
data_utworzenia: "2026-06-16"
---

# Wprowadzenie, definicje i architektury

> Notatka raportu "Orbitalne centra danych". Kluczowe źródła: [źródło 1](https://researchintelo.com/report/orbital-space-based-data-center-and-ai-compute-market), [źródło 2](https://www.adlittle.com/en/insights/viewpoints/data-centers-go-orbital).

## W skrócie

Orbitalne (kosmiczne) centrum danych to po prostu sprzęt obliczeniowy - procesory, pamięć, dyski - umieszczony na satelicie lub grupie połączonych satelitów krążących nad Ziemią, zwykle na niskiej orbicie (<abbr title="obszar orbity do około 2000 km wysokości, gdzie zwykle umieszcza się te satelity.">LEO</abbr>, 400-2000 km), zamiast w hali na powierzchni planety. Inwestor powinien rozumieć, że to dziś przede wszystkim wyścig o tanią energię słoneczną i o omijanie wieloletnich kolejek na przyłącze prądu: naziemne centrum danych w USA potrzebuje około 7 lat od pomysłu do uruchomienia, a kolejki na podłączenie do sieci sięgają 3-5 lat. Po stronie przychodów stawka jest ogromna - globalne zużycie prądu przez centra danych ma się podwoić z 415 <abbr title="jednostka ilości zużytej energii; miara rocznego poboru prądu przez centra danych.">TWh</abbr> (2024) do około 945 TWh (2030) według Międzynarodowej Agencji Energii. Kluczowe ryzyko: prawie wszystko jest dziś demonstratorem (Starcloud-1 to jeden satelita z jednym GPU), a opłacalność zależy w całości od drastycznego spadku kosztów startu rakiet, których operatorzy w większości nie kontrolują. Wygrywają na razie sprzedawcy "kilofów i łopat" (producenci platform satelitarnych jak K2 Space, dostawcy laserów), a największym przegranym mogą być inwestorzy kupujący wizję gigawatowych chmur "do 2028 roku", które eksperci nazywają science fiction.

<!-- network:watki:start -->
## Powiązane wątki

> Mapa powiązań tematycznych - jak ten wątek łączy się z resztą raportu.

- [[03 - fizyka-orbitalna-orbity-i-operacje|Fizyka orbitalna]] - architektury free-flyer i konstelacji wynikają z wyboru orbity i operacji
- [[04 - energetyka-kosmiczna-i-fotowoltaika-orbitalna|Energetyka kosmiczna]] - głównym motorem napędowym jest tania, ciągła energia słoneczna
- [[09 - ekonomika-i-koszty-calkowite-tco|Ekonomika i TCO]] - czy wizja gigawatowych chmur jest opłacalna rozstrzyga rachunek TCO
- [[10 - gracze-i-projekty|Gracze i projekty]] - kto realnie buduje opisane tu architektury (SpaceX, Google, Starcloud)
- [[12 - naziemny-bottleneck-energetyczny-i-sieciowy|Naziemny bottleneck]] - motywacja popytowa: niedobór mocy i kolejki przyłączeniowe na Ziemi
<!-- network:watki:end -->
## Czym jest orbitalne centrum danych i jak je klasyfikować

Najprostsza definicja brzmi: orbitalne centrum danych (ang. orbital / space-based data center, <abbr title="sprzęt obliczeniowy (procesory, pamięć, dyski) umieszczony na satelicie lub grupie satelitów krążących nad Ziemią, zamiast w naziemnej hali.">ODC</abbr>) to obiekt obliczeniowy umieszczony na niskiej orbicie okołoziemskiej (LEO - Low Earth Orbit, czyli orbita do około 2000 km wysokości), na pokładzie satelity lub klastra połączonych satelitów, zaprojektowany do wykonywania zadań AI: wnioskowania (inference - uruchamianie gotowych modeli), trenowania modeli (training) lub analityki danych w kosmosie. Tak definiuje go firma analityczna ResearchIntelo, podając typowy zakres wysokości 400-2000 km ([źródło](https://researchintelo.com/report/orbital-space-based-data-center-and-ai-compute-market)). Firma doradcza Arthur D. Little zawęża ten zakres do 400-1400 km i podkreśla, że chodzi o "sprzęt obliczeniowy (procesory, pamięć, dyski) ulokowany na pokładzie tych satelitów" ([źródło](https://www.adlittle.com/en/insights/viewpoints/data-centers-go-orbital)). Dla inwestora termin "data center" jest tu więc rozciągliwy - od pojedynczego procesora po wyobrażenie miliona satelitów.

Taksonomia (czyli klasyfikacja zastosowań) ma znaczenie, bo decyduje o tym, które obietnice są już realne, a które odległe. Arthur D. Little wyróżnia trzy wczesne kategorie zastosowań: (1) edge compute na orbicie - przetwarzanie danych tam, gdzie powstają, czyli przy obserwacji Ziemi (EO, Earth Observation); (2) odporne i suwerenne przechowywanie danych (storage/backup); (3) tolerujące opóźnienia przetwarzanie wsadowe (batch compute), gdzie nie liczy się szybka odpowiedź ([źródło](https://www.adlittle.com/en/insights/viewpoints/data-centers-go-orbital)). Implikacja inwestorska: storage i edge są najbliżej komercjalizacji, bo są "lekkie energetycznie", a trening modeli frontier (największych, najnowszych) jest najdroższy energetycznie i najdalszy.

Dlaczego storage jest łatwiejszy? Według eksperta cytowanego przez Satellite Today przechowywanie danych "pobiera bardzo mało mocy - mniej niż 15 procent mocy typowego centrum danych", a dane mogą być rozproszone na wielu satelitach dla odporności ([źródło](https://www.satellitetoday.com/technology/2026/06/02/are-orbital-data-centers-the-next-frontier-of-ai-infrastructure/)). Dla porównania, trening modeli frontier pochłania 30-80 MW (megawatów - milionów watów) ciągłej mocy przez 30-90 dni ([źródło](https://researchintelo.com/report/orbital-space-based-data-center-and-ai-compute-market)). Różnica rzędu wielkości tłumaczy, czemu pierwsze realne wdrożenia to backup i obserwacja Ziemi, a nie chmura AI.

Argument za przetwarzaniem przy źródle danych: globalny strumień surowych zdjęć satelitarnych przekroczył w 2025 roku 2,8 <abbr title="jednostka ilości danych równa miliardowi gigabajtów.">EB</abbr>/dzień (eksabajta na dobę; eksabajt to miliard gigabajtów) ([źródło](https://researchintelo.com/report/orbital-space-based-data-center-and-ai-compute-market)). Przetwarzanie tych danych na orbicie zamiast ściągania ich na Ziemię oszczędza pasmo. Co do opóźnień - klaster na LEO na 600 km może obsłużyć użytkowników naziemnych w swoim zasięgu z opóźnieniem <abbr title="czas, w jakim sygnał dociera do celu i wraca, czyli miara opóźnienia łącza (w milisekundach).">RTT</abbr> (round-trip time, czas tam i z powrotem) około 8-15 ms (milisekund) ([źródło](https://researchintelo.com/report/orbital-space-based-data-center-and-ai-compute-market)). To pokazuje, że niektóre zastosowania są fizycznie wykonalne; pytanie brzmi - po jakim koszcie.

Fizyczna przewaga kosmosu, która przewija się przez całą dziedzinę: według white papera firmy Starcloud "głęboka przestrzeń jest zimna - efektywna temperatura otoczenia to około -270°C, odpowiadająca temperaturze mikrofalowego promieniowania tła" ([źródło](https://starcloudinc.github.io/wp.pdf)). To teoretycznie darmowa chłodnica, choć - jak pokaże sekcja o kontrowersjach - w praktyce wymaga ciężkich radiatorów.

## Warianty architektury

### Free-flyer LEO i konstelacje węzłów obliczeniowych

Dominujący pomysł to "free-flyer" - swobodnie latający satelita lub cała konstelacja (sieć wielu satelitów) pełniących rolę węzłów obliczeniowych. Skala deklarowanych wniosków jest skrajnie rozbieżna. 30 stycznia 2026 SpaceX złożył do amerykańskiego regulatora FCC wniosek o autoryzację systemu "do jednego miliona satelitów" pod nazwą "SpaceX Orbital Data Center system" ([źródło](https://docs.fcc.gov/public/attachments/DA-26-113A1.pdf)). System ma działać na wysokościach 500-2000 km, w inklinacjach 30 stopni oraz heliosynchronicznej (<abbr title="orbita, na której satelita przelatuje nad danym punktem Ziemi zawsze o tej samej porze słonecznej.">SSO</abbr> - orbita, na której satelita przelatuje nad danym punktem zawsze o tej samej porze słonecznej) ([źródło](https://docs.fcc.gov/public/attachments/DA-26-113A1.pdf)). Implikacja: milion satelitów to liczba bezprecedensowa - dla porównania kontekst skali pojawi się w sekcji o kontrowersjach.

Inni gracze składają własne, również gigantyczne wnioski. Starcloud złożył do FCC wniosek na konstelację 88 000 satelitów (3 lutego 2026, dzień po SpaceX) ([źródło](https://siliconvalleyinvestclub.com/starcloud/)). Blue Origin (firma Jeffa Bezosa) wnioskuje o "do 51 600 satelitów-centrów danych" w projekcie nazwanym Project Sunrise, działającym na orbitach kołowych SSO od 500 do 1800 km ([źródło](https://www.geekwire.com/2026/blue-origin-data-center-space-race-project-sunrise/)). Implikacja inwestorska: liczby we wnioskach regulacyjnych to deklaracje maksymalnych pułapów, nie zobowiązania - traktuj je jako "rezerwacje miejsca", nie jako biznesplan.

```mermaid
xychart-beta
    title "Konstelacje ODC - wnioski (liczba sat.)"
    x-axis ["SpaceX", "Starcloud", "Blue Origin", "Chiny 3BCC", "Google Suncatcher"]
    y-axis "liczba satelitow" 0 --> 1000000
    bar [1000000.0, 88000.0, 51600.0, 2800.0, 81.0]
```
*Rys. 1 - skala deklarowanych konstelacji ODC wg graczy: wnioski FCC i projekty (SpaceX milion, Starcloud 88 tys., Blue Origin Project Sunrise 51,6 tys., chiński Three-Body 2800, klaster Google Suncatcher 81). Dane: FCC DA-26-113A1, siliconvalleyinvestclub (Starcloud), GeekWire (Blue Origin), dig.watch (Chiny), arXiv 2511.19468 (Google).*

Najbardziej dopracowaną technicznie architekturę free-flyer pokazał Google w projekcie Suncatcher. W publikacji naukowej (preprint arXiv autorstwa Google Research) opisano klaster 81 satelitów o promieniu 1 km na średniej wysokości 650 km, lecących w formacji ([źródło](https://arxiv.org/html/2511.19468v1)). Aby taki klaster działał jak jedno centrum danych, każde łącze międzysatelitarne potrzebuje przepustowości rzędu 10 Tbps (terabitów na sekundę), co Google uznaje za osiągalne komercyjnymi komponentami <abbr title="technika gęstego zwielokrotnienia falowego, upychająca wiele kanałów świetlnych w jedno łącze optyczne dla większej przepustowości.">DWDM</abbr> (technika gęstego zwielokrotnienia falowego, pozwalająca wepchnąć wiele kanałów w jedno łącze optyczne) ([źródło](https://arxiv.org/html/2511.19468v1)). Demonstrator laboratoryjny osiągnął 800 Gbps w jedną stronę, czyli 1,6 Tbps dwukierunkowo, na krótkim odcinku w wolnej przestrzeni ([źródło](https://arxiv.org/html/2511.19468v1)). Implikacja: łączenie satelitów w "jeden komputer" jest sercem problemu - i wymaga przepustowości jeszcze 6 razy wyższej niż osiągnięto w labie.

Chiny realizują podejście konstelacyjne najszybciej w praktyce. W maju 2025 Zhejiang Lab wystrzelił 12 satelitów LEO jako pierwszą fazę "Three-Body Computing Constellation", docelowo planowanej na około 2800 satelitów o łącznej mocy obliczeniowej 1000 peta operacji na sekundę ([źródło](https://dig.watch/updates/china-moves-toward-data-centres-in-orbit)).

### Moduł przy komercyjnej stacji - Axiom Space (POTWIERDZONE)

Alternatywą dla free-flyerów jest doczepienie centrum danych do załogowanej stacji kosmicznej. Robi to Axiom Space - i wbrew oznaczeniu "do potwierdzenia" w briefie, źródła pierwotne to potwierdzają. Axiom oficjalnie ogłosił, że pracuje nad ODC od 2022 roku, od wyniesienia urządzenia AWS Snowcone (przenośna jednostka obliczeniowa Amazona) na Międzynarodową Stację Kosmiczną ISS ([źródło](https://www.axiomspace.com/release/axiom-space-to-launch-orbital-data-center-nodes-to-support-national-security-commercial-international-customers)). Firma zapowiedziała wyniesienie pierwszych dwóch węzłów ODC (free-flyer) na LEO do końca 2025 roku, z optycznymi łączami o przepustowości 2,5 Gbps do satelitów przekaźnikowych Kepler Communications ([źródło](https://www.axiomspace.com/release/axiom-space-to-launch-orbital-data-center-nodes-to-support-national-security-commercial-international-customers)). Docelowo, do 2027 roku, Axiom planuje pełną szafę serwerową o rozmiarze około pół metra sześciennego (0,5 m³) na swojej stacji Axiom Station, z łączami optycznymi <abbr title="laserowe połączenie między satelitami pozwalające im wymieniać dane bez pośrednictwa Ziemi.">OISL</abbr> do 10 Gbps spełniającymi standardy interoperacyjności agencji SDA ([źródło](https://www.axiomspace.com/release/orbital-data-center)). Implikacja: Axiom to przykład realnej, etapowej, mniejszej skali - od jednego urządzenia AWS po pół metra sześciennego sprzętu, daleko od miliona satelitów.

![[assets/x00-1-c6f8b80a-5a7b-427d-a2c7-0c0bc2806a.png]]
*Rys. 2 - Architektura Axiom Space Orbital Data Center (modul przy stacji komercyjnej). Źródło: Axiom Space / ITHome, licencja: materialy prasowe - do uzytku wlasnego.*
#grafika #wprowadzenie-definicje-i-architektury #architektura #Axiom #ODC

### Inne architektury - storage księżycowy i cislunarny

Osobna gałąź to przechowywanie danych daleko od Ziemi. Lonestar Data Holdings podpisał z firmą Sidus Space umowę wartości 120 mln USD na sześć statków przeznaczonych do księżycowego przechowywania danych ([źródło](https://sidusspace.com/2025/04/02/sidus-space-signs-extended-and-amended-preliminary-120m-agreement-with-lonestar-for-lunar-data-storage-spacecraft/)). Kolejnym krokiem ma być seria wielopetabajtowych pamięci operujących z punktu libracyjnego L1 układu Ziemia-Księżyc, z pierwszym startem w 2027 roku ([źródło](https://www.factoriesinspace.com/lonestar)). <abbr title="stabilny grawitacyjnie punkt między Ziemią a Księżycem (około 300 000 km od Ziemi), rozważany pod dalekie archiwa danych.">Punkt L1</abbr> znajduje się około 300 000 km od Ziemi ([źródło](https://www.datacenterdynamics.com/en/news/sidus-space-advances-120m-agreement-with-lonestar-brings-in-atomic-6/)). Implikacja: to nisza "archiwum poza zasięgiem katastrof", a nie chmura AI - inny profil ryzyka i przychodu.

## Motywacja popytowa - boom na moc obliczeniową AI

Cała dziedzina opiera się na założeniu, że popyt na moc obliczeniową rośnie szybciej, niż Ziemia jest w stanie dostarczyć prąd. Według Międzynarodowej Agencji Energii (IEA) centra danych zużyły w 2024 roku około 415 TWh (terawatogodzin) energii, czyli około 1,5% światowego zużycia prądu ([źródło](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)). W scenariuszu bazowym IEA prognozuje podwojenie tej liczby do około 945 TWh do 2030 roku, przy wzroście około 15% rocznie - ponad cztery razy szybciej niż cała reszta zapotrzebowania na prąd ([źródło](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)). Samo zużycie serwerów akcelerowanych (czyli napędzanych głównie przez AI) ma rosnąć około 30% rocznie ([źródło](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)). Implikacja inwestorska: to jest twardy, niezależny od entuzjastów kosmosu dowód na realny niedobór mocy - paliwo dla całej narracji ODC.

```mermaid
xychart-beta
    title "Globalne zuzycie pradu centrow danych"
    x-axis ["2024", "2030 (prognoza)"]
    y-axis "TWh/rok" 0 --> 1000
    bar [415.0, 945.0]
```
*Rys. 3 - podwojenie globalnego zużycia prądu przez centra danych w scenariuszu bazowym IEA (415 TWh w 2024 do ok. 945 TWh w 2030). Dane: IEA - Energy and AI.*

Rynek amerykański pokazuje to jeszcze ostrzej. BloombergNEF prognozuje, że zapotrzebowanie centrów danych na moc w USA ponad się podwoi - z prawie 35 GW (gigawatów) w 2024 do 78 GW w 2035 ([źródło](https://about.bnef.com/insights/commodities/power-for-ai-easier-said-than-built/)). Udział centrów danych w całym popycie na prąd w USA ma wzrosnąć z 3,5% dziś do 8,6% w 2035 ([źródło](https://about.bnef.com/insights/commodities/power-for-ai-easier-said-than-built/)).

```mermaid
xychart-beta
    title "Popyt centrow danych na moc w USA"
    x-axis ["2024", "2035 (prognoza)"]
    y-axis "GW" 0 --> 80
    bar [35.0, 78.0]
```
*Rys. 4 - ponad dwukrotny wzrost zapotrzebowania centrów danych na moc w USA (z prawie 35 GW w 2024 do 78 GW w 2035). Dane: BloombergNEF - Power for AI.*

## Motywacja energetyczna i administracyjna

### Tania, ciągła energia słoneczna

To najmocniejszy argument zwolenników. Starcloud twierdzi, że "capacity factor" (czyli udział czasu, w którym panel realnie produkuje pełną moc) jego kosmicznej matrycy solarnej przekracza 95%, bez cyklu dzień/noc, z idealną orientacją paneli i bez wpływu pogody czy pór roku ([źródło](https://starcloudinc.github.io/wp.pdf)). Szczytowa generacja ma być około 40% wyższa niż na Ziemi, bo atmosfera osłabia i rozprasza promieniowanie nawet w pogodny dzień ([źródło](https://starcloudinc.github.io/wp.pdf)). W sumie ten sam panel ma w kosmosie wytworzyć ponad 5 razy więcej energii niż na Ziemi ([źródło](https://starcloudinc.github.io/wp.pdf)). Google podaje ostrożniejszą, ale zbieżną liczbę: w odpowiednich orbitach panel otrzymuje do 8 razy więcej energii słonecznej rocznie niż na Ziemi w średnich szerokościach geograficznych ([źródło](https://arxiv.org/html/2511.19468v1)). Fizyczne tło: irradiancja słoneczna w kosmosie to 1361 W/m², wobec efektywnych 150-300 W/m² na Ziemi ([źródło](https://introl.com/blog/orbital-data-centers-space-computing-race-2026)).

Z tych przewag Starcloud wyprowadza spektakularne deklaracje kosztowe. Firma twierdzi, że docelowo zaoferuje "równoważny koszt energii około 0,002 USD/kWh", czyli energię 22 razy tańszą niż dzisiejsze ceny ([źródło](https://starcloudinc.github.io/wp.pdf)). Bardziej powściągliwa, wtórna liczba mówi o 0,05 USD/kWh dla satelity Starcloud-3 ([źródło](https://tech-insider.org/starcloud-170-million-series-a-space-data-center-2026/)). Implikacja: rozrzut od 0,002 do 0,05 USD/kWh (25-krotny) sam w sobie pokazuje, jak niepewne są te projekcje - inwestor powinien traktować dolny koniec jako marketing.

### Chłodzenie bez wody

Studium ASCEND (Thales Alenia Space) podkreśla, że kosmiczne centra danych "nie wymagałyby wody do chłodzenia - kluczowa przewaga w czasach rosnących susz" ([źródło](https://www.thalesaleniaspace.com/en/press-releases/thales-alenia-space-reveals-results-ascend-feasibility-study-space-data-centers-0)). Na Ziemi chłodzenie potrafi pochłaniać do 40% budżetu energetycznego centrum danych ([źródło](https://researchintelo.com/report/orbital-space-based-data-center-and-ai-compute-market)). Ale chłodzenie w próżni nie jest darmowe - ciepło trzeba wypromieniować radiatorami. Starcloud podaje, że czarna płyta 1x1 m o temperaturze 20°C wypromieniowuje około 838 W do głębokiej przestrzeni (z obu stron) ([źródło](https://starcloudinc.github.io/wp.pdf)). W praktyce masa radiatora potrzebnego do oddania ciepła z około 10 MW obliczeń na orbicie szacowana jest na około 529 ton ([źródło](https://www.insiderfinance.io/news/google-spacex-orbital-data-centers-talks)). Implikacja: "darmowa zimna kosmiczna chłodnica" w realu oznacza setki ton sprzętu do wyniesienia - koszt, który wraca w rachunku startowym.

### Omijanie przyłączy, pozwoleń i protestów

To argument administracyjny, często niedoceniany. Według analizy Introl orbitalne centra danych "nie wymagają przyłącza do sieci elektrycznej, pozwoleń na użytkowanie gruntu pod kampusy serwerów, praw do wody na chłodzenie ani wieloletnich umów przyłączeniowych z dostawcami prądu" ([źródło](https://introl.com/blog/orbital-data-centers-space-computing-race-2026)). Starcloud podkreśla, że w krajach zachodnich nowe wielkoskalowe projekty energetyczne "często zajmują dekadę lub więcej" z powodu wymogów pozwoleniowych, praw drogi i ocen środowiskowych ([źródło](https://starcloudinc.github.io/wp.pdf)). Orbitalne DC mają te przeszkody niemal w całości omijać, co - według firmy - przynosi istotne oszczędności ([źródło](https://starcloudinc.github.io/wp.pdf)). To łączy się z naziemnymi wąskimi gardłami: Starcloud wskazuje, że pozwolenia i budowa nowych centrów danych oraz projektów energetycznych na Ziemi mogą trwać do 5 lat ([źródło](https://www.businesswire.com/news/home/20260330024111/en/)); BNEF szacuje typowy czas rozwoju DC w USA na około 7 lat (4,8 roku przed budową, 2,4 roku budowy) ([źródło](https://about.bnef.com/insights/commodities/power-for-ai-easier-said-than-built/)); kolejki na przyłącze sięgają 3-5 lat na kluczowych rynkach jak Północna Wirginia, Dublin i Singapur ([źródło](https://researchintelo.com/report/orbital-space-based-data-center-and-ai-compute-market)). Implikacja: gdyby tempo wdrożenia w kosmosie biło te 5-7 lat, byłoby to realne źródło przewagi konkurencyjnej, niezależne od kosztu energii.

## Analogia do Starlink jako "kolejny krok"

Narracja "po terminalach komunikacyjnych przychodzi czas na komputery na orbicie" opiera się na sukcesie Starlink. SpaceX ma już ponad 10 000 satelitów w konstelacji Starlink, wyniesionych od 2019 roku ([źródło](https://www.geekwire.com/2026/blue-origin-data-center-space-race-project-sunrise/)). W styczniu 2026 aktywnych było około 9500 z 14 500 wszystkich satelitów na orbicie ([źródło](https://repo.enc.edu/2026/02/03/why-did-spacex-just-ask-to-launch-1-million-satellites/)). Sam 2025 rok przyniósł 3000 satelitów V2 Mini Optimized, dodających ponad 270 Tbps pojemności ([źródło](https://orbitaltoday.com/2026/01/03/starlink-progress-2025-report-part-ii-satellites/)). Kluczowy łącznik z ODC to sieć optyczna: każdy V2 Mini ma trzy lasery, a cała sieć ponad 24 000 laserów ([źródło](https://orbitaltoday.com/2026/01/03/starlink-progress-2025-report-part-ii-satellites/)); każdy laser nadaje z prędkością do 200 Gbps ([źródło](https://www.fierce-network.com/cloud/opinion-spacexs-satellite-data-center-plan-unhinged)). We wniosku FCC SpaceX wprost zapowiada, że łącza optyczne ODC będą kierować ruch "do satelitów w konstelacji Starlink, przez jej wysokoprzepustową (petabitową) i niezawodną siatkę laserową", która przekaże ruch do stacji naziemnych ([źródło](https://docs.fcc.gov/public/attachments/DA-26-113A1.pdf)). Implikacja: dla SpaceX orbitalne DC nie jest projektem od zera, lecz nadbudową nad istniejącym, działającym backbonem - to realna przewaga, ale tylko dla jednego gracza.

## Skala odniesienia - typowe naziemne DC

Brief prosi o benchmark "~200 MW". W źródłach precyzyjna liczba 200 MW jest NIE UJAWNIONA - dostępne są za to liczby okalające ten rząd wielkości. Nowy obiekt hyperscale (najwiekszej klasy) potrzebuje co najmniej 50-100 MW ([źródło](https://cc-techgroup.com/how-much-power-does-a-hyperscale-data-center-use/)). Pojedynczy duży obiekt hyperscale zużywa około 100 MW - tyle, co setki tysięcy domów ([źródło](https://cc-techgroup.com/how-much-power-does-a-hyperscale-data-center-use/)). Inne źródło podaje ciągle 20-100+ MW, a największe obiekty ponad 650 MW ([źródło](https://iaeimagazine.org/electrical-fundamentals/how-much-electricity-does-a-data-center-use-complete-2025-analysis/)). Starcloud przyjmuje za punkt odniesienia 100 MW dla dużego DC dziś, z planami zbliżenia się do 1 GW ([źródło](https://starcloudinc.github.io/wp.pdf)), i wskazuje, że klaster potrzebny do treningu modeli pokroju Llama 5 lub GPT-6 to aż 5 GW ([źródło](https://starcloudinc.github.io/wp.pdf)). Studium ASCEND szacuje rynek mocy DC na 23 GW do 2030 i celuje w 1 GW na orbicie przed 2050 rokiem ([źródło](https://www.thalesaleniaspace.com/en/press-releases/thales-alenia-space-reveals-results-ascend-feasibility-study-space-data-centers-0)). Implikacja: dzisiejsze orbitalne demonstratory działają na poziomie kilowatów - od pojedynczych setek megawatów naziemnego DC dzieli je pięć rzędów wielkości.

![[assets/x00-2-station-data-center-v2-1036-light.jpg]]
*Rys. 5 - Koncepcja modularnego orbitalnego DC Thales Alenia Space ASCEND. Źródło: Thales Alenia Space / Satellite Today, licencja: materialy prasowe - do uzytku wlasnego.*
#grafika #wprowadzenie-definicje-i-architektury #architektura #ASCEND

## Kontrowersje

**1. Czy to prawdziwe data center, czy demonstrator, storage, edge lub etykieta marketingowa?**

To najważniejszy spór dziedziny, bo decyduje, czy inwestor kupuje produkt, czy obietnicę.

**Strona "to jeszcze nie są prawdziwe DC":** Starcloud-1 to pojedynczy satelita z jednym GPU Nvidia H100, a nie klaster centrum danych ([źródło](https://siliconcanals.com/sc-w-one-satellite-one-gpu-1-1-billion-valuation-the-reality-behind-starclouds-orbital-data-center-ambitions/)). Ta sama analiza podaje, że łączna moc największej sieci satelitarnej w historii to mniej niż 1% pojemności centrów danych obecnie budowanych na Ziemi ([źródło](https://siliconcanals.com/sc-w-one-satellite-one-gpu-1-1-billion-valuation-the-reality-behind-starclouds-orbital-data-center-ambitions/)). Blog Per Aspera: dzisiejsze demonstratory działają w skali kilowatów i kilku teraflopów - "efektywnie równowartość szafy lub dwóch serwerów na Ziemi, a nie całego centrum danych" ([źródło](https://peraspera.us/realities-of-space-based-compute/)). Według tego samego źródła "ktokolwiek macha biznesplanem stumegawatowej chmury LEO do 2028 roku wciąż uprawia science fiction" ([źródło](https://peraspera.us/realities-of-space-based-compute/)). Dokłada problemy fizyczne: na LEO każde 90-minutowe okrążenie zawiera 25-35% czasu zaćmienia (brak słońca) ([źródło](https://peraspera.us/realities-of-space-based-compute/)); sam osprzęt zasilania dla systemu 100 kW waży około 1,4 tony, bez kabli i elektroniki sterującej ([źródło](https://peraspera.us/realities-of-space-based-compute/)); 140 kW wymaga około 700 m² paneli ([źródło](https://peraspera.us/realities-of-space-based-compute/)).

**Strona "to pierwszy krok ku prawdziwym DC":** Starcloud-1 dostarczył pierwszy H100 na orbicie, ze 100-krotnym wzrostem mocy obliczeniowej AI względem wcześniejszych GPU w kosmosie ([źródło](https://www.businesswire.com/news/home/20260330024111/en/)). Starcloud-2 ma mieć największy komercyjny rozkładany radiator w historii i 100-krotnie większą generację mocy niż Starcloud-1 ([źródło](https://www.businesswire.com/news/home/20260330024111/en/)). Starcloud-3 ma osiągnąć 200 kW przy masie 3 ton ([źródło](https://tech-insider.org/starcloud-170-million-series-a-space-data-center-2026/)). K2 Space deklaruje 100 kW mocy na satelitę na platformie Giga, "umożliwiając misje, które wcześniej istniały tylko w science fiction: obliczenia w skali AI na orbicie" ([źródło](https://www.prnewswire.com/news-releases/k2-space-raises-250m-at-3b-valuation-to-roll-out-a-new-class-of-high-capability-satellites-302638936.html)). Starcloud argumentuje, że przy gęstości 120 kW na szafę jeden start Starship może wynieść około 40 MW obliczeń, a 5 GW dałyby się wynieść mniej niż 100 startami ([źródło](https://starcloudinc.github.io/wp.pdf)). ASCEND celuje w 1 GW na orbicie przed 2050 ([źródło](https://www.thalesaleniaspace.com/en/press-releases/thales-alenia-space-reveals-results-ascend-feasibility-study-space-data-centers-0)). Wniosek: obie strony zgadzają się co do faktów dzisiejszej skali (kilowaty, jeden GPU); różnią się interpretacją tempa - sceptycy mówią o science fiction do 2028, optymiści o uzasadnionej trajektorii do 2050.

**2. Czy orbitalne DC to logiczne następstwo Starlink, czy osobna kategoria?**

**Strona "logiczne następstwo":** ODC SpaceX ma jawnie korzystać z petabitowej siatki laserowej Starlink jako backbone ([źródło](https://docs.fcc.gov/public/attachments/DA-26-113A1.pdf)). Istniejące ponad 9500 aktywnych satelitów Starlink tworzy gotowy szkielet ([źródło](https://repo.enc.edu/2026/02/03/why-did-spacex-just-ask-to-launch-1-million-satellites/)), z infrastrukturą 3 laserów na satelitę i ponad 24 000 laserów w sieci ([źródło](https://orbitaltoday.com/2026/01/03/starlink-progress-2025-report-part-ii-satellites/)).

**Strona "osobna kategoria" (komunikacja to nie obliczenia):** Skala jest innego rzędu: ODC to wniosek na 1 milion satelitów wobec pierwotnego wniosku Starlink na 42 000 z 2019 roku ([źródło](https://repo.enc.edu/2026/02/03/why-did-spacex-just-ask-to-launch-1-million-satellites/)). Moc satelity ODC liczy się w setkach kW (np. 100 kW), wobec mniej niż 1 kW dla satelity komunikacyjnego - inne wymagania zasilania i chłodzenia ([źródło](https://www.spacewar.com/reports/Orbital_Data_Centers_The_175_Trillion_Bridge_To_Nowhere_999.html)). Wykonalność wdrożenia jest pod znakiem zapytania: w 2025 wyniesiono na świecie 4526 satelitów; w tym tempie milion satelitów zająłby ponad 220 lat ([źródło](https://www.yahoo.com/news/articles/amazon-urges-fcc-deny-spacex-001720630.html)). Przy 5-letnim życiu satelity utrzymanie konstelacji 1 mln wymagałoby wymiany 200 000 satelitów rocznie - ponad 44-krotność całej światowej produkcji startów z 2025 ([źródło](https://www.yahoo.com/news/articles/amazon-urges-fcc-deny-spacex-001720630.html)). Wniosek: technicznie ODC dziedziczy backbone Starlink (następstwo), ale energetycznie, kosztowo i logistycznie jest kategorią osobną, o skali fizycznie niewykonalnej obecnymi środkami.

```mermaid
xychart-beta
    title "Moc na satelite - ODC vs komunikacja (kW)"
    x-axis ["Sat. komunikacyjny", "K2 Giga", "Starcloud-3"]
    y-axis "kW na satelite" 0 --> 200
    bar [1.0, 100.0, 200.0]
```
*Rys. 6 - przepaść mocy między satelitą komunikacyjnym (poniżej 1 kW) a satelitami ODC (platforma K2 Giga 100 kW, Starcloud-3 200 kW). Dane: spacewar.com (sat. komunikacyjny), PR Newswire (K2 Space Giga), tech-insider (Starcloud-3).*

## Słowniczek pojęć

- **ODC (orbitalne centrum danych)** - sprzęt obliczeniowy (procesory, pamięć, dyski) umieszczony na satelicie lub grupie satelitów krążących nad Ziemią, zamiast w naziemnej hali.
- **LEO (Low Earth Orbit, niska orbita okołoziemska)** - obszar orbity do około 2000 km wysokości, gdzie zwykle umieszcza się te satelity.
- **SSO (orbita heliosynchroniczna)** - orbita, na której satelita przelatuje nad danym punktem Ziemi zawsze o tej samej porze słonecznej.
- **Punkt L1 (punkt libracyjny)** - stabilny grawitacyjnie punkt między Ziemią a Księżycem (około 300 000 km od Ziemi), rozważany pod dalekie archiwa danych.
- **Konstelacja** - sieć wielu współpracujących ze sobą satelitów działających jak jeden system.
- **Free-flyer** - swobodnie latający, samodzielny satelita pełniący rolę węzła obliczeniowego (w odróżnieniu od modułu doczepionego do stacji).
- **Edge compute (przetwarzanie przy źródle)** - analiza danych tam, gdzie powstają (np. zdjęć satelitarnych), zamiast przesyłania surowych danych na Ziemię.
- **Inference / training (wnioskowanie / trenowanie)** - dwa tryby pracy AI: uruchamianie gotowego modelu (tańsze) oraz uczenie nowego modelu (znacznie droższe energetycznie).
- **Downlink / stacja naziemna** - łącze i naziemny punkt odbioru, przez który dane z orbity trafiają na Ziemię.
- **OISL (optyczne łącze międzysatelitarne)** - laserowe połączenie między satelitami pozwalające im wymieniać dane bez pośrednictwa Ziemi.
- **DWDM** - technika gęstego zwielokrotnienia falowego, upychająca wiele kanałów świetlnych w jedno łącze optyczne dla większej przepustowości.
- **RTT (round-trip time)** - czas, w jakim sygnał dociera do celu i wraca, czyli miara opóźnienia łącza (w milisekundach).
- **Capacity factor (współczynnik wykorzystania mocy)** - udział czasu, w którym panel lub urządzenie realnie produkuje pełną moc.
- **Irradiancja słoneczna** - moc promieniowania Słońca padająca na metr kwadratowy (w kosmosie 1361 W/m², na Ziemi efektywnie 150-300 W/m²).
- **Radiator** - płyta odprowadzająca ciepło z urządzeń poprzez wypromieniowanie go w przestrzeń (w próżni nie ma chłodzenia powietrzem ani wodą).
- **Hyperscale** - naziemne centrum danych największej klasy, o mocy zwykle od kilkudziesięciu do ponad stu megawatów.
- **MW / GW (megawat / gigawat)** - jednostki mocy; 1 GW to 1000 MW, miara skali zapotrzebowania na prąd.
- **TWh (terawatogodzina)** - jednostka ilości zużytej energii; miara rocznego poboru prądu przez centra danych.
- **Tbps / Gbps** - jednostki przepustowości łącza (terabity i gigabity na sekundę); ile danych przepływa w ciągu sekundy.
- **EB (eksabajt)** - jednostka ilości danych równa miliardowi gigabajtów.

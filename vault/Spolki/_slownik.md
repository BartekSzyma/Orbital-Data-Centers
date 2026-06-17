---
title: "Słownik warstwy spółek"
typ: slownik
---

# Słownik

Centralny słownik warstwy spółek. Każdy nagłówek `## <termin>` jest celem linków `[[_slownik#<termin>|<termin>]]` z notatek spółek - rdzeniowy plugin Page Preview pokazuje definicję po najechaniu kursorem (efekt dymka).

## backlog
Wartość zakontraktowanych, jeszcze niezrealizowanych zamówień. "Backlog zarządczy" bywa szerszy (uwzględnia opcje i umowy ramowe) niż formalne RPO.

## RPO
Remaining Performance Obligations - formalne, wyegzekwowalne zobowiązania z podpisanych umów; węższa i twardsza miara niż backlog zarządczy.

## GAAP
Amerykański standard rachunkowości (US GAAP); "surowe" liczby raportowane do SEC.

## non-GAAP
Miary "po korektach" zarządu (np. z wyłączeniem zdarzeń jednorazowych); zwykle korzystniejsze niż surowy GAAP.

## related party
Podmiot powiązany - kontrahent niebędący w pełni niezależny (np. spółka, w której emitent ma udział); transakcje raportuje się osobno, bo nie są w pełni rynkowe.

## PPA
Power Purchase Agreement - długoterminowa umowa na zakup energii po ustalonej cenie; podstawa finansowania projektów energetycznych dla data center.

## MSA
Master Supply/Services Agreement - umowa ramowa ustalająca warunki i pułap, ale zwykle bez wiążącego zobowiązania do odbioru całego wolumenu; wiążące są dopiero zamówienia (PO).

## MOU
Memorandum of Understanding / list intencyjny (LOI) - niewiążąca deklaracja współpracy; sygnał kierunku, nie twardy przychód.

## capex
Nakłady inwestycyjne (capital expenditures) na środki trwałe; w energetyce często wyrażane jako USD/kW mocy.

## time-to-power
Czas od decyzji o zakupie mocy do jej realnego dostarczenia; kluczowa "waluta" w wyścigu o moc dla AI.

## hyperscaler
Giganci chmury (Microsoft, Google, Amazon, Oracle) budujący własne centra danych w skali setek MW.

## neo-cloud
Wyspecjalizowani operatorzy infrastruktury GPU (np. CoreWeave, Nebius) wynajmujący moc obliczeniową dla AI.

## TCO
Total Cost of Ownership - całkowity koszt posiadania (capex + opex + serwis + wymiana) w całym cyklu życia, nie tylko cena zakupu.

## LEO
Low Earth Orbit - niska orbita okołoziemska (~300-650 km); relatywnie łagodne środowisko radiacyjne i niska latencja.

## GEO
Geostationary Orbit - orbita geostacjonarna (~36 000 km); satelita "wisi" nad jednym punktem, ale dawka radiacyjna i latencja są wysokie.

## SSO
Sun-Synchronous Orbit - orbita heliosynchroniczna; szczególny jej wariant "dawn-dusk" (terminatorowy) daje niemal ciągłe nasłonecznienie.

## ADCS
Attitude Determination and Control System - układ wyznaczania i kontroli położenia satelity (koła reakcyjne, star trackery, magnetorquery).

## koło reakcyjne
Wirujące koło zmieniające orientację satelity dzięki zachowaniu momentu pędu; podstawowy element ADCS.

## star tracker
Czujnik gwiazdowy - kamera rozpoznająca układ gwiazd i precyzyjnie wyznaczająca orientację satelity.

## bus satelitarny
Platforma satelity (zasilanie, sterowanie, łączność, struktura), na której montuje się ładunek użyteczny (payload).

## in-space assembly
Montaż konstrukcji na orbicie z modułów (zamiast wynoszenia gotowego obiektu), omijający ograniczenie średnicy owiewki rakiety (fairing).

## ROSA
Roll-Out Solar Array - rolowana, lekka macierz słoneczna rozwijana na orbicie; wariant iROSA zasila ISS.

## GaAs
Arsenek galu - półprzewodnik kosmicznych ogniw wielozłączowych (multi-junction) o sprawności znacznie wyższej niż krzem naziemny.

## multi-junction
Ogniwo wielozłączowe - kilka warstw półprzewodnika łapiących różne zakresy widma; standard fotowoltaiki kosmicznej (~30%+ sprawności).

## BOL
Begin of Life - sprawność/moc na początku misji; spada do EOL (End of Life) wskutek degradacji radiacyjnej.

## rad-hard
Elektronika utwardzona radiacyjnie na poziomie krzemu - droga i o kilka generacji w tyle, ale odporna na promieniowanie.

## COTS
Commercial Off-The-Shelf - tania, najnowsza elektronika komercyjna "z półki", bez fabrycznej ochrony radiacyjnej.

## TID
Total Ionizing Dose - skumulowana dawka jonizująca powodująca powolne "starzenie" tranzystorów; mierzona w radach/grejach.

## SEE
Single-Event Effects - nagłe efekty uderzenia pojedynczej cząstki: SEU (odwracalny błąd bitu), SEL (zwarcie mogące spalić układ), SET (impuls).

## FPGA
Reprogramowalny układ logiczny; w wersjach rad-tolerant (np. AMD Versal, Microchip RTG4) popularny w kosmosie.

## TMR
Triple Modular Redundancy - potrójne powielenie układu z głosowaniem większościowym; kosztuje ponad 3x powierzchni i mocy.

## ECC
Error-Correcting Code - kod korekcyjny pamięci wykrywający i naprawiający błędy bitowe (np. od SEU).

## OISL
Optical Inter-Satellite Link - optyczne (laserowe) łącze międzysatelitarne; wysoka przepustowość (do setek Gbps) bez zajmowania pasma radiowego.

## downlink
Łącze satelita-Ziemia (przesył danych w dół); wąskie gardło zależne od stacji naziemnych i pogody (optyka) lub pasma (RF).

## heat pipe
Rurka cieplna - pasywny element przenoszący ciepło dzięki parowaniu i skraplaniu czynnika; podstawa termiki satelitów.

## radiator
Powierzchnia oddająca ciepło przez promieniowanie podczerwone; w próżni jedyny sposób odprowadzania ciepła, stąd ogromne pole na 1 MW.

## pętla dwufazowa
Układ chłodzenia, w którym czynnik krąży zmieniając fazę (ciecz-para), przenosząc duże moce cieplne przy małym przepływie.

## liquid cooling
Chłodzenie cieczowe serwerów (np. direct-to-chip, immersja); konieczne przy gęstych obciążeniach AI, których powietrze nie schłodzi.

## MEV
Mission Extension Vehicle - statek dokujący do satelity GEO i przejmujący jego sterowanie/napęd, przedłużając misję o lata.

## life extension
Przedłużanie misji satelity (tankowanie, przejęcie napędu, naprawa) zamiast jego wymiany; rdzeń serwisowania orbitalnego.

## ADR
Active Debris Removal - aktywne usuwanie śmieci kosmicznych (przechwycenie i deorbitacja nieczynnego obiektu).

## station-keeping
Utrzymywanie satelity na zadanej orbicie mimo zaburzeń (drag, ciśnienie słoneczne); zużywa paliwo i budżet delta-V.

## delta-V
Budżet zmiany prędkości dostępny dzięki paliwu; określa, ile manewrów (korekta orbity, unikanie kolizji, deorbitacja) satelita wykona.

## deorbitacja
Sprowadzenie satelity z orbity na koniec życia (EOL), zwykle przez spalenie w atmosferze; reguła FCC wymaga tego w 5 lat.

## SOFC
Solid Oxide Fuel Cell - ogniwo paliwowe ze stałym, ceramicznym elektrolitem tlenkowym; produkuje prąd ciągle z paliwa, nie magazynuje.

## SMR
Small Modular Reactor - mały reaktor modułowy (zwykle 15-300 MW) produkowany seryjnie; rozważany jako baseload dla data center.

## baseload
Moc podstawowa - źródło dostarczające energię ciągle, niezależnie od pory dnia i pogody (jądro, gaz, ogniwa paliwowe).

## CCGT
Combined Cycle Gas Turbine - turbina gazowa z odzyskiem ciepła w obiegu parowym; sprawność ~60%, ale skala elektrowni i długi czas budowy.

## BESS
Battery Energy Storage System - magazyn energii w bateriach; reaguje błyskawicznie, ale tylko oddaje zmagazynowaną energię.

## UPS
Uninterruptible Power Supply - zasilanie bezprzerwowe podtrzymujące pracę przy zaniku sieci do czasu uruchomienia źródła zapasowego.

## precision cooling
Precyzyjne chłodzenie sali serwerowej (kontrola temperatury i wilgotności); rynek, w którym liderem jest Vertiv (marka Liebert).

## grid interconnection
Przyłączenie do sieci elektroenergetycznej; w USA kolejka i budowa trwają 5-10 lat, co jest głównym wąskim gardłem dla mocy DC.

## warrant
Prawo objęcia akcji po ustalonej cenie w przyszłości; dla obejmującego to opcja, dla spółki źródło potencjalnego rozwodnienia.

## de-SPAC
Wejście na giełdę przez fuzję ze spółką-wydmuszką (SPAC) zamiast klasycznego IPO; częste wśród młodych spółek kosmicznych.

## switchgear
Rozdzielnica - aparatura łączeniowa i zabezpieczająca rozdzielająca i chroniąca obwody zasilania; w data center wąskie gardło o długim czasie dostawy.

## SDA
Space Development Agency - agencja Departamentu Obrony USA budująca warstwową konstelację wojskową (Transport/Tracking Layer); duży odbiorca terminali laserowych.

## LCOE
Levelized Cost of Energy - uśredniony koszt wytworzenia 1 MWh w całym cyklu życia źródła; pozwala porównać technologie generacji.

## offtake
Umowa odbioru (offtake) - zobowiązanie nabywcy do kupna ustalonego wolumenu produkcji (energii, mocy), zabezpieczające przychód projektu.

## book-to-bill
Stosunek wartości nowych zamówień do zafakturowanych przychodów w danym okresie; wartość powyżej 1 oznacza, że backlog rośnie szybciej, niż firma fakturuje.

## IBDM
International Berthing and Docking Mechanism - uniwersalny mechanizm dokowania/cumowania statków do stacji; produkt Redwire wykorzystywany m.in. w europejskich i komercyjnych programach orbitalnych.

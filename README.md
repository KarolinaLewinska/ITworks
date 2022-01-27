# ITWorks

## Table of Contents:
1. [Short Description](#1-short-description)
2. [Interfaces](#2-interfaces)
3. [Authors](#3-authors)
4. [Requirements Specifications](#4-requirements-specifications)
5. [UML Diagrams](#5-uml-diagrams)
6. [Software Architecture](#6-software-architecture)
7. [Tests](#7-tests)

### 1. Short Description
- ITworks – search courses and develop your IT skills.<br> 
- Website which allows searching for courses offers in information technology.<br> 

### 2. Interfaces
![](https://github.com/KarolinaLewinska/ITworks/blob/main/ReadmeIMG/ranking.PNG)<br/>
![](https://github.com/KarolinaLewinska/ITworks/blob/main/ReadmeIMG/browser.PNG)<br/>
![](https://github.com/KarolinaLewinska/ITworks/blob/main/ReadmeIMG/results.PNG)<br/>
![](https://github.com/KarolinaLewinska/ITworks/blob/main/ReadmeIMG/error404.PNG)<br/>

### 3. Authors
**Authors:** [Karolina Lewińska](https://github.com/KarolinaLewinska), [Justyna Gapys](https://github.com/justynagapys), [Marcin Wiśniewski](https://github.com/marcinwisniewski98)<br> 

### 4. Requirements Specifications

| ID | Category     | Subcategory                 | Short name              | Description                                                               | Priority |
| -- | ------------- | ---------------------------- | ------------------------- | ------------------------------------------------------------------ | --------- |
| F1 | funkcjonalne | Strona główna | Rankingi | Użytkownik po wejściu na stronę główną widzi rankingi dotyczące liczby dostępnych kursów o najpopularniejszej tematyce oraz odnoszące się do najpopularniejszych języków programowania. | 1 |
| F2 | funkcjonalne | Nawigacja | Przejście do wyszukiwarki | Użytkownik może poprzez kliknięcie przycisku “Wyszukiwarka” w menu nawigacyjnym przejść na podstronę z wyszukiwarką kursów. | 1 |
| F3 | funkcjonalne | Dostosowywanie wyników stron | Wyszukiwanie | Użytkownik po wpisaniu w pole tekstowe interesującej go frazy otrzyma listę wyników z ofertami szkoleń domyślnie posortowanymi alfabetycznie. | 1 |
| F4 | funkcjonalne | Nawigacja | Przekierowanie | Użytkownik po wybraniu interesującego go szkolenia może przejść na stronę danej oferty poprzez kliknięcie w link. | 1 |
| F5 | funkcjonalne | Nawigacja | Przejście do  rankingów | Użytkownik ma możliwość powrotu do strony z rankingami poprzez kliknięcie przycisku “Rankingi” w menu nawigacyjnym. | 1 |
| F6 | funkcjonalne | Dostosowywanie wyników ofert | Brak wyników | Jeśli wpisana w wyszukiwarkę przez użytkownika fraza nie będzie pasować do żadnej z ofert to zostanie mu wyświetlony komunikat “Brak dostępnych kursów o interesującej Cię tematyce”. | 2 |
| F7 | funkcjonalne | Dostosowywanie wyników ofert | Wyszukiwanie po kategorii | Użytkownik może wyszukać szkolenia poprzez wciśnięcie jednego z przycisków kategorii (Java, JavaScript, HTML5, PHP, Python, C++, C#, C, SQL). Po wciśnięciu przycisku wyświetlana jest lista kursów z wybranej kategorii. | 2 |
| F8 | funkcjonalne | Dostosowywanie wyników ofert | Kontakt | Użytkownikowi po wciśnięciu przycisku "Napisz" zostanie wyświetlone okno do napisania wiadomości mailowej, dzięki czemu może skontaktować się z twórcami strony. | 3 |
| F9 | funkcjonalne  | Obsługa błędów | Dedykowane strony błędu | Użytkownik po wpisaniu błędnego/nieistniejącego adresu URL widzi dedykowaną stroną z kodem błędu (500, 404, 400). | 3 |
| F10 | funkcjonalne  | Dostosowywanie wyników ofert | Wyświetlenie liczby dostępnych ofert | Użytkownik po wprowadzeniu interesującej go frazy otrzyma wypisaną liczbę ofert, dla których ta fraza obowiązuje. | 3 |
| NF1 | niefunkcjonalne | Projektowe | Rodzaj aplikacji | Portal jest aplikacją webową. | 1 |
| NF2 | niefunkcjonalne | Projektowe | Używana technologia | W projekcie jest wykorzystywana technologia wolnodostępna. | 1 |
| NF3 | niefunkcjonalne | Projektowe | Obsługiwane przeglądarki | Aplikacja działa w przeglądarkach takich jak Google Chrome, Internet Explorer, Safari, Opera, Mozilla Firefox.| 1 |
| NF4 | niefunkcjonalne | Projektowe | Dostęp do internetu | Aplikacja działa tylko i wyłącznie jeśli użytkownik posiada dostęp do internetu. | 1 |
| NF5 | niefunkcjonalne | Projektowe | Środowisko pracy aplikacji | Aplikacja działa w systemie operacyjnym Windows, macOS, Linux. | 1 |
| NF6 | niefunkcjonalne | Bezpieczeństwo | Testowalność aplikacji | Środowisko testowe powinno być stworzone w taki sposób aby funkcjonalność aplikacji była możliwa do przetestowania. | 1 |
| NF7 | niefunkcjonalne | Bezpieczeństwo | Backup | Aplikacja powinna posiadać kopie zapasowe z systemu kontroli wersji. | 1 |
| NF8 | niefunkcjonalne | UI | Język aplikacji| Strona jest stworzona w języku polskim. | 1 |
| NF9 | niefunkcjonalne | UI | Nawigacja aplikacji | Wszystkie podstrony powinny być łatwe w odnalezieniu przez użytkownika. | 1 |
| NF10 | niefunkcjonalne | UI | Sposób wyświetlania listy oferty | Lista z ofertami kursów powinna być wyświetlona w sposób przejrzysty i zrozumiały dla użytkownika. | 1 |
| NF11 | niefunkcjonalne | UI | Linki przekierowujące do oferty | Linki przekierowujące do ofert szkoleniowych powinny jasno wskazywać możliwość przejścia na stronę z ofertą. Przekierowanie na stronę z kursem wymaga tylko jednego kliknięcia. | 1 |
| NF12 | niefunkcjonalne | UI | Wygląd interfejsów | Interfejsy powinny być spójne pod względem estetycznym. | 1 |
| NF13 | niefunkcjonalne | Bezpieczeństwo | Strony z ofertami | Oferty znajdujące się w naszej bazie pochodzą ze sprawdzonych stron. | 2 |
| NF14 | niefunkcjonalne | Wydajność | Czas załadowania listy wyników | Użytkownikowi powinna ukazać się lista z wynikami w czasie nie większym niż 3 sekundy. | 2 |
| NF15 | niefunkcjonalne | Wydajność | Czas reakcji| Czas reakcji aplikacji na działanie użytkownika nie powinien przekraczać 3 sekund. | 2 |
| NF16 | niefunkcjonalne | Ergonomia | Rozbudowa aplikacji | Kod aplikacji pozwala na prostą implementację kolejnych funkcjonalności. | 2 |
| NF17 | niefunkcjonalne | Ergonomia | Pielęgnacja aplikacji | Struktura projektu i kod aplikacji muszą być łatwe w utrzymywaniu. | 2 |
| NF18 | niefunkcjonalne | Ergonomia | Aktualizacja bazy z kursami | Aplikacja będzie posiadała jeden główny skrypt, który po uruchomieniu będzie usuwał stare dane o kursach i dostarczał nowe. | 2 |
| NF19 | niefunkcjonalne | UI | Logo aplikacji | Logo aplikacji umieszczone jest w menu nawigacyjnym w lewym górnym rogu oraz w stopce na środku. | 2 |
| NF20 | niefunkcjonalne | Wydajność | Liczba użytkowników na stronie | Maksymalna liczba użytkowników jednocześnie korzystających z aplikacji wynosi 500 osób. | 3 |
| NF21 | niefunkcjonalne | UI | Responsywność | Aplikacja jest w pełni responsywna, aby użytkownik mógł z niej korzystać również na urządzeniu mobilnym. | 3 |

### 5. UML diagrams

**Diagram przypadków użycia**
![UseCaseDiagram](https://github.com/justynagapys/ITworks/blob/main/UML/Diagram%20przypadk%C3%B3w%20u%C5%BCycia.PNG)

**Diagram wdrożenia**
![DeploymentDiagram](https://github.com/justynagapys/ITworks/blob/main/UML/Diagram%20wdro%C5%BCenia.png)

**Diagram aktywności**
![ActivityDiagram](https://github.com/justynagapys/ITworks/blob/main/UML/Diagram%20aktywno%C5%9Bci.PNG)

### 6. Software Architecture

**Portale, z których pochodzą kursy:** alx.pl, cts.com.pl, itschool.pl, luxoft-training.pl, videopoint.pl.

#### Architektura rozwoju:
| LP. | Nazwa produktu | Przeznaczenie w projekcie | Wersja |
| --- | -------------- | ------------------------- | ------ |
| 1 | Python | Backend aplikacji oraz scrapping ofert szkoleniowych | 3.9.2 (19.02.2021) |
| 2 | Flask | Backend aplikacji | 1.1.2 (03.04.2020) |
| 3 | SQLite | Zarządzanie relacyjną bazą danych z ofertami | 3.33.0 (14.08.2020) |
| 4 | Beautiful Soup | Web scraping | 4.9.3 (03.10.2020) |
| 5 | Requests | Uproszczenie żądań | 2.25.0 (11.11.2020) |
| 6 | Matplotlib | Wykresy do rankingu | 3.1.3 (02.02.2020) |
| 7 | HTML5 | Struktura widoków aplikacji | 1.4938 (01.11.2016) |
| 8 | CSS3 | Wygląd interfejsów | v. 3 (07.06.2011)|
| 9 | Bootstrap | Wygląd interfejsów | 4.4.1 (28.11.2019) |
| 10 | visual-paradigm.com | Stworzenie diagramu UML | (2020) |

#### Architektura uruchomieniowa:
| LP. | Nazwa produktu | Przeznaczenie w projekcie | Wersja |
| --- | -------------- | ------------------------- | ------ |
| 1 | Visual Studio Code | Środowisko IDE używane przy tworzeniu projektu | 1.55.0 (30.03 2021) |
| 2 | Google Chrome | Przeglądarka używana przy uruchamianiu projektu | 90.0.4430.51 (31.03. 2021) |
| 3 | Windows 10 | System operacyjny używany przy tworzeniu projektu | 20H2 10.0.19042.870 (29.10.2020) |
| 4 | GitHub | Udostępnianie repozytorium projektowego pomiędzy twórcami | - |
| 5 | Git | System kontroli wersji tworzonej aplikacji | 2.31.1 (26 marca 2021) |

### 7. Tests

| Funkcjonalność | Cel testu | Warunki wstępne | Akcja | Oczekiwana wartość |
| -------------- | --------- | --------------- | ----- | ------------------ |
| F1 | Wyświetlenie widoku z rankingami dotyczącymi ofert kursów. | Dostęp do Internetu oraz przeglądarki. | Użytkownik przechodzi na stronę ITworks poprzez wpisanie w przeglądarce adresu URL. | Użytkownikowi ukazuje się strona główna z rankingami dotyczącymi ofert kursów. | 
| F2 | Wyświetlenie widoku z wyszukiwarką. | Użytkownik znajduje się na stronie głównej ITworks. | Użytkownik wybiera przycisk „Wyszukiwarka” w menu nawigacyjnym strony lub wpisuje odpowiedni adres URL. | Użytkownikowi ukazuje się strona z wyszukiwarką. |
| F3, F6 | Wyszukanie ofert według wpisanej frazy w pole wyszukiwarki.  | Użytkownik znajduje się na stronie z wyszukiwarką oraz ma możliwość wpisania tekstu w pole wyszukiwania. | Użytkownik wpisuje interesującą go frazę w pole tekstowe, następnie wybiera przycisk „Wyszukaj”. | Użytkownikowi ukazuje się lista dostępnych kursów bądź komunikat o braku kursów. |
| F4 | Przejście do strony zewnętrznej oferującej kurs. | Użytkownik otrzymuje minimalnie jeden wynik z ofertą szkoleniową. | Użytkownik wybiera interesujący go kurs i poprzez kliknięcie przycisku „Przejdź do kursu” zostaje przekierowany na stronę podmiotu oferującego kurs. | Użytkownik przechodzi na stronę z kursem i widzi szczegóły dotyczące oferty. |
| F5 | Przejście do strony z rankingami. | Użytkownik znajduje się na stronie z wyszukiwarką. | Użytkownik wybiera przycisk „Rankingi” w menu nawigacyjnym strony. | Użytkownikowi ukazuje się strona z rankingami. |
| F7 | Wyszukanie ofert według języku programowania. | Użytkownik znajduje się na stronie z wyszukiwarką. | Użytkownik wybiera jeden z przycisków znajdujących się nad wyszukiwarką. | Po wybraniu danego przycisku z kategorią użytkownikowi ukazują się odpowiednie wyniki ofert. |
| F8 | Napisanie wiadomości do twórców strony. | Użytkownik znajduje się na stronie z wyszukiwarką. | Użytkownik wybiera przycisk „Napisz”. Po kliknięciu ma bezpośrednią możliwość zredagowania wiadomości mailowej na adres itworks.website@gmail.com. | Użytkownik pomyślnie wysyła wiadomość na podany adres email. |
| F9 | Wyświetlenie użytkownikowi dedykowanych stron dla kodu błędu: 500, 404, 400. | Znajdowanie się na dowolnej stronie ITworks. | Użytkownik wpisuje w adresie URL błędną frazę. | Ukazanie się odpowiednio dedykowanej strony określającej kod błędu. |
| F10 | Wyświetlenie liczby wyników. | Znajdowanie się na stronie z wyszukiwarką oraz wyszukanie kursu/wybranie kategorii języku programowania. | Użytkownik wpisuje słowo-klucz w wyszukiwarkę lub wybiera jedną z kategorii języka programowania. | Użytkownikowi ukazuje się komunikat „Liczba wyników” z adekwatną liczbą wyszukanych ofert. |

# INŻYNIERIA OPROGRAMOWANIA
# rok akademicki 2020/2021
## ITWORKS - DOKUMENTACJA

## Spis treści:
1. [Charakterystyka oprogramowania](#1-charakterystyka-oprogramowania)
2. [Prawa autorskie](#2-prawa-autorskie)
3. [Specyfikacja wymagań](#3-specyfikacja-wymagań)
4. [Projekt (język UML)](#4-projekt-język-uml)
5. [Architektura systemu / oprogramowania](#5-architektura-systemu--oprogramowania)
6. [Testy](#6-testy)

### 1. Charakterystyka oprogramowania

**Nazwa skrócona:** ITworks <br> 
**Nazwa pełna:** ITworks – search courses and develop your IT skills <br> 
**Krótki opis:** Portal pozwalający na wyszukiwanie interesujących ofert szkoleniowych w zakresie technologii informacyjnej.

#### Projekt aplikacji:

**Rankingi**
![Rankings](https://github.com/justynagapys/ITworks/blob/main/mockup/Rankingi.png)

**Wyszukiwarka**
![Browser](https://github.com/justynagapys/ITworks/blob/main/mockup/Wyszukiwarka.png)
![Browser with search](https://github.com/justynagapys/ITworks/blob/main/mockup/Wyszukiwarka%20%2B%20Java.png)

**Brak kursów**
![NoCourses](https://github.com/justynagapys/ITworks/blob/main/mockup/Brak%20kurs%C3%B3w.png)

**Strona błędu**
![ErrorPage](https://github.com/justynagapys/ITworks/blob/main/mockup/B%C5%82%C4%85d.png)

### 2. Prawa autorskie 

**Autorzy:** Karolina Lewińska, Justyna Gapys, Marcin Wiśniewski <br> 
**Licencja:** Uznanie autorstwa - użycie niekomercyjne 4.0

### 3. Specyfikacja wymagań

| ID | Kategoria     | Podkategoria                 | Nazwa krótka              | Opis                                                               | Priorytet |
| -- | ------------- | ---------------------------- | ------------------------- | ------------------------------------------------------------------ | --------- |
| F1 | funkcjonalne | Strona główna | Statystyki | Użytkownik po wejściu na stronę główną widzi statystyki dotyczące liczby dostępnych kursów o najpopularniejszej tematyce oraz odnoszące się do najpopularniejszych języków programowania. | 1 |
| F2 | funkcjonalne | Nawigacja | Przejście do wyszukiwarki | Użytkownik może poprzez kliknięcie przycisku “Wyszukiwarka” w menu nawigacyjnym przejść na podstronę z wyszukiwarką kursów. | 1 |
| F3 | funkcjonalne | Dostosowywanie wyników stron | Wyszukiwanie | Użytkownik po wpisaniu w pole tekstowe interesującej go frazy otrzyma listę wyników z ofertami szkoleń domyślnie posortowanymi alfabetycznie. | 1 |
| F4 | funkcjonalne | Nawigacja | Przekierowanie | Użytkownik po wybraniu interesującego go szkolenia może przejść na stronę danej oferty poprzez kliknięcie w link. | 1 |
| F5 | funkcjonalne | Nawigacja | Przejście do  statystyk | Użytkownik ma możliwość powrotu do strony ze statystykami poprzez kliknięcie przycisku “Rankingi” w menu nawigacyjnym. | 1 |
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

### 4. Projekt (język UML)

![UseCaseDiagram](https://github.com/justynagapys/ITworks/blob/main/UML/Diagram%20przypadk%C3%B3w%20u%C5%BCycia.PNG)

### 5. Architektura systemu / oprogramowania

**Portale, z których pochodzą kursy:** alx.pl, cts.com.pl, itschool.pl, luxoft-training.pl, videopoint.pl

#### Architektura rozwoju:
| LP. | Nazwa produktu | Przeznaczenie w projekcie | Wersja |
| --- | -------------- | ------------------------- | ------ |
| 1 | Python | Backend aplikacji oraz scrapping ofert szkoleniowych | 3.9.2 (19.02.2021) |
| 2 | SQL | Zapytania do bazy z ofertami | (2016) |
| 3 | Flask | Backend aplikacji | 1.1.2 (03.04.2020) |
| 4 | SQLite | Zarządzanie relacyjną bazą danych z ofertami | 3.33.0 (14.08.2020) |
| 5 | Beautiful Soup | Web scraping | 4.9.3 (03.10.2020) |
| 6 | Requests | Uproszczenie żądań | 2.25.0 (11.11.2020) |
| 7 | Matplotlib | Wykresy do rankingu | 3.1.3 (02.02.2020) |
| 8 | HTML5 | Struktura widoków aplikacji | 1.4938 (01.11.2016) |
| 9 | CSS3 | Wygląd interfejsów | v. 3 (07.06.2011)|
| 10 | Bootstrap | Wygląd interfejsów | 4.4.1 (28.11.2019) |
| 11 | app.moqups.com | Stworzenie projektu aplikacji | 2.11.34 |
| 12 | visual-paradigm.com | Stworzenie diagramu UML | (2020) |

#### Architektura uruchomieniowa:
| LP. | Nazwa produktu | Przeznaczenie w projekcie | Wersja |
| --- | -------------- | ------------------------- | ------ |
| 1 | Visual Studio Code | Środowisko IDE używane przy tworzeniu projektu | 1.55.0 (30.03 2021) |
| 2 | Google Chrome | Przeglądarka używana przy uruchamianiu projektu | 90.0.4430.51 (31.03. 2021) |
| 3 | Windows 10 | System operacyjny używany przy tworzeniu projektu | 20H2 10.0.19042.870 (29.10.2020) |
| 4 | GitHub | Udostępnianie repozytorium projektowego pomiędzy twórcami | - |
| 5 | Git | System kontroli wersji tworzonej aplikacji | 2.31.1 (26 marca 2021) |

### 6. Testy

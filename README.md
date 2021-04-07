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

### 2. Prawa autorskie 

**Autorzy:** Karolina Lewińska, Justyna Gapys, Marcin Wiśniewski <br> 
**Licencja:** Uznanie autorstwa - użycie niekomercyjne 4.0

### 3. Specyfikacja wymagań

| ID | Kategoria     | Podkategoria                 | Nazwa krótka              | Opis                                                               | Priorytet |
| -- | ------------- | ---------------------------- | ------------------------- | ------------------------------------------------------------------ | --------- |
| F1 | funkcjonalne | Strona główna | Statystyki | Użytkownik po wejściu na stronę główną widzi statystyki dotyczące liczby dostępnych kursów o najpopularniejszej tematyce. | 1 |
| F2 | funkcjonalne | Nawigacja | Przejście do wyszukiwarki | Użytkownik może poprzez kliknięcie przycisku “Wyszukiwarka kursów” w menu nawigacyjnym przejść na podstronę z wyszukiwarką. | 1 |
| F3 | funkcjonalne | Dostosowywanie wyników stron | Wyszukiwanie | Użytkownik po wpisaniu w pole tekstowe interesującej go frazy otrzyma listę wyników z ofertami szkoleń domyślnie posortowanymi alfabetycznie. | 1 |
| F4 | funkcjonalne | Nawigacja | Przekierowanie | Użytkownik po wybraniu interesującego go szkolenia może przejść na stronę danej oferty poprzez kliknięcie w link. | 1 |
| F5 | funkcjonalne | Dostosowywanie wyników ofert | Brak wyników | Jeśli wpisana w wyszukiwarkę przez użytkownika fraza nie będzie pasować do żadnej z ofert to zostanie mu wyświetlony komunikat “Brak dostępnych kursów”. | 2 |
| F6 | funkcjonalne | Nawigacja | Przejście do  rankingu | Użytkownik ma możliwość przejścia do podstrony z rankingiem poprzez kliknięcie przycisku “Ranking” w menu nawigacyjnym. | 2 |
| F7 | funkcjonalne | Dostosowywanie wyników ofert | Wyszukiwanie po kategorii | Użytkownik może wyszukać szkolenia poprzez wciśnięcie jednego z przycisków kategorii (Java, JavaScript, HTML5, PHP, Python, C++, C#, SQL). Po wciśnięciu przycisku wyświetlana jest lista kursów z wybranej kategorii. | 3 |
| F8 | funkcjonalne | Dostosowywanie wyników ofert | Paging | Użytkownik może przejść do kolejnej strony z wynikami jeśli szkoleń będzie więcej niż 20 oraz następnie powrócić do poprzedniej strony klikając przyciski na dole  strony. | 3 |
| F9 | funkcjonalne | Dostosowywanie wyników ofert | Sortowanie | Użytkownik może sortować interesujące go materiały szkoleniowe alfabetycznie rosnąco i malejąco według nazwy kursu. | 3 |
| F10 | funkcjonalne | Dostosowywanie wyników ofert | Kursy w rankingu | Użytkownik po wyświetleniu rankingu może od razu przejść do listy kursów dotyczących kategorii rankingowej po kliknięciu jej nazwy. | 3 |
| F11 | funkcjonalne  | Obsługa błędów | Dedykowana strona błędu | Użytkownik po wpisaniu błędnego/nieistniejącego adresu URL widzi dedykowaną stronę z kodem błędu. | 3 |
| NF1 | niefunkcjonalne | Projektowe | Rodzaj oprogramowania | Aplikacja jest oprogramowaniem wolnym. | 1 |
| NF2 | niefunkcjonalne | Projektowe | Rodzaj aplikacji | Portal jest aplikacją webową zrealizowaną w architekturze klient-serwer. | 1 |
| NF3 | niefunkcjonalne | Projektowe | Używana technologia | Wykorzystywana w projekcie technologia wolnodostępna. | 1 |
| NF4 | niefunkcjonalne | Projektowe | Obsługiwane przeglądarki | Aplikacja działa w przeglądarkach takich jak Google Chrome, Internet Explorer, Safari, Opera, Mozilla Firefox.| 1 |
| NF5 | niefunkcjonalne | Projektowe | Dostęp do internetu | Aplikacja działa tylko i wyłącznie jeśli użytkownik posiada dostęp do internetu. | 1 |
| NF6 | niefunkcjonalne | Projektowe | Środowisko pracy aplikacji | Aplikacja działa w systemie operacyjnym Windows, macOS, Linux. | 1 |
| NF7 | niefunkcjonalne | Bezpieczeństwo | Strony z ofertami | Oferty znajdujące się w naszej bazie pochodzą ze sprawdzonych stron. | 2 |
| NF8 | niefunkcjonalne | Bezpieczeństwo | Utrata połączenia sieciowego | Po przywróceniu utraconego połączenia sieciowego użytkownik pozostaje na tej samej stronie, na której był. | 3 |
| NF9 | niefunkcjonalne | Bezpieczeństwo | Testowalność aplikacji | Środowisko testowe powinno być stworzone w taki sposób aby funkcjonalność aplikacji była możliwa do przetestowania. | 1 |
| NF10 | niefunkcjonalne | Wydajność | Czas załadowania listy wyników | Użytkownikowi powinna ukazać się lista z wynikami w czasie nie większym niż 3 sekundy. | 2 |
| NF11 | niefunkcjonalne | Wydajność | Liczba użytkowników na stronie | Maksymalna liczba użytkowników jednocześnie korzystających z aplikacji wynosi 500 osób. | 3 |
| NF12 | niefunkcjonalne | Ergonomia | Rozbudowa aplikacji | Kod aplikacji pozwala na prostą implementację kolejnych funkcjonalności. | 2 |
| NF13 | niefunkcjonalne | UI | Język aplikacji| Strona jest stworzona w języku polskim. | 1 |
| NF14 | niefunkcjonalne | UI | Nawigacja aplikacji | Wszystkie podstrony powinny być łatwe w odnalezieniu przez użytkownika. | 1 |
| NF15 | niefunkcjonalne | UI | Sposób wyświetlania listy oferty | Lista z ofertami kursów powinna być wyświetlona w sposób przejrzysty i zrozumiały dla użytkownika. | 1 |
| NF16 | niefunkcjonalne | UI | Linki przekierowujące do oferty | Linki przekierowujące do ofert szkoleniowych powinny jasno wskazywać możliwość przejścia na stronę z ofertą. Przekierowanie na stronę z kursem wymaga tylko jednego kliknięcia. | 1 |
| NF17 | niefunkcjonalne | UI | Wygląd interfejsów | Interfejsy powinny być spójne pod względem estetycznym. | 1 |

### 4. Projekt (język UML)

### 5. Architektura systemu / oprogramowania

#### Architektura rozwoju:
| LP. | Nazwa produktu | Przeznaczenie w projekcie | Wersja |
| --- | -------------- | ------------------------- | ------ |
| 1 | Python | Backend aplikacji oraz scrapping ofert szkoleniowych | 3.9.2 (19.02.2021) |
| 2 | SQL | Zapytania do bazy z ofertami | (2016) |
| 3 | Flask | Backend aplikacji | 1.1.2 (03.04.2020) |
| 4 | SQLite | Zarządzanie relacyjną bazą danych z ofertami | 3.33.0 (14.08.2020) |
| 5 | Beautiful Soup | Web scraping | 4.9.3 (03.10.2020) |
| 6 | Requests | Biblioteka do uproszczenia żądań | 2.25.0 (11.11.2020) |
| 7 | Pandas | Stworzenie rankingu | 1.2.3 (02.03.2021) |
| 8 | Matplotlib | Wykresy do rankingu | 3.1.3 (02.02.2020) |
| 9 | HTML5 | Struktura widoków aplikacji | 1.4938 (01.11.2016) |
| 10| CSS3 | Wygląd widoków | v. 3 (07.06.2011)|
| 11| Bootstrap | Wygląd widoków | 4.4.1 (28.11.2019) |

#### Architektura uruchomieniowa:
| LP. | Nazwa produktu | Przeznaczenie w projekcie | Wersja |
| --- | -------------- | ------------------------- | ------ |
| 1 | Visual Studio Code | Środowisko IDE używane przy tworzeniu projektu. | 1.55.0 (30.03 2021) |
| 2 | Google Chrome | Przeglądarka używana przy uruchamianiu projektu. | 90.0.4430.51 (31.03. 2021) |
| 3 | Windows 10 | System operacyjny używany przy tworzeniu projektu. | 20H2 10.0.19042.870 (29.10.2020) |
| 4 | GitHub | Udostępnianie repozytorium projektowego pomiędzy twórców. | - |
| 5 | Git | System kontroli wersji tworzonej aplikacji. | 2.31.1 (26 marca 2021) |

### 6. Testy

# INŻYNIERIA OPROGRAMOWANIA
# rok akademicki 2020/2021
## ITWORKS - DOKUMENTACJA

### 1.  Charakterystyka  oprogramowania.
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
| F2 | funkcjonalne | Nawigacja | Przejście do wyszukiwarki | Użytkownik może poprzez kliknięcie przycisku “Wyszukiwarka kursów” w menu nawigacyjnym przejść na podstronę z wyszukiwarką. | <center> 1 </center> |
| F3 | funkcjonalne  | Dostosowywanie wyników stron | Wyszukiwanie | Użytkownik po wpisaniu w pole tekstowe interesującej go frazy otrzyma listę wyników z ofertami szkoleń domyślnie posortowanymi alfabetycznie. | 1 |
| F4 | funkcjonalne  | Nawigacja | Przekierowanie | Użytkownik po wybraniu interesującego go szkolenia może przejść na stronę danej oferty poprzez kliknięcie w link. | 1 |
| F5 | funkcjonalne  | Dostosowywanie wyników ofert | Brak wyników | Jeśli wpisana w wyszukiwarkę przez użytkownika fraza nie będzie pasować do żadnej z ofert to zostanie mu wyświetlony komunikat “Brak dostępnych kursów”. | 2 |
| F6 | funkcjonalne  | Nawigacja | Przejście do  rankingu | Użytkownik ma możliwość przejścia do podstrony z rankingiem poprzez kliknięcie przycisku “Ranking” w menu nawigacyjnym. | 2 |
| F7 | funkcjonalne  | Dostosowywanie wyników ofert | Wyszukiwanie po kategorii | Użytkownik może wyszukać szkolenia poprzez wciśnięcie jednego z przycisków kategorii (Java, JavaScript, HTML5, PHP, Python, C++, C#, SQL). Po wciśnięciu przycisku wyświetlana jest lista kursów z wybranej kategorii. | 3 |
| F8 | funkcjonalne  | Dostosowywanie wyników ofert | Paging | Użytkownik może przejść do kolejnej strony z wynikami jeśli szkoleń będzie więcej niż 20 oraz następnie powrócić do poprzedniej strony klikając przyciski na dole  strony. | 3 |
| F9 | funkcjonalne  | Dostosowywanie wyników ofert | Sortowanie | Użytkownik może sortować interesujące go materiały szkoleniowe alfabetycznie rosnąco i malejąco według nazwy kursu. | 3 |
| F10 | funkcjonalne  | Dostosowywanie wyników ofert | Kursy w rankingu | Użytkownik po wyświetleniu rankingu może od razu przejść do listy kursów dotyczących kategorii rankingowej po kliknięciu jej nazwy. | 3 |
| F11 | funkcjonalne  | Obsługa błędów | Dedykowana strona błędu | Użytkownik po wpisaniu błędnego/nieistniejącego adresu URL widzi dedykowaną stronę z kodem błędu. | 3 |

# Programming exercise 1 for Technics and Architecture of Computers at my uni

## details in polish below

Dane są trzy liczby całkowite dodatnie a, b, c.
Wyznacz a-tą cyfrę znaczącą ilorazu b/c (tzn. a-tą cyfrę, licząc od pierwszej cyfry niezerowej).

Przykładowo:

    Dla dowolnego a > 0, b = 2 oraz c = 3 oraz program powinien zwrócić 6.
    Dla a = 1, b = 10000, c = 8 program powinien zwrócić 1.
    Dla a = 2, b = 10000, c = 8 program powinien zwrócić 2.
    Dla a = 3, b = 10000, c = 8 program powinien zwrócić 5.
    Dla dowolnego a > 3, b = 10000 oraz c = 8 program powinien zwrócić 0.
    Dla a = 1, b = 1, c = 2000 program powinien zwrócić 5.
    Dla dowolnego a > 1, b = 1 oraz c = 2000 program powinien zwrócić 0.
    Dla a = 1, b = 71, c = 700 program powinien zwrócić 1.
    Dla a = 2, b = 71, c = 700 program powinien zwrócić 0.
    Dla a = 3, b = 71, c = 700 program powinien zwrócić 1.

WEJŚCIE

Wejście programu składa się z jednej linii, zawierającej kolejno liczby a, b, c, oddzielone spacjami.

WYJŚCIE

Na wyjściu należy wypisać szukaną cyfrę.

ZAŁOŻENIA

Zakładamy, że a, b, c są całkowite dodatnie i mniejsze niż 108.

Wersja uproszczona (za 50% punktów): zakładamy, że a < 6.

WYMAGANIA

    Program powinien zwracać poprawny matematycznie wynik - co oznacza, że w wersji nieuproszczonej nie zadziała zwykłe dzielenie wbudowanych typów zmiennoprzecinkowych (float, double itp.).
    Wykorzystanie typów o nieograniczonej precyzji lub bibliotek wykonujących tego typu obliczenia jest zabronione. (Tzn. chodzi o to, żeby zapewnili Państwo precyzję wyniku samodzielnie).
    Jeżeli język oferuje wyłącznie takie typy (np. int w Pythonie 3), proszę ich użyć tak, jak w C albo Javie. Proszę w żadnym momencie nie przechowywać w pamięci liczb ponad 20-cyfrowych.
    W razie pytań proszę o maila.
    Nie ograniczam języka programowania.
    Program powinien działać w rozsądnym czasie (maksymalnie rzędu minuty). Jeżeli u kogoś ten warunek będzie prawie spełniony (np. kilkanaście minut dla największych danych), może to być usprawiedliwione przez wybór języka lub sprawy sprzętowe; proszę o maila, być może też zaakceptuję.
    Zastrzegam sobie prawo do przyznania dodatkowych punktów za szczególnie wydajne programy (da się zejść do ułamków sekund zakładając b, c < 105 przy a < 108), oraz karcenia za szczególnie chaotyczny kod.

PRZYKŁAD

Dla wejścia

3 100 8

program powinien wypisać

5

WSKAZÓWKA

Warto przypomnieć sobie dzielenie pisemne. Jeśli wynik byłby wypisywany na bieżąco, w czasie jego wykonywania nigdy nie trzeba pamiętać zbyt dużych liczb, a dokładność wyniku można uzyskać dowoloną.
'''
Program przechowuje w pamięci dynamicznie zmienianą liczbę b
Zmiany przypominają dzielenie pisemne.
Nowa wartość b wynosić będzie tyle co wartość b z poprzedniej iteracji pomniejszona o n-tą wielokrotność c, taką że n*c <= b
Jeśli nowa wartość b < c, podnosimy rząd wielkości b
'''

'''
TODO komentarz od prowadzącej:

Program działa na dobrej zasadzie, choć czasami źle liczy cyfry.
W efekcie daje błędny wynik dla niektórych przykładów z treści zadania (np. "1 2 3", "1 1 2000").

Drobne uwagi do kodu (bez wpływu na punktację):
- Linia 28: można po prostu "b %= c"
- Linia 30: zbędna, curr_b musi być mniejsze od c w tym momencie
'''

#pobranie wejścia
a, b, c = [int(i) for i in input("podaj a,b,c oddzielone spacjami\n").split(" ")]

#sprowadzenie b do rzędu wielkości, w którym b/c < 10
curr_b = b
while True:
    if not(curr_b/c < 10):
        curr_b /= 10
    else:
        break

iter = 1
while True:
    #iteracja końcowa, podanie wyniku
    if iter == a:
        #dodaję jedną milionową dla sytuacji, w której 1 przechowywane jest jako np 0.9999999999999787
        print(int(curr_b/c+0.000000001))
        break

    #wykonanie przejścia do kolenego 'wiersza' dzielenia
    curr_b -= int(curr_b/c)*c

    if(curr_b < c):
        curr_b *= 10
    
    iter += 1

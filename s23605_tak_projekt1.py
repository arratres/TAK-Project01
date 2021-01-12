'''
Program przechowuje w pamięci dynamicznie zmienianą liczbę b
wartość b jest dostosowana wcześniej tak, by b/c należało do zbioru <1,10)
Zmiany przypominają dzielenie pisemne.
Nowa wartość b wynosić będzie tyle co wartość b z poprzedniej iteracji pomniejszona o n-tą wielokrotność c, taką że n*c <= b
Jeśli nowa wartość b < c, podnosimy rząd wielkości b
'''

#pobranie wejścia
a, b, c = [int(i) for i in input("podaj a,b,c oddzielone spacjami\n").split(" ")]

#sprowadzenie b do rzędu wielkości, w którym b/c < 10 oraz b/c > 0
while True:
    if not(b/c < 10):
        b /= 10
    elif not(b/c >= 1):
        b *= 10
    else:
        break

iter = 1
while True:

    #iteracja końcowa, podanie wyniku
    if iter == a:
        #dodaję jedną milionową dla sytuacji, w której 1 przechowywane jest jako np 0.9999999999999787
        print(int(b/c+0.000000001))
        break

    #wykonanie przejścia do kolenego 'wiersza' dzielenia
    b %= c
    b *= 10
    iter += 1

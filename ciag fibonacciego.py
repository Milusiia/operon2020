liczba = 10

def ciag_fibonacciego(liczba):
    a = 0
    b = 1
    suma = 0
    for x in range(liczba-1):
        suma = a + b
        a = b
        b = suma
        print(suma)
    return suma

ciag_fibonacciego(liczba)
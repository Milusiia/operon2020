import math

liczby_pierwsze = []
liczby_super_pierwsze = []
liczby_super_b_pierwsze = []

def pierwsza(liczba):
    if liczba != 2:
        for x in range(2, int(math.sqrt(liczba) + 2)):
            if liczba % x == 0:
                return False
    liczby_pierwsze.append(liczba)
    return True

def suma_pierwszych():
    for liczba in liczby_pierwsze:
        suma=0
        for x in str(liczba):
            suma+=int(x)
        sprawdz_czy_super_pierwsza(suma,liczba)

def sprawdz_czy_super_pierwsza(suma,liczba):
    if suma!=2:
        for x in range(2, int(math.sqrt(suma) + 2)):
            if suma% x == 0:
                return False
            else:
                liczby_super_pierwsze.append(liczba)
                return True
    liczby_super_pierwsze.append(liczba)
    return True

def suma_b():
    for li in liczby_super_pierwsze:
        suma=0
        binarny = bin(li)
        binarny = binarny.replace("b", "")
        for y in binarny:
            suma+=int(y)
        sprawdz_czy_b(li,suma)

def sprawdz_czy_b(li,suma):
    if suma != 2:
        for x in range(2, int(math.sqrt(suma) + 2)):
            if suma % x == 0:
                return False
    liczby_super_b_pierwsze.append(li)
    return True

list({pierwsza(li)} for li in range(2, 1001))
print(liczby_pierwsze,"\n","ilosc pierwszych:", len(liczby_pierwsze))
suma_pierwszych()
print(liczby_super_pierwsze,"\n","ilosc super pierwszych:", len(liczby_super_pierwsze))
suma_b()
print(liczby_super_b_pierwsze,"\n","ilosc super B pierwszych:", len(liczby_super_b_pierwsze))


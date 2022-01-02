liczby_doskonale = []

def sprawdz_czy_doskonala(liczba):
    suma = 1
    for x in range(2,int(liczba/2)+1):
        if liczba % x == 0:
            suma+=x
    if suma == liczba:
        liczby_doskonale.append(liczba)

for liczba in range (1,10001):
    sprawdz_czy_doskonala(liczba)

print(liczby_doskonale)

file = open("example.txt", "r")


def oblicz(operacja, li1, li2):
    if operacja == 'DODAJ':
        wynik = li1 + li2
    elif operacja == 'ODEJMIJ':
        wynik = li1 - li2
    elif operacja == 'PODZIEL':
        wynik = li1 / li2
    else:
        wynik = li1 * li2
    return wynik


def obliczenia():
    for line in file:
        podzial = line.split()
        operator = podzial[0]
        l1 = int(podzial[1])
        l2 = int(podzial[2])
        print(operator, l1, l2)

        print(oblicz(operator,l1,l2))

obliczenia()

print('asd as as  aae ae g g      \n\n\n\n\n\n g'.split())

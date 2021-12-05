s = 'DUPA'


def cezar(key, string):
    wynik = ''
    for x in string:
        liczbowo = ord(x) + key
        czar = chr(liczbowo)
        wynik += czar
    return wynik


zaszyfrowane = cezar(2, "ABC")
print(zaszyfrowane)

print(cezar(-2, zaszyfrowane))
# 9linijka cezar klucz 2

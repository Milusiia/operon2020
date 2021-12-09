def czy_anagram(wyraz, wyraz2):
    if len(wyraz) != len(wyraz2):
        return False

    if sorted(wyraz) == sorted(wyraz2):
        return True
    return False


def sprawdz_ile_anagramow():
    file = open("wordlist-test.txt")

    wyrazy = list(map(lambda s: s.replace('\n', ''), file.readlines()))

    suma = 0
    for i in range(len(wyrazy)):
        print(i)
        wyraz = wyrazy[i]
        for j in range(i + 1, len(wyrazy)):
            wyraz2 = wyrazy[j]
            if czy_anagram(wyraz, wyraz2):
                suma += 1
    file.close()
    return suma


print(f'Liczba anagramów w pliku: {sprawdz_ile_anagramow()}')

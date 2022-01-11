file = open("sygnaly.txt")
def szyfr():
    wynik = " "
    suma = 0
    for line in file:
        suma +=1
        if suma % 40 == 0:
            sumaa = 0
            for x in line:
                sumaa += 1
                if sumaa == 10:
                    wynik += x
    print(wynik)
    return wynik

#szyfr()

def slowo():
    max = 0
    word = " "
    for line in file:
        s = []
        suma = 0
        for x in line:
            if x not in s and x!="\n":
                s.append(x)
                suma+=1
        if suma > max:
            max = suma
            word = line
    print(max, word)

#slowo()

def sprawdz_czy_litera_nie_spelnia(litera, slowo):
    for x in slowo:
        if abs(ord(litera) - ord(x)) > 10:
            return True
    return False

def dlugosc_improved():
    words = ""
    for line in file:
        line_s = line.strip()
        to_break = False
        for x in line_s:
            to_break = sprawdz_czy_litera_nie_spelnia(x, line_s)
            if to_break:
                break
        if not to_break:
            words += line_s + '\n'
    print(words)

def dlugosc():
    words = ""
    for line in file:
        line_s = line.strip()
        to_break = False
        for x in line_s:
            for y in line_s:
                if abs(ord(x)-ord(y)) > 10:
                    to_break = True
                    break
            if to_break:
                break
        if not to_break:
            words += line_s + '\n'
    print(words)
dlugosc_improved()


from random import randint

file = open("words.txt", "r")
dict_ang = {}
dict_pl = {}

for line in file:
    podzial = line.split()
    ang = podzial[0]
    pl = podzial[2]
    dict_ang[ang] = pl

dict_pl = dict([(value, key) for key, value in dict_ang.items()])

def compartment():
    compartment = randint(1, 2)
    return compartment

def game():
    x = compartment()
    if x == 1:
        for word in dict_ang.keys():
            print(word)
            x = input()
            y = dict_ang.get(str(word))
            if x==y:
                print("dobrze! :)" + "\n")
            else:
                print("źle :(" + "\n")
    else:
        for word in dict_pl.keys():
            print(word)
            x = input()
            y = dict_pl.get(str(word))
            if x == y:
                print("dobrze! :)" + "\n")
            else:
                print("źle :(" + "\n")

game()

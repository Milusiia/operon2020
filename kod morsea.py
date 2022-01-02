file = open("morse_code.txt")
dict1 = {}
for line in file:
    znak = line[0]
    morse = line[2:(len(line) - 1)]
    dict1[znak] = morse
dict_n = dict1
print(dict_n)
print(dict_n.items())

# dict_m = dict([(value, key) for key, value in dict_n.items()])
dict_m = {}
for key, value in dict_n.items():
    dict_m[value] = key

print(dict_m)


def convert_to_morse(s):
    slowo = ""
    for x in s.upper():
        slowo += dict_n[x] + " "
    return slowo


morse_s = convert_to_morse('Oliwia Sieradzka 2003')
print(morse_s)


def convert_morse_to_normal(s):
    slowo = ""
    for x in s.split():
        slowo += dict_m[x]
    return slowo

normal_s = convert_morse_to_normal(morse_s)
print(normal_s)
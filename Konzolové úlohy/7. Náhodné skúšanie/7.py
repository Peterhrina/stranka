import random

studenti = [i for i in range(1, int(input("Zadajte počet študentov:")) + 1)]
otazky = [i for i in range(1, int(input("Zadajte počet otázok:")) + 1)]

random.shuffle(studenti)

parne = []
neparne = []
for i in otazky:
    if i % 2 == 0:
        parne.append(i)
    else:
        neparne.append(i)
random.shuffle(parne)
random.shuffle(neparne)
poradie_otazok = []
for i in range(len(neparne)):
    poradie_otazok.append(parne[i])
    poradie_otazok.append(neparne[i])

if len(otazky) < len(studenti):
    print("Program sa skončil pre málo otázok na počet študentov.")
    exit()

print("Poradie odpovedajúcich a ich číslo otázky:")
for i in range(len(studenti)):
    print(f"{i + 1}. študent: {studenti[i]}, otázka: {poradie_otazok[i]}")
import random

subor = "/Users/nkubala/Projekty/Python/skolsky-rok-2025-26/Škola-hodiny/Precvičovanie/Material_dudo/25. Lotéria/loteria_2.txt"
with open(subor, "r", encoding = "UTF-8") as fr:
    nacitane_riadky = fr.readlines()

vyherna_kombinacia: set[str] = set(random.sample(range(1, 50), 6))

while True:
    uzivatel_vstup: list[str] = input("Zadajte 6 výherných čísiel od 1-49 oddelených medzerou: ").split()
    if len(uzivatel_vstup) != 6:
        print(f"Zadajte 6 čísel oddelených medzerou!")
    elif len(uzivatel_vstup) == 6:
        break

uhadnute_pocet: dict[int, int] = {poradie: 0 for poradie in range(7)}

for riadok in nacitane_riadky:
    prienik_cislo: int = len(vyherna_kombinacia.intersection(riadok.split()))
    uhadnute_pocet[prienik_cislo] += 1

uhadnutych_uzivatel: int = len(vyherna_kombinacia.intersection(uzivatel_vstup))

print(f"""
Výherná kombinácia je: {(" ").join(vyherna_kombinacia)}
Uhádol si {uhadnutych_uzivatel} zo šiestich!

Koľko ľudí uhadlo koľko čísel:
Nula čísel uhádlo: {uhadnute_pocet[0]}
Jedno číslo uhádlo: {uhadnute_pocet[1]}
Dve čísla uhádli: {uhadnute_pocet[2]}
Tri čísla uhádli: {uhadnute_pocet[3]}
Štyri čísla uhádli: {uhadnute_pocet[4]}
Päť čísel uhádlo: {uhadnute_pocet[5]}
Šesť čísel uhádlo: {uhadnute_pocet[6]}""")
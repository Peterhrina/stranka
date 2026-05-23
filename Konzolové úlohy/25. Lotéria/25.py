import random as rd

vstup:str = "Škola-hodiny/Precvičovanie/Material_dudo/25. Lotéria/loteria_2.txt"
def otvaranie(vstup: str) -> list[str]:
    with open(vstup, "r", encoding = "UTF-8")as fr:
        return fr.readlines()

vitazne: set[str] = {str(cislo) for cislo in rd.sample(range(1, 50), 6)}

uzivatelove_tipy: list[str] = input("Vyber 6 čísel od 1 po 49, oddelené medzerou: ").split()

uhadnute_uzivatel: set[str] = vitazne.intersection(uzivatelove_tipy)

print(f"Víťazné čísla sú: {" ".join(list(vitazne))}")

if len(uhadnute_uzivatel) > 0:
    print(f"Úhádol si {len(uhadnute_uzivatel)} čísel zo 6!")
else:
    print(f"Neúhádol si ani jedno číslo!")

uhadnute_subor: dict[int, int]= {poradie: 0 for poradie in range(0, 7)}

nacitane_riadky: list[str] = otvaranie(vstup)

for riadok in nacitane_riadky:
    pocet_uhadnutych: set[str] = vitazne.intersection(riadok.split())
    uhadnute_subor[len(pocet_uhadnutych)] += 1

print(f"""
Počet uhádnutých čísel v súbore:

Nula čísel uhádlo: {uhadnute_subor[0]}
Jedno číslo uhádlo: {uhadnute_subor[1]}
Dve čísla uhádli: {uhadnute_subor[2]}
Tri čísla uhádli: {uhadnute_subor[3]}
Štyri čísla uhádli: {uhadnute_subor[4]}
Päť čísel uhádlo: {uhadnute_subor[5]}
Šesť čísel uhádlo: {uhadnute_subor[6]}""")
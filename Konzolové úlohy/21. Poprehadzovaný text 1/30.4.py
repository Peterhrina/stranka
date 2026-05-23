import random

VSTUP = "Škola-hodiny/Precvičovanie/Material_dudo/Konzolové úlohy/21. Poprehadzovaný text 1/poprehadzovany_text1_vstup.txt"
VYSTUP = "Škola-hodiny/Precvičovanie/Material_dudo/Konzolové úlohy/21. Poprehadzovaný text 1/vysledok.txt"

with open(VSTUP, "r") as fr:
    nacitane_riadky = fr.readlines()

vysledok: list[str] = []
for riadok in nacitane_riadky:
    riadok_temp: list[str] = []
    for slovo in riadok.split():
        slovo_list = [pismenko for pismenko in slovo[1:-1]]
        random.shuffle(slovo_list)
        if len(slovo) > 3:
            upravene_slovo = slovo[0] + "".join(slovo_list) + slovo[-1]
            riadok_temp.append(upravene_slovo)
        else:
            riadok_temp.append(slovo)
    vysledny_riadok = " ".join(riadok_temp)
    print(vysledny_riadok)
    vysledok.append(vysledny_riadok)

with open(VYSTUP, "w") as fw:
    for riadok in vysledok:
        fw.write(riadok + "\n")

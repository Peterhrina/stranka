fr = open("Škola-hodiny\Precvičovanie\Material_dudo\hada.txt", "r")
fw = open("Škola-hodiny\Precvičovanie\Material_dudo\zapiss.txt", "w")

pocet_hier = 0
najdlhsia_hra = 0

for riadok in fr:
    pocet_hier += 1
    if len(riadok) > najdlhsia_hra:
        najdlhsia_hra = len(riadok)
    pocitadlo = 1
    for i in range(1, len(riadok)):
        if riadok[i] == riadok[i - 1]:
            pocitadlo += 1
        else:
            fw.write(riadok[i - 1] + str(pocitadlo) + " ")
            pocitadlo = 1

print(f"Najdlhsia hra bola {najdlhsia_hra}")
fw.close()
fr.close()
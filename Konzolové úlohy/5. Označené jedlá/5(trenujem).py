fr = open("Škola-hodiny/Precvičovanie/Material_dudo/5. Označené jedlá/objednane_jedla.txt", "r")

pocitadlo = 0
zoznam_jedal = []
pocet_jedal = {}

for riadok in fr:
    pocitadlo += 1
    zoznam_jedal.append(riadok.split())
for objednavka in zoznam_jedal:
    if objednavka[1] not in pocet_jedal:
        pocet_jedal[objednavka[1]] = 1
    else:
        pocet_jedal[objednavka[1]] += 1

for jedlo, pocet in pocet_jedal.items():
    if pocet < 20:
        print(f"Jedlo {jedlo} si objednalo {pocet} - nedostatok")
    else:
        print(f"Jedlo {jedlo} si objednalo {pocet} - dostatok")

fr.close()
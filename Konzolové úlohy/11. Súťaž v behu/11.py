fr = open("Precvičovanie/Material_dudo/11. Súťaž v behu/sutaz_vbehu.txt", "r")

pocitadlo = 0
riadok_list = []
for riadok in fr:
    pocitadlo += 1
    riadok_list.append(riadok.split())

for beh in riadok_list:
    beh[1] = int(beh[1])

print(f"Počet zúčastnených športovcov: {pocitadlo}")

vitaz_cas = 78787897987
vitaz_meno = ""
for beh in riadok_list:
    print(f"Súťažiaci {beh[0]} dobehol do cieľa za {beh[1]} sekúnd")
    if beh[1] < vitaz_cas:
        vitaz_cas = beh[1]
        vitaz_meno = beh[0]

print(f"Víťazom je {vitaz_meno} s časom {vitaz_cas // 60}min. a {vitaz_cas % 60}sek.")
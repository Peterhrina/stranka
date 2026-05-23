a = "Škola-hodiny/Precvičovanie/Material_dudo/28. Hlasovanie 1/hlasovanie_2.txt"
with open(a, "r", encoding = "UTF-8")as fr:
    nacitane_riadky = fr.readlines()

slov: dict[int, int] = {}
for cislo in nacitane_riadky:
    if int(cislo) in slov:
        slov[int(cislo)] += 1
    else:
        slov[int(cislo)] = 1

print(f"Celkový počet SMS: {sum(slov.values())}")

for cislo, pocet in slov.items():
    print(f"Číslo {cislo} dostalo {pocet} hlasov")

najmensi_hlas = min(slov.items(), key=lambda x: x[1])
print(f"Vypadáva súťažiaci {najmensi_hlas[0]} s {najmensi_hlas[1]} hlasmi")
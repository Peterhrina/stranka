fr = open("Precvičovanie/Material_dudo/12. Vyťaženosť liniek dopravného podniku/bus_vytazenost.txt", "r", encoding="UTF-8")

nacitane_riadky = fr.readlines()

max_kapacita = int(nacitane_riadky[0].strip())

zastavky = []
pocitadlo_zastavok = 0
for i in nacitane_riadky[1:]:
    riadok_bez_enteru = i.strip()
    zastavky.append(riadok_bez_enteru.split(" ", 2))
    pocitadlo_zastavok += 1

print(f"Počet zastávok na trase autobusu: {pocitadlo_zastavok}")

zastavky_nazov_list = []
for zastavenie in zastavky:
    zastavky_nazov_list.append(zastavenie[2])
zastavky_nazov_str = ", ".join(zastavky_nazov_list)
print(f"Toto sú všetky zastávky na trase: {zastavky_nazov_str}")

def pocitanie_preplnenosti(zoznam_zastavok:list):
    priebezne_pocitanie_plnosti = 0
    max_preplnenost = 0
    for zastavenie in zoznam_zastavok:
        priebezne_pocitanie_plnosti += int(zastavenie[0])
        priebezne_pocitanie_plnosti -= int(zastavenie[1])
        if priebezne_pocitanie_plnosti > max_kapacita:
            print(f"Na zastávke {zastavenie[2]} je prekročený maximálny počet cestujúcich.")
        if priebezne_pocitanie_plnosti > max_preplnenost:
            max_preplnenost = priebezne_pocitanie_plnosti
    print(f"Najvyššie možné preplnenie bolo o {max_preplnenost - max_kapacita} ľudí.")

pocitanie_preplnenosti(zastavky)
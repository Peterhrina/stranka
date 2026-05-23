fr = open("Precvičovanie/Material_dudo/5. Označené jedlá/objednane_jedla.txt", "r")

pocet_riadkov = 0
zoznam_objednavka = []
pocet_farieb = {} # Slovník na počítanie výskytov farieb.

# 1. Načíta dáta zo súboru a rozdelí riadky.
for riadok in fr:
    pocet_riadkov += 1
    zoznam_objednavka.append(riadok.split())

# 2. Spočítanie výskytu každej farby pomocou slovníka.
for objednavka in zoznam_objednavka:
    if objednavka[1] not in pocet_farieb:
        pocet_farieb[objednavka[1]] = 1
    else:
        pocet_farieb[objednavka[1]] += 1

# 3. Skontroluje počty a vypíše výsledok pre každé jedlo.
for jedlo, pocet in pocet_farieb.items():
    if pocet < 20:
        print(f"Jedlo {jedlo} si objednalo {pocet} ľudí = nedostatok ľudí")
    else:
        print(f"Jedlo {jedlo} si objednalo {pocet} ľudí = dostatok ľudí")

fr.close()
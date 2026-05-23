fr = open("Škola-hodiny/Precvičovanie/Material_dudo/meteo_stanice.txt", "r")
zoznam = []

def stanice():
    teploty = []
    pocet_merani = 0

    # 1. Načíta súbor a rozdelí každý riadok na zoznam slov.
    for riadok in fr:
        pocet_merani += 1
        zoznam.append(riadok.split())
    
    # 2. Prejde dáta, upraví teplotu na číslo a pridá ju do zoznamu 'teploty'.
    for meranie in zoznam:
        meranie[3] = float(meranie[3].replace(",", ".").replace("+", ""))
        teploty.append(meranie[3])

    print(f"Počet meraní: {pocet_merani}")
    print(f"Teploty: {teploty}")
    print(f"Najvyššia teplota je: {max(teploty)}") # Nájde maximum zo zoznamu teplôt.

    # 3. Nájde kód stanice, ktorá zodpovedá najvyššej teplote.
    for meranie in zoznam:
        if max(teploty) == meranie[3]:
            print(f"Najvyššia teplota je na stanici: {meranie[0]}")
    
    # 4. Vypočíta priemer zo všetkých teplôt.
    print(f"Priemerná teplota je: {sum(teploty) / len(teploty)}")

stanice()
fr.close
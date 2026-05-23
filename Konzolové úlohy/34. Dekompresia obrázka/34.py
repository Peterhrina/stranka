def otvor_subor(vstup: str) -> list[str]:
    with open(vstup, "r", encoding="UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    return nacitane_riadky

def pisanie_subor(vystup: str, obsah: list[str]) -> None:
    with open(vystup, "w", encoding="UTF-8") as fw:
        fw.write(str(sirka) + " " + str(vyska) + "\n")
        for riadok in obsah:
            fw.write("".join(riadok) + "\n")

def spracuj_riadok(riadok: str) -> list[str]:
    spracovany_riadok: list[str] = []
    nula_alebo_jeden: int = 0
    for cislo in riadok.split():
        spracovany_riadok.append(str(nula_alebo_jeden) * int(cislo))
        if nula_alebo_jeden == 0:
            nula_alebo_jeden = 1
        else:
            nula_alebo_jeden = 0
    return spracovany_riadok

vystup: str = "Škola-hodiny/Precvičovanie/Material_dudo/34. Dekompresia obrázka/dekompresia_obrazka_vystup.txt"
vstup: str = "Škola-hodiny/Precvičovanie/Material_dudo/34. Dekompresia obrázka/dekompresia_obrazka_1.txt"
nacitane_riadky: list[str] = otvor_subor(vstup)

sirka, vyska = nacitane_riadky[0].split(" ")
sirka = int(sirka)
vyska = int(vyska)

vysledok: list[str] = []
for riadok in nacitane_riadky[1:]:
    vysledok.append(spracuj_riadok(riadok.strip()))

pisanie_subor(vystup, vysledok)
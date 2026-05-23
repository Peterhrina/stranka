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
    for idx in range(0, sirka * 2, 2):
        hex_cislo: str = riadok[idx : idx+2]
        hodnota: int = int(hex_cislo, 16)
        if hodnota >= 128:
            spracovany_riadok.append("1")
        else:
            spracovany_riadok.append("0")
    return spracovany_riadok

vystup: str = "Škola-hodiny/Precvičovanie/Material_dudo/32. Konverzia súboru 1/konverzia_suboru_1_vystup.txt"
vstup: str = "Škola-hodiny/Precvičovanie/Material_dudo/32. Konverzia súboru 1/ciernobiely_obrazok_1.txt"
nacitane_riadky: list[str] = otvor_subor(vstup)

sirka, vyska = nacitane_riadky[0].split()
sirka = int(sirka)
vyska = int(vyska)

vysledok: list[str] = []
for riadok in nacitane_riadky[1:]:
    vysledok.append(spracuj_riadok(riadok.strip()))

pisanie_subor(vystup, vysledok)
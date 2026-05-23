def sutaz_v_behu(cesta_k_suboru):
    
    with open(cesta_k_suboru, "r",  encoding="UTF-8") as fr:
        zaznam_vysledkov = fr.readlines()
    
    vysledky_zoznam = []
    for zaznam in zaznam_vysledkov:
        vysledky_slovnik = {}
        bezec, cas_sekundy = zaznam.strip().split()
        vysledky_slovnik = {
            "bezec": bezec,
            "cas_sekundy": int(cas_sekundy)
        }
        vysledky_zoznam.append(vysledky_slovnik)

    print(f"Počet zúčastnených športovcov: {len(vysledky_zoznam)}")

    for pretekar in vysledky_zoznam:
        print(f"Súťažiaci {pretekar["bezec"]} dobehol do cieľa za {pretekar["cas_sekundy"]} sekúnd.")

    casy_zoznam = []
    for zaznam in vysledky_zoznam:
        casy_zoznam.append(zaznam["cas_sekundy"])

    for pretekar in vysledky_zoznam:
        if pretekar["cas_sekundy"] == min(casy_zoznam):
            print(
    f"Najrýchlejší pretekár bol {pretekar['bezec']} "
    f"s časom {pretekar['cas_sekundy'] // 60} minút a {pretekar['cas_sekundy'] % 60} sekúnd."
)

subor = "Precvičovanie/Material_dudo/11. Súťaž v behu/sutaz_vbehu.txt"
sutaz_v_behu(subor)
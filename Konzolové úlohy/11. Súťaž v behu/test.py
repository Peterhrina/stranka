def sutaz_v_behu(subor):

    with open(subor, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()

    zaznamy_zoznam = []
    for zaznam in nacitane_riadky:
        meno, cas = zaznam.strip().split()
        zaznam_slovnik = {
            "Meno": meno,
            "Čas_sekundy": int(cas)
        }
        zaznamy_zoznam.append(zaznam_slovnik)

    print(f"Počet zúčastnených športovcov: {len(zaznamy_zoznam)}")

    casy_zoznam = []
    for zaznam in zaznamy_zoznam:
        print(f"Súťažiaci {zaznam["Meno"]} dobehol do cieľa za {zaznam["Čas_sekundy"]} sekúnd.")
        casy_zoznam.append(zaznam["Čas_sekundy"])

    for pretekar in zaznamy_zoznam:
        if pretekar["Čas_sekundy"] == max(casy_zoznam):
            print(
                f"Súťažiaci {pretekar["Meno"]} dobehol do cieľa" 
                f"za {pretekar["Čas_sekundy"] // 60} minút a {pretekar["Čas_sekundy"] % 60} sekúnd.")

subor = "Precvičovanie/Material_dudo/11. Súťaž v behu/sutaz_vbehu.txt"
sutaz_v_behu(subor)
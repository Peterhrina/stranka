def skok(subor):
    with open(subor, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    skoky_zaznam = []
    for riadok in nacitane_riadky:
        meno, krajina, s1, s2, s3, s4, s5 = riadok.split()
        temp_slovnik = {
            "meno": meno,
            "krajina": krajina,
            "best_skok": int(max(s1, s2, s3, s4, s5))
        }
        skoky_zaznam.append(temp_slovnik)
    
    krajiny_slovik = {}
    for zaznam in skoky_zaznam:
        if zaznam["krajina"] not in krajiny_slovik:
            krajiny_slovik[zaznam["krajina"]] = 1
        else:
            krajiny_slovik[zaznam["krajina"]] += 1
    
    zoznam_krajin_str = (", ").join(list(krajiny_slovik.keys()))
    print(f"Zúčastnené krajiny: {zoznam_krajin_str}.")
    for krajina, pocet in krajiny_slovik.items():
        print(f"Z krajiny {krajina} sa zúčasnilo {pocet} športovcov.")
    
    max_skok = max(skoky_zaznam, key = lambda zaznam: zaznam["best_skok"])
    for sutaziaci in skoky_zaznam:
        if sutaziaci["best_skok"] == max_skok["best_skok"]:
            print(f"Najlepší skokan je {sutaziaci["meno"]} so skokom dlhým {sutaziaci["best_skok"]} cm.")
subor = "Precvičovanie/Material_dudo/14. Skok do diaľky/skok_do_dialky.txt"
skok(subor)
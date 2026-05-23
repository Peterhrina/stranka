def skok_do_dialky(subor):
    with open(subor, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    zaznam_skokov = []
    for riadok in nacitane_riadky:
        meno, kod_krajiny, vykon1, vykon2, vykon3, vykon4, vykon5 = riadok.split()
        riadok_slovnik = {
            "meno": meno,
            "kod_krajiny": kod_krajiny,
            "vykon1": int(vykon1),
            "vykon2": int(vykon2),
            "vykon3": int(vykon3),
            "vykon4": int(vykon4),
            "vykon5": int(vykon5), 
            "najlepsi_vykon": int(max(vykon1, vykon2, vykon3, vykon4, vykon5))
        }
        zaznam_skokov.append(riadok_slovnik)
    
    krajiny_slovnik = {}
    for zaznam in zaznam_skokov:
        if zaznam["kod_krajiny"] not in krajiny_slovnik:
            krajiny_slovnik[zaznam["kod_krajiny"]] = 1
        else:
            krajiny_slovnik[zaznam["kod_krajiny"]] += 1
    zoznam_krajin_str = (", ").join(list(krajiny_slovnik.keys()))
    print(f"Zúčastnené krajiny: {zoznam_krajin_str}")
    
    for krajina, pocet in krajiny_slovnik.items():
        print(f"Krajina: {krajina}, Počet zúčastnených: {pocet}")
    
    najlepsi_skok = max(zaznam_skokov, key = lambda zaznam: zaznam["najlepsi_vykon"])
    for zaznam in zaznam_skokov:
        if zaznam["najlepsi_vykon"] == najlepsi_skok["najlepsi_vykon"]:
            print(f"Najlepší bol športovec {zaznam["meno"]} s výkonom {zaznam["najlepsi_vykon"]} cm.")
    
subor = "Precvičovanie/Material_dudo/14. Skok do diaľky/skok_do_dialky.txt"
skok_do_dialky(subor)
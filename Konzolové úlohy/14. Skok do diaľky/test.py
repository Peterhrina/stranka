def skok(subor):
    with open(subor, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    zaznam_skokov = []
    for riadok in nacitane_riadky:
        meno, krajina, skok1, skok2, skok3, skok4, skok5 = riadok.split()
        temp_slovnik = {
            "meno": meno,
            "krajina": krajina,
            "skok_1": int(skok1),
            "skok_2": int(skok2),
            "skok_3": int(skok3),
            "skok_4": int(skok4),
            "skok_5": int(skok5),
            "najlepsi_skok": int(max(skok1, skok2, skok3, skok4, skok5))
        }
        zaznam_skokov.append(temp_slovnik)
    
    zoznam_krajin = {}
    for zaznam in zaznam_skokov:
        if zaznam["krajina"] not in zoznam_krajin:
            zoznam_krajin[zaznam["krajina"]] = 1
        else:
            zoznam_krajin[zaznam["krajina"]] += 1
    zoznam_krajin_str = (", ").join(list(zoznam_krajin.keys()))
    print(f"Zoznam zúčastnených krajín: {zoznam_krajin_str}.")
    for krajina, pocet in zoznam_krajin.items():
        print(f"Súťažiacich z {krajina} bolo {pocet}.")
    
    vitaz = max(zaznam_skokov, key = lambda zaznam: zaznam["najlepsi_skok"])
    print(f"Najlepším skokanom bol {vitaz["meno"]} a skočil {vitaz["najlepsi_skok"]} cm.")
    
subor = "Precvičovanie/Material_dudo/14. Skok do diaľky/skok_do_dialky.txt"
skok(subor)
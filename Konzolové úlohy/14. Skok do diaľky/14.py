def skok_do_dialky(subor):
    with open(subor, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    zaznam_skokov = []
    for riadok in nacitane_riadky:
        meno, kod_krajiny, vykon1, vykon2, vykon3, vykon4, vykon5 = riadok.split()
        riadok_slovnik = {
            "Meno": meno,
            "kod_krajiny": kod_krajiny,
            "vykon1": int(vykon1),
            "vykon2": int(vykon2),
            "vykon3": int(vykon3),
            "vykon4": int(vykon4),
            "vykon5": int(vykon5), 
            "najlepsi_vykon": int(max(vykon1, vykon2, vykon3, vykon4, vykon5))
        }
        zaznam_skokov.append(riadok_slovnik)
    
    pocty_krajin = {}
    for zaznam in zaznam_skokov:
        if zaznam["kod_krajiny"] not in pocty_krajin:
            pocty_krajin[zaznam["kod_krajiny"]] = 1
        else:
            pocty_krajin[zaznam["kod_krajiny"]] += 1
    nazvy_krajin_str = (", ").join(list(pocty_krajin.keys()))
    print(f"Názvy zúčastnených krajín: {nazvy_krajin_str}")
    for krajina, pocet in pocty_krajin.items():
        print(f"Krajina: {krajina}, Počet súťažiacich: {pocet}")
    
    vitaz = max(zaznam_skokov, key = lambda zaznam: zaznam["najlepsi_vykon"])
    for zaznam in zaznam_skokov:
        if zaznam["najlepsi_vykon"] == vitaz["najlepsi_vykon"]:
            print(f"Celkový víťaz je {zaznam["Meno"]} s výkonom {zaznam["najlepsi_vykon"]} cm.")
    
subor = "Precvičovanie/Material_dudo/14. Skok do diaľky/skok_do_dialky.txt"
skok_do_dialky(subor)
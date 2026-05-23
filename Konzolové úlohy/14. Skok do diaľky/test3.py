def skok(subor):
    with open(subor, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    zaznam_skokov = []
    for riadok in nacitane_riadky:
        meno, krajina, s1, s2, s3, s4, s5 = riadok.split()
        temp_slovnik = {
            "meno": meno,
            "krajina": krajina,
            "najlepsi_vykon": max(s1, s2, s3, s4, s5)
        }
        zaznam_skokov.append(temp_slovnik)
    
    krajiny_pocet = {}
    for zaznam in zaznam_skokov:
        if zaznam["krajina"] not in krajiny_pocet:
            krajiny_pocet[zaznam["krajina"]] = 1
        else:
            krajiny_pocet[zaznam["krajina"]] += 1
    
    krajiny_str = (", ").join([zaznam["krajina"] for zaznam in zaznam_skokov])
    print(f"Zoznam zúčastnených krajín: {krajiny_str}.")
    
    for krajina, pocet in krajiny_pocet.items():
        print(f"Z krajiny {krajina} sa zúčastnilo {pocet} športovcov.")
    
    vitaz = max(zaznam_skokov, key = lambda zaznam: zaznam["najlepsi_vykon"])
    for zaznam in zaznam_skokov:
        if zaznam["najlepsi_vykon"] == vitaz["najlepsi_vykon"]:
            print(f"Celkový víťaz je {zaznam["meno"]} so skokom {zaznam["najlepsi_vykon"]} cm.")
    
subor = "Precvičovanie/Material_dudo/14. Skok do diaľky/skok_do_dialky.txt"
skok(subor)
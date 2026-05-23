def mena(subor_vstup, subor_vystup):
    with open(subor_vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    list_mien = []
    for index in range(0, len(nacitane_riadky) // 2):
        temp_slovnik = {
            "meno": nacitane_riadky[index].strip(),
            "priezvisko": nacitane_riadky[index + len(nacitane_riadky) // 2].strip()
        }
        list_mien.append(temp_slovnik)
    
    print(f"Počet mien v súbore: {len(list_mien)}")
    
    najdlhsie_meno = max(list_mien, key = lambda cele_meno: len(cele_meno["meno"]))
    najdlhsie_priezvisko = max(list_mien, key = lambda cele_meno: len(cele_meno["priezvisko"]))
    print(f"Najdlhšie meno je: {najdlhsie_meno["meno"]}.")
    print(f"Najdlhšie priezvisko je: {najdlhsie_priezvisko["priezvisko"]}.")
    
    dlzka_najdlhsieho_mena = len(najdlhsie_meno["meno"]) + 4
    with open(subor_vystup, "w", encoding = "UTF-8") as fw:
        for riadok in list_mien:
            fw.write(f"{riadok["meno"]:<{dlzka_najdlhsieho_mena}}{riadok["priezvisko"] + "\n"}")
    
subor_vstup = "Precvičovanie/Material_dudo/16. Mená v stĺpcoch/mena_zamestnancov.txt"
subor_vystup = "Precvičovanie/Material_dudo/16. Mená v stĺpcoch/vystup.txt"
mena(subor_vstup, subor_vystup)
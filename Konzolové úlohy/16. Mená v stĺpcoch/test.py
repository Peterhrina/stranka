def mena(subor_vstup, subor_vystup):
    with open(subor_vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    mena_list = [riadok.strip() for riadok in nacitane_riadky[: len(nacitane_riadky) // 2]]
    priezviska_list = [riadok.strip() for riadok in nacitane_riadky[len(nacitane_riadky) // 2:]]
    
    print(f"Počet mien v súbore: {len(mena_list)}")
    
    najdlhsie_meno = max(mena_list, key = len)
    najdlhsie_priezvisko = max(priezviska_list, key = len)
    print(f"Najdlhšie meno: {najdlhsie_meno} \n"
        f"Najdlhšie priezvisko: {najdlhsie_priezvisko}")
    
    with open(subor_vystup, "w", encoding = "UTF-8") as fw:
        for index in range(0, len(mena_list)):
            fw.write(f"{mena_list[index]:<{len(najdlhsie_meno) + 4}}{priezviska_list[index]} \n")
    
subor_vstup = "Precvičovanie/Material_dudo/16. Mená v stĺpcoch/mena_zamestnancov.txt"
subor_vystup = "Precvičovanie/Material_dudo/16. Mená v stĺpcoch/vystup.txt"
mena(subor_vstup, subor_vystup)
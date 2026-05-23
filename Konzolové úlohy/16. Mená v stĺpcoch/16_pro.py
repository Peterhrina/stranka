def mena(subor_vstup, subor_vystup):
    with open(subor_vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    mena_list = [riadok.strip() for riadok in nacitane_riadky[:len(nacitane_riadky) // 2]]
    priezviska_list = [riadok.strip() for riadok in nacitane_riadky[len(nacitane_riadky) // 2:]]
    
    print(f"Počet mien v súbore: {len(mena_list)}")
    
    najdlhsie_meno = max(mena_list, key = lambda meno: len(meno))       #tu je jedno ci pouzijem riadok tento alebo
    najdlhsie_priezvisko = max(priezviska_list, key = len)              #tento riadok, do key sa dava funkcia a ak je
    print(f"Najdlhšie meno je: {najdlhsie_meno}")                       #zlozitejsia tak radsej cez lambdu
    print(f"Najdlhšie priezvisko je: {najdlhsie_priezvisko}")
    
    najdlhsie_meno_int = len(najdlhsie_meno) + 4
    with open(subor_vystup, "w", encoding = "UTF-8") as fr:
        for index in range(0, len(mena_list)):
            fr.write(f"{mena_list[index]:<{najdlhsie_meno_int}}{priezviska_list[index] + "\n"}")
    
subor_vstup = "Precvičovanie/Material_dudo/16. Mená v stĺpcoch/mena_zamestnancov.txt"
subor_vystup = "Precvičovanie/Material_dudo/16. Mená v stĺpcoch/vystup.txt"
mena(subor_vstup, subor_vystup)
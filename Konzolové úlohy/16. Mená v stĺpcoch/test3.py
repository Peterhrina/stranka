def mena(vstup, vystup):
    with open(vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    mena = [riadok.strip() for riadok in nacitane_riadky[:len(nacitane_riadky) // 2]]
    priezviska = [riadok.strip() for riadok in nacitane_riadky[len(nacitane_riadky) // 2:]]
    
    print(f"Počet mien v súbore: {len(mena)}")
    
    najdlhsie_meno = max(mena, key = lambda meno: len(meno))
    najdlhsie_priezvisko = max(priezviska, key = lambda priezvisko: len(priezvisko))
    print(f"Najdlhšie meno je {najdlhsie_meno} s dĺžkou {len(najdlhsie_meno)}.")
    print(f"Najdlhšie meno je {najdlhsie_priezvisko} s dĺžkou {len(najdlhsie_priezvisko)}.")
    
    with open(vystup, "w", encoding = "UTF-8") as fw:
        for meno, priezvisko in zip(mena, priezviska):
            fw.write(f"{meno:<{len(najdlhsie_meno) + 2}}{priezvisko} \n")
    
vstup = "Precvičovanie/Material_dudo/16. Mená v stĺpcoch/mena_zamestnancov.txt"
vystup = "Precvičovanie/Material_dudo/16. Mená v stĺpcoch/vystup.txt"
mena(vstup, vystup)
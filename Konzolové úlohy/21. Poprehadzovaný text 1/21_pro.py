import random as r
def a(vs, vy):
    with open(vs, "r", encoding = "UTF-8")as fr:
        riadky = fr.readlines()
    
    vysledok = []
    for riadok in riadky:
        print(("").join(riadok.strip()))
        
        temp_riadok = []
        for slovo in riadok.split():
            prehadzovanie = list(slovo[1:-1])
            r.shuffle(prehadzovanie)
            temp_riadok.append(f"{slovo[0]}{("").join(prehadzovanie)}{slovo[-1]}")
        vysledok.append(temp_riadok)
    
    print("-" * 25)
    with open(vy, "w", encoding = "UTF-8")as fw:
        for riadok in vysledok:
            print(f"{(" ").join(riadok)}")
            fw.write(f"{(" ").join(riadok)}{"\n"}")
    
    
vstup = "Precvičovanie/Material_dudo/21. Poprehadzovaný text 1/poprehadzovany_text1_vstup.txt"
vystup = "Precvičovanie/Material_dudo/21. Poprehadzovaný text 1/vysledok.txt"
a(vstup, vystup)
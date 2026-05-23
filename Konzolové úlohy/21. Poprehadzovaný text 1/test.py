import random as rd

def text(vs, vy):
    with open(vs, "r", encoding = "UTF-8")as fr:
        nacitane_riadky = fr.readlines()
    
    vysledok = []
    for riadok in nacitane_riadky:
        print(riadok.strip())
        
        temp_riadok = []
        for slovo in riadok.split():
            if len(slovo) <= 3:
                temp_riadok.append(slovo)
            else:
                slovo_stred = list(slovo[1:-1])
                rd.shuffle(slovo_stred)
                temp_slovo = f"{slovo[0]}{("").join(slovo_stred)}{slovo[-1]}"
                temp_riadok.append(temp_slovo)
        vysledok.append(temp_riadok)
    
    print("-" * 25)
    
    with open(vy, "w", encoding = "UTF-8")as fw:
        for riadok in vysledok:
            print(f"{(" ").join(riadok)}")
            fw.write(f"{(" ").join(riadok)}{"\n"}")
    
vs = "Precvičovanie/Material_dudo/21. Poprehadzovaný text 1/poprehadzovany_text1_vstup.txt"
vy = "Precvičovanie/Material_dudo/21. Poprehadzovaný text 1/vysledok.txt"
text(vs, vy)
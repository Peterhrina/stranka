import random as rd

def a(vs, vy):
    with open(vs, "r", encoding = "UTF-8")as fr:
        riadky = fr.readlines()
    
    vysledok = []
    for riadok in riadky:
        print(riadok.strip())
        
        temp_riadok = []
        for slovo in riadok.split():
            if slovo.isalpha():
                if len(slovo) <= 3:
                    temp_riadok.append(slovo)
                else:
                    stred = list(slovo[1:-1])
                    rd.shuffle(stred)
                    temp_riadok.append(f"{slovo[0]}{("").join(stred)}{slovo[-1]}")
            else:
                if len(slovo) <= 4:
                    temp_riadok.append(slovo)
                else:
                    stred = list(slovo[1:-2])
                    rd.shuffle(stred)
                    temp_riadok.append(f"{slovo[0]}{("").join(stred)}{slovo[-2:]}")
        vysledok.append(temp_riadok)
    
    print("-" * 25)
    
    with open(vy, "w", encoding = "UTF-8")as fw:
        for riadok in vysledok:
            print(f"{(" ").join(riadok)}")
            fw.write(f"{(" ").join(riadok)}{"\n"}")

vs = "Precvičovanie/Material_dudo/22. Poprehadzovaný text 2/poprehadzovany_text_vstup2.txt"
vy = "Precvičovanie/Material_dudo/22. Poprehadzovaný text 2/poprehadzovany_text.txt"
a(vs, vy)
import random as r
def a(vs, vy):
    with open(vs, "r", encoding = "UTF-8")as fr:
        riadky = fr.readlines()
    
    vysledok = []
    for riadok in riadky:
        print(riadok.strip())
        
        temp_riadok = []
        for slovo in riadok.split():
            if slovo.isalpha():
                zamiesaj = list(slovo[1:-1])
                r.shuffle(zamiesaj)
                temp_riadok.append(f"{slovo[0]}{("").join(zamiesaj)}{slovo[-1]}")
            else:
                zamiesaj = list(slovo[1:-2])
                r.shuffle(zamiesaj)
                temp_riadok.append(f"{slovo[0]}{("").join(zamiesaj)}{slovo[-2:]}")
        vysledok.append(temp_riadok)
    
    print("-" * 25)
    with open(vy, "w", encoding = "UTF-8")as fw:
        for riadok in vysledok:
            print(f"{(" ").join(riadok)}")
            fw.write(f"{(" ").join(riadok)}{"\n"}")

vstup = "Precvičovanie/Material_dudo/22. Poprehadzovaný text 2/poprehadzovany_text_vstup2.txt"
vystup = "Precvičovanie/Material_dudo/22. Poprehadzovaný text 2/poprehadzovany_text.txt"
a(vstup, vystup)
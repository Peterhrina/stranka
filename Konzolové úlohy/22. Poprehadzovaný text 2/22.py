import random
def text(vstup, vystup):
    with open(vstup, "r", encoding = "UTF-8")as fr:
        riadky = fr.readlines()
    
    vysledok = []
    
    for riadok in riadky:
        print(riadok.strip())
        temp_riadok = []
        
        for slovo in riadok.split():
            
            if slovo.isalpha():
                temp_slovo = list(slovo[1:-1])
                random.shuffle(temp_slovo)
                temp_riadok.append(f"{slovo[:1]}{("").join(temp_slovo)}{slovo[-1:]}")
            
            else:
                temp_slovo = list(slovo[1:-2])
                random.shuffle(temp_slovo)
                temp_riadok.append(f"{slovo[:1]}{("").join(temp_slovo)}{slovo[-2:]}")

        vysledok.append(temp_riadok)
    
    print("-" * 25)
    
    with open(vystup, "w", encoding = "UTF-8")as fw:
        for riadok in vysledok:
            fw.write(f"{(" ").join(riadok)}{"\n"}")
            print((" ").join(riadok))


vstup = "Precvičovanie/Material_dudo/22. Poprehadzovaný text 2/poprehadzovany_text_vstup2.txt"
vystup = "Precvičovanie/Material_dudo/22. Poprehadzovaný text 2/poprehadzovany_text.txt"
text(vstup, vystup)
import random
def prehadzovanie(vstup, vystup):
    with open(vstup, "r", encoding = "UTF-8")as fr:
        riadky = fr.readlines()
    
    slova = []
    for riadok in riadky:
        print(riadok.strip())
        slova.append(riadok.strip().split())
    
    print(f"-" * 25)
    
    vysledok = []
    for riadok in slova:
        riadok_list = []
        for slovicko in riadok:
            temp = [pismenko for pismenko in slovicko[1:-1]]
            random.shuffle(temp)
            hotovo = slovicko[0] + ("").join(temp) + slovicko[-1]
            riadok_list.append(hotovo)
        vysledok.append(riadok_list)
    
    with open(vystup, "w", encoding = "UTF-8") as fw:
        for riadok in vysledok:
            print(f"{(" ").join(riadok)}")
            fw.write(f"{(" ").join(riadok)}{"\n"}")

vstup = "Precvičovanie/Material_dudo/21. Poprehadzovaný text 1/poprehadzovany_text1_vstup.txt"
vystup = "Precvičovanie/Material_dudo/21. Poprehadzovaný text 1/vysledok.txt"
prehadzovanie(vstup, vystup)
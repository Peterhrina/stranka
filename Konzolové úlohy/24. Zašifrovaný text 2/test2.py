import random as rd

def menic(znak, posun):
    if "a" <= znak <= "z":
        stary_index = ord(znak) - ord("a") + 1
        novy_index = (stary_index + posun) % 26
        novy_znak = chr(novy_index + ord("a"))
        return novy_znak
    elif "A" <= znak <= "Z":
        stary_index = ord(znak) - ord("A") + 1
        novy_index = (stary_index + posun) % 26
        novy_znak = chr(novy_index + ord("A"))
        return novy_znak
    else:
        return znak

def sifrovat(nacitane_riadky):
    vysledok = []
    for riadok in nacitane_riadky:
        posun = rd.randrange(1, 26)
        temp_riadok = []
        kluc = chr(posun + ord("a"))
        temp_riadok.append(kluc)
        
        for znak in riadok:
            novy_znak = menic(znak, posun)
            temp_riadok.append(novy_znak)
        vysledok.append(("").join(temp_riadok))
    return vysledok

def desifrovat(nacitane_riadky):
    vysledok = []  
    for riadok in nacitane_riadky:
        posun = -(ord(riadok[0]) - ord("a") + 2)
        
        temp_riadok = []
        for znak in riadok[1:]:
            novy_znak = menic(znak, posun)
            temp_riadok.append(novy_znak)
        vysledok.append(("").join(temp_riadok))
    return vysledok

def citaj(vstup):
    with open(vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
        return nacitane_riadky

def pis(vystup, riadky):
    with open(vystup, "w", encoding = "UTF-8") as fw:
        for riadok in riadky:
            fw.write(riadok)
        print("Zapísané")


co = input("Napíš 1 pre šifrovanie, 2 pre dešifrovanie: ")

if co == "1":
    riadky = citaj("Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/vstupny_text.txt")
    zasifrovane = sifrovat(riadky)
    pis("Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/vystupny_text.txt", zasifrovane)
    
elif co == "2":
    riadky = citaj("Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/zasifrovany_text_2.txt")
    desifrovane = desifrovat(riadky)
    pis("Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/vystupny_text.txt", desifrovane)
    
else:
    print("Napíš buď 1 alebo 2!")
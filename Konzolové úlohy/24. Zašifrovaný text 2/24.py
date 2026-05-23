import random as rd

def dekodac(riadky: list[str]) -> list[str]:
    """ Teraz si zistím podľa prvého písmenka, o koľko sa posúvalo. """
    
    vysledok: list[str] = []
    for riadok in riadky:
        prve_pismenko: str = riadok[0][0]
        posun: int = - (ord(prve_pismenko) - ord("a") + 1)
        temp_riadok: list[str] = []
        
        for pismenko in riadok.strip()[1:]:
            temp_riadok.append(posun_pismenko(pismenko, posun))
            
        vysledok.append(("").join(temp_riadok) + "\n")
        
    return vysledok

def posun_pismenko(pismenko: str, posun: int) -> str:
    if "a" <= pismenko <= "z":
        pismenko_index: int = ord(pismenko) - ord("a")
        novy_index: int = (pismenko_index + posun) % 26
        nove_pismenko: str = chr(novy_index + ord("a"))
        return nove_pismenko
    elif "A" <= pismenko <= "Z":
        pismenko_index: int = ord(pismenko) - ord("A")
        novy_index: int = (pismenko_index + posun) % 26
        nove_pismenko: str = chr(novy_index + ord("A"))
        return nove_pismenko
    else: #ak to nie je pismenko
        return pismenko

def sifrovac(riadky: list[str]) -> list[str]:
    vysledok: list[str] = []
    for riadok in riadky:
        temp_riadok: list[str] = []
        posun: int = rd.randrange(1, 26)
        temp_riadok.append(chr(posun - 1 + ord("a"))) # Klučové prvé písmenko.
        
        for pismenko in riadok:
            temp_riadok.append(posun_pismenko(pismenko, posun))
            
        vysledok.append(("").join(temp_riadok))
        
    return vysledok

def main():
    vstupny_subor_na_sifrovanie: list[str] = "Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/vstupny_text.txt"
    vstupny_subor_na_desifrovanie: list[str] = "Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/zasifrovany_text_2.txt"
    vystupny_subor = "Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/vystupny_text.txt"
    
    try:
        volba: str = input("Napíš '1' pre šifrovanie alebo '2' pre dešifrovanie: ")
        
        if volba == "1":
            
            with open(vstupny_subor_na_sifrovanie, "r", encoding= "UTF-8")as fr:
                riadky: list[str] = fr.readlines()
                print("Zašifrovaný text bol načítaný zo súboru:", vstupny_subor_na_sifrovanie)
                
            with open(vystupny_subor, "w", encoding= "UTF-8") as fw:
                for riadok in sifrovac(riadky):
                    fw.write(riadok)
                print("Zašifrovaný text bol uložený do súboru:", vystupny_subor)
        
        elif volba == "2":
            
            with open(vstupny_subor_na_desifrovanie, "r", encoding= "UTF-8")as fr:
                riadky: list[str] = fr.readlines()
                print("Dešifrovaný text bol načítaný zo súboru:", vstupny_subor_na_desifrovanie)
                
            with open(vystupny_subor, "w", encoding= "UTF-8") as fw:
                for riadok in dekodac(riadky):
                    fw.write(riadok)
                print("Dešifrovaný text bol uložený do súboru:", vystupny_subor)
        else:
            print("Neplatná voľba.")
    except FileNotFoundError:
        print("Súbor nebol nájdený.")
    
if __name__ == "__main__":
    main()
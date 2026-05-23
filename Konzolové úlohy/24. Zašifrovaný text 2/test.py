""" NEFUNKČNÉ!!! """
import random as rd

def sifrovac(vstup: list[str]) -> list[str]:
    vysledok: list[str] = []
    for riadok in vstup:
        temp_riadok: list[str] = []
        posun: int = rd.randrange(1, 26)
        
        kluc_zakodovania: str = chr(posun + ord("a"))
        temp_riadok.append(kluc_zakodovania)
        for znak in riadok:
            zasifrovany_znak: str = posun_pismenka(znak, posun)
            temp_riadok.append(zasifrovany_znak)
        
        vysledok.append(temp_riadok)
    
    return "".join(vysledok)

def dekodovac(vstup: list[str]) -> list[str]:
    vysledok: list[str] = []
    
    for riadok in vstup:
        temp_riadok: list[str] = []
        posun: int = - (ord(riadok[0][0]) - ord("a") + 1)
        
        for znak in riadok[1:]:
            desifrovany_znak: str = posun_pismenka(znak, posun)
            temp_riadok.append(desifrovany_znak)
        
        vysledok.append(temp_riadok)
    
    return "".join(vysledok)

def posun_pismenka(znak: str, posun: int):
    zaciatok_malej_abecedy: int = ord("a")
    zaciatok_velkej_abecedy: int = ord("A")
    
    if "a" <= znak <= "z":
        stary_index: int = ord(znak) - zaciatok_malej_abecedy 
        novy_index: int = (stary_index + posun) % 26
        nove_pismenko: str = chr(novy_index)
        return nove_pismenko
    
    elif "A" <= znak <= "Z":
        stary_index: int = ord(znak) - zaciatok_velkej_abecedy
        novy_index: int = (stary_index + posun) % 26
        nove_pismenko: str = chr(novy_index)
        return nove_pismenko
    
    else:
        return znak

def main() -> None:
    vstupny_subor_na_sifrovanie: list[str] = "Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/vstupny_text.txt"
    vstupny_subor_na_desifrovanie: list[str] = "Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/zasifrovany_text_2.txt"
    vystupny_subor = "Škola-hodiny/Precvičovanie/Material_dudo/24. Zašifrovaný text 2/vystupny_text.txt"
    
    vyber_input: str = input("Napíš '1' pre šifrovanie alebo '2' pre dešifrovanie: ")
    
    def otvor(vstup: str) -> list[str] | None:
        try:
            with open(vstup, "r", encoding = "UTF-8")as fr:
                nacitany_subor = fr.readlines()
                print("Súbor úspešne zašifrovaný!")
                
                if nacitany_subor is None:
                    print("Súbor na čítanie je prázdny")
                    return
                
                return nacitany_subor
        except FileNotFoundError:
            print("CHYBA! Súbor na čítanie neexistuje?")
            return
    
    def pisanie(subor: str, vysledok: list[str]):
        try:
            with open(subor, "w", encoding = "UTF-8")as fw:
                for riadok in vysledok:
                    fw.write(riadok + "\n")
                    print("Súbor úspešne dešifrovaný!")
        except FileExistsError:
            print("CHYBA! Súbor na písanie neexistuje?")
            return
        
    if vyber_input == "1":
        nacitany_subor = otvor(vstupny_subor_na_sifrovanie)
        ...
    elif vyber_input == "2":
        nacitany_subor = otvor(vstupny_subor_na_desifrovanie)
        ...
    else:
        print("CHYBA! Napíš buď '1' alebo '2'! Nič iné!")

if __name__ == "__main__":
    main()
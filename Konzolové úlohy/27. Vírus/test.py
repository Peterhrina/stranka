import random

subor_citanie: str = "Škola-hodiny/Precvičovanie/Material_dudo/27. Vírus/virus.txt"
subor_pisanie: str = "Škola-hodiny/Precvičovanie/Material_dudo/27. Vírus/vystup.txt"

def anonie() -> bool:
    return random.choice([True, False])

def otvorenie(vstup: str) -> list[str]:
    with open(vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    print(f"Správne som otvoril a prečítal súbor.")
    return nacitane_riadky

def virusovanie(nacitane_riadky: list[str]) -> list[str]:
    vysledok: list[str] = []
    
    if anonie(): # Zmeň poradie riadkov
        random.shuffle(nacitane_riadky)
    
    for riadok in nacitane_riadky:
        riadok_temp: list[str] = []
        
        if anonie(): # Zamieša slová v riadku
            random.shuffle(riadok.split())
        
        for slovo in riadok.split():
            if anonie():
                slovo:str = slovo[::-1]
            riadok_temp.append(slovo)
        vysledok.append((" ").join(riadok_temp))
    print(f"Zavírusoval som súbor.")
    return vysledok

def zapis(vysledok: list[str], vystup: str) -> None:
    with open(vystup, "w", encoding = "UTF-8") as fw:
        for riadok in vysledok:
            fw.write(riadok + "\n")
    print(f"Správne som zapísal výsledok.")

if __name__ == "__main__":
    nacitane_riadky: list[str] = otvorenie(subor_citanie)
    vysledok: list[str] = virusovanie(nacitane_riadky)
    zapis(vysledok, subor_pisanie)
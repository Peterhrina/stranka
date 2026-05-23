import random as rd

vstup: str = "Škola-hodiny/Precvičovanie/Material_dudo/27. Vírus/virus.txt"
vystup: str = "Škola-hodiny/Precvičovanie/Material_dudo/27. Vírus/vystup.txt"

def anonie() -> bool:
    return rd.choice([True, False])

def virusovanie(nacitane_riadky: list[str]) -> list[str]:
    if anonie():
        rd.shuffle(nacitane_riadky)
        print(f"Mením poradie riadkov.")
    
    vysledok: list = []
    
    for riadok in nacitane_riadky:
        temp_riadok: list = []
        riadok: list[str] = riadok.split()
        if anonie():
            rd.shuffle(riadok)
        for slovo in riadok:
            if anonie():
                slovo: str = slovo[::-1]
            temp_riadok.append(slovo)
        vysledok.append(" ".join(temp_riadok))
    print(f"Zavírusoval som riadky.")
    return vysledok

def otvorenie(vstup: str) -> list[str]:
    with open(vstup, "r")as fr:
        riadky = fr.readlines()
    print("Prečítal som vstupný súbor.")
    return riadky

def zapis(vystup: str, riadky: list[str]) -> None:
    with open(vystup, "w") as fw:
        for riadok in riadky:
            fw.write(riadok + "\n")
    print("Zapísal som výstupný súbor.")

if __name__ == "__main__":
    nacitane_riadky: list[str] = otvorenie(vstup)
    vysledok: list[str] = virusovanie(nacitane_riadky)
    zapis(vystup, vysledok)
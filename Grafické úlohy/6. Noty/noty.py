import tkinter as tki
vstup = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/6. Noty/noty.txt"

def otvorenie(vstup:str ) -> list[str]:
    with open(vstup, "r", encoding = "UTF-8")as fr:
        vystup: list[str] = fr.readlines()
        return vystup

def menic_not(noty: list[str]) -> list[int]:
    hodnotova_tabulka: dict[str: int] = {
        "c": 15,
        "d": 10,
        "e": 5,
        "f": 0,
        "g": -5,
        "a": -10,
        "h": -15
    }
    vysledok: list = []
    for riadok in noty:
        for znak in riadok.strip():
            vysledok.append(hodnotova_tabulka[znak])
    return vysledok

def kreslic_riadkov(premenene_noty: list[int]) -> list[list[int]]:
    kolko_riadkov: int = len(premenene_noty) // 15
    vysky_riadkov: list[int] = []
    
    for CISLO in range(1, kolko_riadkov + 2):
        y = Y + (100 * CISLO)
        
        temp: list[int] = []
        for cislo in range(1, 6):
            y_kolko = y + (10 * cislo)
            canvas.create_line(
                0, y_kolko,
                SIRKA, y_kolko,
                width = 2, fill = "black"
            )
            temp.append(y_kolko)
        
        vysky_riadkov.append(temp)
    return vysky_riadkov

def kreslic_not(premenene_noty: list[int], vysky_riadkov: list[list[int]]):
    for index, RIADOK in enumerate(vysky_riadkov):
        x = X
        y = RIADOK[0] + 30
        
        for pozicia, nota in enumerate(premenene_noty[index * 15: (index + 1) * 15]):
            canvas.create_oval(
                x + (20 * pozicia), y + nota,
                x + 10 + (20 * pozicia), y + 10 + nota
            )

noty = otvorenie(vstup)
premenene_noty = menic_not(noty)
SIRKA = 500
VYSKA = 500
X = 10
Y = -50

root = tki.Tk()
canvas = tki.Canvas(width = SIRKA, height = VYSKA, background = "grey")
canvas.pack()

vysky_riadkov = kreslic_riadkov(premenene_noty)
kreslic_not(premenene_noty, vysky_riadkov)
print(premenene_noty)


root.mainloop()
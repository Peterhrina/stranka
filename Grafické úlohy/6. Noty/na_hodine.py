import tkinter as tk

# KONŠTANTY
SUBOR = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/6. Noty/noty.txt"
VYSKA_NOTY = 10
SIRKA_NOTY = 25
MEDZERA = 1 * SIRKA_NOTY
VZDIALENOST_OSNOV = 3 * VYSKA_NOTY
SIRKA = 800
VYSKA = 600
OFFSET = {
    "c": 0,
    "d": 0.5,
    "e": 1,
    "f": 1.5,
    "g": 2,
    "a": 2.5,
    "h": 3
}

def otvorenie(vstup:str ) -> list[str]:
    with open(vstup, "r", encoding = "UTF-8")as fr:
        vystup: str = fr.read().strip()
        return vystup

def pocet_osnov(noty_list: str):
    pocet_osnov = len(noty_list) / (SIRKA / (SIRKA_NOTY + MEDZERA))
    

noty_list: str = otvorenie(SUBOR)
pocet_osnov(noty_list)


# root = tk.Tk()
# canvas = tk.Canvas(width = SIRKA, height = VYSKA, background = "grey")
# canvas.pack()

# root.mainloop()
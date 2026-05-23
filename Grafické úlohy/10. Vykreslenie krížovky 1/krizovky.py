import tkinter as tk

#KONŠTANTY
SIRKA = 1000
VYSKA = 400
ZACIATOK_X = 40
ZACIATOK_Y = 40
STRED_SIVYCH = 240
VSTUP = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/10. Vykreslenie krížovky 1/krizovka1-1.txt"

class Slovo():
    def __init__(self, canvas, slovo: str, pozicia: int):
        self.canvas = canvas
        self.slovo = slovo
        self.pozicia = pozicia - 1
    
    def vykreslovanie(self, x: int, y: int, zobrazit_text: bool):
        for idx, pismenko in enumerate(self.slovo):
            vnutro = "grey" if idx == self.pozicia else "white"
            
            id_box: int = self.canvas.create_rectangle(
                x + (40 * idx), y,
                x + 40 + (40 * idx), y + 40,
                fill=vnutro, outline="black"
            )
            
            if zobrazit_text:
                x1, y1, x2, y2 = self.canvas.coords(id_box)
                stred_x = (x1 + x2) / 2
                stred_y = (y1 + y2) / 2
            
                self.canvas.create_text(
                    stred_x, stred_y,
                    text=pismenko, font=("Arial", 10), fill="black"
                )

class Hra():
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(
            width=SIRKA, height=VYSKA,
            background="light grey"
        )
        self.canvas.pack()
        
        self.slova: list[str] = list()
        self.nacitanie_slov()
        self.vytvorenie_krizovky()
    
    def nacitanie_slov(self):
        with open(VSTUP, "r", encoding="utf-8")as fr:
            self.slova = fr.readlines()
    
    def vytvorenie_krizovky(self):
        for idx, riadok in enumerate(self.slova):
            casti: list[str] = riadok.strip().split()
            cislo: int = int(casti[0])
            slovo: str = casti[1]
            pozicia_v_slove: int = cislo - 1
            
            slovo: str = riadok[2:].strip()
            
            x: int = STRED_SIVYCH - (pozicia_v_slove * 40)
            y: int = ZACIATOK_Y + (40 * idx)
            
            na_spracovanie = Slovo(self.canvas, slovo, cislo)
            na_spracovanie.vykreslovanie(x, y, True)
            na_spracovanie.vykreslovanie(x + SIRKA // 2, y, False)

if __name__ == "__main__":
    root = tk.Tk()
    hra = Hra(root)
    root.mainloop()
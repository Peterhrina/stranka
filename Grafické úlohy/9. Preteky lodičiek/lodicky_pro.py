import tkinter as tk
import random as rd

# KONŠTANTY
SIRKA = 700
VYSKA = 800
ZACIATOK_LODICIEK = (50, 50)
POCET_LODICIEK = 15
RYCHLOST_LODIEK = 100

class Lodicka:
    def __init__(self, canvas, x, y, cislo):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.cislo = cislo 
        
        # Nakreslíme sa a uložíme si ID-čka
        # Plachta
        self.id_ciara = self.canvas.create_line(
            x, y, x, y-25, x+10, y-10, x, y-5, 
            fill="black", tags=f"lodka_{cislo}"
        )
        # Telo lode
        self.id_spodok = self.canvas.create_polygon(
            x-20, y, x+20, y, x+10, y+8, x-10, y+8, 
            fill="black", tags=f"lodka_{cislo}"
        )

    def plavaj(self):
        # 1. Posun o náhodný kus dopredu
        posun = rd.randint(1, 10)
        self.x += posun
        
        # Metóda move() posunie existujúci objekt o dx, dy
        self.canvas.move(self.id_ciara, posun, 0)
        self.canvas.move(self.id_spodok, posun, 0)
        
        # 2. Zmena tvaru plachty (animácia bez mazania)
        plachta = rd.randint(-3, 3)
        
        # coords() zmení súradnice existujúceho objektu
        # Pozor: musíme zadať ABSOLÚTNE súradnice
        self.canvas.coords(
            self.id_ciara, 
            self.x, self.y,           # Bod 1
            self.x, self.y-25,        # Bod 2
            self.x+10+plachta, self.y-10, # Špička plachty (tu je tá zmena)
            self.x, self.y-5          # Bod 4
        )

class Hra:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
        self.canvas.pack()
        
        self.lodicky = [] 
        self.ciel_x = SIRKA - 100
        
        self.vykresli_ciel()
        self.priprav_preteky()
        self.posuvanie()

    def vykresli_ciel(self):
        self.canvas.create_line(self.ciel_x, 0, self.ciel_x, VYSKA, fill="red", width=3)

    def priprav_preteky(self):
        start_x, start_y = ZACIATOK_LODICIEK
        for i in range(POCET_LODICIEK):
            # Vytvoríme inštanciu triedy Lodicka pre každú loď
            nova_lodka = Lodicka(self.canvas, start_x, start_y + i*50, i)
            self.lodicky.append(nova_lodka)

    def posuvanie(self):
        # Pohneme každou lodičkou
        for lodka in self.lodicky:
            lodka.plavaj()
            
        # Skontrolujeme, či niekto vyhral
        # (Zistíme čísla lodiek, ktorých x je za cieľom)
        vitazi = [lodka.cislo for lodka in self.lodicky if lodka.x >= self.ciel_x]
        
        if vitazi:
            self.koniec(vitazi)
        else:
            self.root.after(RYCHLOST_LODIEK, self.posuvanie)

    def koniec(self, vitazi):
        text_vitazi = ", ".join(map(str, vitazi))
        self.canvas.create_text(
            SIRKA // 2, VYSKA // 2,
            text=f"Víťazmi sú lodičky číslo: {text_vitazi}",
            font=("Arial", 15, "bold"), fill="red" 
        )

# Spustenie
if __name__ == "__main__":
    root = tk.Tk()
    hra = Hra(root)
    root.mainloop()

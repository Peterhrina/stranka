import tkinter as tk
import random as rd

# Konštanty na začiatok
SIRKA = 1000
VYSKA = 200
PISMENA_TANIEROV = "ABCDEFGHIJ"

class Tanier:
    def __init__(self, pismenko, je_puknuty):
        self.pismenko = pismenko
        self.je_puknuty = je_puknuty

class Hra:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="grey")
        self.canvas.pack()
        
        self.taniere = []
        self.mapa_id_na_letter = {}
        self.kliknute_pismena = set()
        self.puknute_pismenko = ""
        
        self.priprav_hru()
        self.vykresli_hru()
        
        # Bindovanie priamo na canvas metódu triedy
        self.canvas.bind("<Button-1>", self.klik)

    def priprav_hru(self):
        idx_puknuteho = rd.randrange(len(PISMENA_TANIEROV))
        
        for idx, znak in enumerate(PISMENA_TANIEROV):
            je_puknuty = (idx == idx_puknuteho)
            if je_puknuty:
                self.puknute_pismenko = znak
            self.taniere.append(Tanier(znak, je_puknuty))

    def vykresli_hru(self):
        for idx, tanier in enumerate(self.taniere):
            x = 1 + 100 * idx
            
            oval_id = self.canvas.create_oval(
                x, VYSKA // 2 - 40,
                x + 90, VYSKA // 2 + 40,
                fill="blue", outline="black", width=3
            )
            
            stred_x = x + 45
            stred_y = VYSKA // 2
            self.canvas.create_text(stred_x, stred_y, text=tanier.pismenko, font=("Arial", 40, "bold"))
            
            # Ulozenie ID pre detekciu kliknutia
            self.mapa_id_na_letter[oval_id] = tanier.pismenko

    def klik(self, event):
        # Nájdi všetky objekty pod kurzorom
        nalez = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        
        for objekt_id in nalez:
            if objekt_id in self.mapa_id_na_letter:
                pismenko = self.mapa_id_na_letter[objekt_id]
                self.skontroluj_tah(pismenko)
                return

    def skontroluj_tah(self, pismeno):
        if pismeno == self.puknute_pismenko:
            self.koniec_hry(pismeno)
        else:
            self.kliknute_pismena.add(pismeno)

    def koniec_hry(self, vitazne_pismeno):
        self.canvas.delete("all")
        self.canvas.create_text(SIRKA // 2, VYSKA // 2 - 20,
            text=f"Gratulujeme! Puknutý tanier bol: {vitazne_pismeno}",
            font=("Arial", 20, "bold"), fill="blue")
        
        sprava_minute = ", ".join(sorted(self.kliknute_pismena))
        self.canvas.create_text(SIRKA // 2, VYSKA // 2 + 30,
            text=f"Predtým si klikol na: {sprava_minute}",
            font=("Arial", 15, "bold"), fill="red")

# Spustenie
root = tk.Tk()
hra = Hra(root)
root.mainloop()
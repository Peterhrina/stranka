import tkinter as tk
import random as rd

SIRKA = 800
VYSKA = 800
POCET_JABLK = 20
RYCHLOST = 50
RYCHLOST_POHYBU = 20
VELKOST_GULIEK = 50
ZACIATOCNA_POZICIA_ZRUTA = 0, 50

class Zrut():
    def __init__(self, canvas: tk.Canvas, pozicia: tuple):
        self.canvas = canvas
        self.pozicia = pozicia
        
        self.dx: int = RYCHLOST_POHYBU
        self.dy: int = 0
        self.id_zruta: int = 0
    
    def vykreslenie(self):
        x, y = self.pozicia
        self.id_zruta = self.canvas.create_oval(
            x, y,
            x + VELKOST_GULIEK, y + VELKOST_GULIEK,
            fill="blue"
        )
    
    def zmena_smeru(self, event):
        klaves = event.keysym.lower()
        
        if klaves == "w":
            self.dx, self.dy = 0, -RYCHLOST_POHYBU
        elif klaves == "a":
            self.dx, self.dy = -RYCHLOST_POHYBU, 0
        elif klaves == "s":
            self.dx, self.dy = 0, RYCHLOST_POHYBU
        elif klaves == "d":
            self.dx, self.dy = RYCHLOST_POHYBU, 0
    
    def krok(self):
        self.canvas.move(self.id_zruta, self.dx, self.dy)

class Jablko():
    def __init__(self, canvas: tk.Canvas, cislo: int, pozicia: tuple):
        self.canvas = canvas
        self.cislo = cislo
        self.pozicia = pozicia
    
    def vykreslenie(self) -> int:
        x, y = self.pozicia
        id_jablka = self.canvas.create_oval(
            x, y,
            x + VELKOST_GULIEK, y + VELKOST_GULIEK,
            fill="red"
        )
        return id_jablka

class Hra():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.canvas = tk.Canvas(
            width=SIRKA, height=VYSKA,
            background="grey"
        )
        self.canvas.pack()
        
        # Premenné
        self.pozicie_jablk: dict[tuple] = {}
        
        # Zavolanie potrebného
        self.zrut = Zrut(self.canvas, ZACIATOCNA_POZICIA_ZRUTA)
        self.zrut.vykreslenie()
        self.logika_vykreslovania_jablk()
        self.logika()
        
        # Zviazanie klávesnice
        self.root.bind_all("<Key>", self.zrut.zmena_smeru)
    
    def generovanie_pozicii(self) -> tuple:
        x: int = rd.randint(0, SIRKA - VELKOST_GULIEK)
        y: int = rd.randint(0, VYSKA - VELKOST_GULIEK)
        return x, y
    
    def logika_vykreslovania_jablk(self):
        for cislo in range(POCET_JABLK):
            i = True
            while i:
                x, y = self.generovanie_pozicii()
                
                if x >= VELKOST_GULIEK or y >= VELKOST_GULIEK:
                    pozicia = x, y
                    jablko = Jablko(self.canvas, cislo, pozicia)
                    id_jablka = jablko.vykreslenie()
                    self.pozicie_jablk.pop(id_jablka, None)
                    print(f"Vykreslil som jablko s id {id_jablka}.")
                    i = False
    
    def logika(self):
        self.zrut.krok()
        
        pozicia_zruta = self.canvas.bbox(self.zrut.id_zruta)
        kolizie = self.canvas.find_overlapping(*pozicia_zruta)
        
        for objekt_id in kolizie:
            
            if objekt_id != self.zrut.id_zruta:
                self.canvas.delete(objekt_id)
                self.pozicie_jablk.pop(objekt_id, None)
                print(f"Zjedol som jablko {objekt_id}!")
        
        self.root.after(RYCHLOST, self.logika)

if __name__ == "__main__":
    root = tk.Tk()
    hra = Hra(root)
    root.mainloop()
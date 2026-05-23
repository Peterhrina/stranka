import tkinter as tk

SIRKA=600
VYSKA=700
VSTUP_MIEN = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/64. Zasadací poriadok/zasadaci_poriadok.csv"

class Lavica():
    def __init__(self, canvas: tk.Canvas, meno: str):
        self.canvas = canvas
        self.meno = meno

    def vykreslenie(self):
        lavica = self.canvas.create_rectangle(
            
        )

class Hra():
    def __init__(self, root: tk.Tk, vstup_mien: str):
        self.vstup_mien = vstup_mien
        self.spracovane_mena = self.spracovanie_mien(vstup_mien)
        self.root = root
        self.canvas = tk.Canvas(self.root,
            width=SIRKA, height=VYSKA,
            background="white"
        )
        self.canvas.pack()
        
        self.tlacidla()
    
    def tlacidla(self):
        tk.Label(self.root,
            text="Počet radov:"
        ).pack()
        
        self.entry_radov = tk.Entry(self.root)
        self.entry_radov.pack()
        
        tk.Label(self.root,
                text="Lavíc v rade:"
            ).pack()
        
        self.entry_lavic = tk.Entry(self.root)
        self.entry_lavic.pack()
        
        tk.Button(self.root,
                text="Potvrď vstup",
                command=self.potvrd
            ).pack()
    
    def potvrd(self):
        hodnota_radov = self.entry_radov.get()
        hodnota_lavic = self.entry_lavic.get()
        
        try:
            hodnota_radov = int(hodnota_radov)
            hodnota_lavic = int(hodnota_lavic)
            
            
        
        except ValueError:
            print("Nie sú to čísla.")
    
    def spracovanie_mien(self, vstup_mien):
        with open(vstup_mien, "r", encoding="windows-1250") as fr:
            nacitanie_riadky = fr.readlines()
        
        spracovane_mena = [riadok.split(";") for riadok in nacitanie_riadky]
        print(spracovane_mena)
        return spracovane_mena


if __name__ == "__main__":
    root = tk.Tk()
    hra = Hra(root, VSTUP_MIEN)
    root.mainloop()
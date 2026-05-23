import tkinter as tk

SIRKA = 500
VYSKA = 500
ZACIATOCNA_POZICIA = SIRKA // 2, VYSKA // 2

class Robot:
    def __init__(self, canvas: tk.Canvas, pozicia: tuple):
        self.canvas = canvas
        self.x = pozicia[0]
        self.y = pozicia[1]
        self.smer = ""
    
    def spracovanie_zadania(self, ako: str) -> str | int | None:
        ako = ako.strip().split()
        if len(ako) == 1:
            self.smer = "vpravo" if ako[0] == "vpravo" else print("A")
            self.smer = "vlavo" if ako[0] == "vlavo" else print("A")
        
        elif len(ako) == 2:
            try:
                o_kolko = int(ako[1])
            except:
                print("Druhý prvok nie je číslo!")
            if ako[0] == "ciara":
                ciara = "ciara"
                return ciara, o_kolko
    
    def vykreslenie(self, ako: str): 
        vysledok = self.spracovanie_zadania(ako)
        ciara, o_kolko = vysledok if len(vysledok) == 2 else print("A")
        
        ciarka = self.canvas.create_line(
            self.x, self.y,
            self.x, self.y 
        )
        

class Hra:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.canvas = tk.Canvas(
            width=SIRKA, height=VYSKA,
            background="grey"
        )
        self.canvas.pack()
    
    

if __name__ == "__main__":
    root = tk.Tk()
    hra = Hra(root)
    root.mainloop()
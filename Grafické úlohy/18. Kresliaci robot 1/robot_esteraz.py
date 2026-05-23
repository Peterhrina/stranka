import tkinter as tk

SIRKA = 500
VYSKA = 500
POZICIA = SIRKA // 2, VYSKA // 2

class Hra:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(
            width=SIRKA, height=VYSKA,
            background="grey"
        )
        self.canvas.pack()
        
        self.robot_smer = 0
    
    def spracuj_smer(self, vstup):
        ...
    
    def vykreslenie_robota(self, dlzka):
        

if __name__ == "__main__":
    root = tk.Tk()
    hra = Hra(root)
    root.mainloop()
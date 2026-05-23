import tkinter as tk
import random as rd

class Tanier:
    def __init__(self, pismenko, puknuty):
        self.pismenko = pismenko
        self.puknuty = puknuty
    
    def co_si_zac(self) -> bool:
        return self.pismenko, self.puknuty 
    

zoznam_tanierov: list = []
ktory_tanier: int = rd.randrange(0, 10)
for idx, znak in enumerate("ABCDEFGHIJ"):
    if ktory_tanier == idx: 
        zoznam_tanierov.append(Tanier(znak, True))
        puknute_pismenko = znak
    else: zoznam_tanierov.append(Tanier(znak, False))

id_tanierov = {}
def vykreslovanie(zoznam_tanierov: list):
    global id_tanierov
    for idx, tanier in enumerate(zoznam_tanierov):
        x = 1 + 100 * idx
        pismenko, puknuty = tanier.co_si_zac()
        ajdi = canvas.create_oval(
            x, VYSKA // 2 - 40,
            x + 90, VYSKA // 2 + 40,
            fill = "blue",
            outline = "black",
            width = 3
        )
        x1, y1, x2, y2 = canvas.coords(ajdi)
        stred_x, stred_y = (x1 + x2) / 2, (y1 + y2) / 2
        canvas.create_text(stred_x, stred_y, text = pismenko, font = ("Arial", 40, "bold"))
        id_tanierov[ajdi] = pismenko

def klik(event):
    global id_tanierov
    nalez = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    for objekt_id in nalez:
        if objekt_id in id_tanierov:
            pismenko = id_tanierov[objekt_id]
            print(f"Klikol si na {pismenko}")
            logika_check(pismenko)

kliknute: set = set()
def logika_check(pismeno):
    global puknute_pismenko, kliknute
    if pismeno == puknute_pismenko:
        canvas.delete("all")
        canvas.create_text(SIRKA // 2, VYSKA // 2,
            text = f"Gratulujeme! Označil si správny tanier: {pismeno}.",
            font = ("Arial", 20, "bold"), fill="blue")
        canvas.create_text(SIRKA // 2, VYSKA // 2 + 40,
            text = f"Predtým si klikol na taniere: {', '.join(kliknute)}.",
            font = ("Arial", 15, "bold"), fill="red")
    else: kliknute.add(pismeno)

SIRKA = 1000
VYSKA = 200

root = tk.Tk()
canvas = tk.Canvas(width=SIRKA, height=VYSKA, background="grey")
canvas.pack()

vykreslovanie(zoznam_tanierov)
canvas.bind_all("<Button-1>", klik)

root.mainloop()
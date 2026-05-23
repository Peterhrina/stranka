#53
import tkinter as tk
import random as rd

SIRKA = 600
VYSKA = 300
SUBOR = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/53. Zástavba na ulici/zastavba_na_ulici.txt"

with open(SUBOR, "r") as fr:
    nacitane_riadky = fr.readlines()

root = tk.Tk()
root.title("Môj program")
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

momentalne_x=0
for riadok in nacitane_riadky:
    sirka, vyska = riadok.split()
    if int(vyska) > 0:
        canvas.create_rectangle(momentalne_x, VYSKA,
                                momentalne_x + int(sirka), VYSKA - int(vyska),
                                outline="black", fill="grey"
                                )
        momentalne_x += int(sirka)
    else:
        canvas.create_line(momentalne_x,VYSKA,
                        momentalne_x + int(sirka), VYSKA,
                        fill="green", width=3
                        )
        momentalne_x += int(sirka)

def vykreslenie():
    global nacitane_riadky
    rozdiel = int(vstup.get())
    
    momentalne_x = 0
    for index, riadok in enumerate(nacitane_riadky[:-1]):
        sirka1, vyska1 = riadok.split()
        sirka2, vyska2 = nacitane_riadky[index + 1].split()
        
        momentalne_x += int(sirka1)
        
        if int(vyska1) - int(vyska2) > rozdiel:
            canvas.create_line(
                momentalne_x, VYSKA - int(vyska2),
                momentalne_x, VYSKA - int(vyska1),
                fill="red", width=2
            )
        elif int(vyska2) - int(vyska1) > rozdiel:
            canvas.create_line(
                momentalne_x, VYSKA - int(vyska2),
                momentalne_x, VYSKA - int(vyska1),
                fill="red", width=2
            )

vstup = tk.Entry(root)
vstup.pack()

tlacidlo = tk.Button(root, text="Potvrdiť", command=vykreslenie)
tlacidlo.pack()

root.mainloop()
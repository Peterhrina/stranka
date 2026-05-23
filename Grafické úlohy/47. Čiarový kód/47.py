import tkinter as tk
import random as rd

SIRKA = 800
VYSKA = 800
VSTUP = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/47. Čiarový kód/ciarovy_kod_1.txt"

root = tk.Tk()
root.title("Môj program")
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

with open(VSTUP, "r")as fr:
    nacitane_riadky = fr.readlines()

kod = rd.choice(nacitane_riadky).strip()
print(kod)

ZACIATOK_X = 0
VELKOST_STVORCA = 100
MEDZERA = 0
KROK = VELKOST_STVORCA + MEDZERA

for index, cislo in enumerate(kod):
    x = ZACIATOK_X + index * KROK
    canvas.create_rectangle(x, 0, x + VELKOST_STVORCA - (int(cislo) * 10), 0 + VYSKA, fill="black")

root.mainloop()
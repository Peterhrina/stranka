import tkinter as tk
import random as rd

SIRKA = 1200
VYSKA = 500
SUBOR = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/58. Trasa linky metra/trasa_linky_metra.txt"
FARBA = ""
ROZOSTUP = 0
X = 100

root = tk.Tk()
root.title("Môj program")
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

with open(SUBOR, "r", encoding="utf-8")as fr:
    nacitane_riadky = fr.readlines()

FARBA = nacitane_riadky[0]

canvas.create_line(0, 450, SIRKA, 450, fill="red", width=4)

ROZOSTUP = SIRKA // len(nacitane_riadky[1:])

for index, zastavka in enumerate(nacitane_riadky[1:]):
    x = X + index * 47
    if index == 0 or index == len(nacitane_riadky[1:]) - 1:
        canvas.create_rectangle(x-20, 430, x+20, 470, fill="red")
        canvas.create_text(x+60, 350, text=zastavka, fill="black", angle=45)
    else:
        if zastavka[0] == "*":
            canvas.create_oval(x, 440, x+20, 460, fill="white", outline="red", width=2)
            canvas.create_text(x+60, 350, text=zastavka[1:], fill="black", angle=45)
        else:
            canvas.create_oval(x, 440, x+20, 460, fill="red")
            canvas.create_text(x+60, 350, text=zastavka, fill="black", angle=45)

root.mainloop()
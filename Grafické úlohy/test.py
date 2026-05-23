import tkinter as tk

SIRKA = 800
VYSKA = 600
VSTUP = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/59. Vyťaženosť autobusovej linky/vytazenost_autobusevej_linky.txt"

root = tk.Tk()
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

with open(VSTUP, "r", encoding="utf-8") as fr:
    nacitane_riadky = fr.readlines()



root.mainloop()
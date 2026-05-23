import tkinter as tk
import random as rd

SIRKA = 500
VYSKA = 500
SUBOR = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/55. Kresliaci robot 2/kresliaci_robot2.txt"
SMERY_VEKTORY = {
    "hore": [0, -1],
    "vpravo": [1, 0],
    "dole": [0, 1],
    "vlavo": [-1, 0],
}
AKTUALNY_SMER = "hore"
AKTUALNA_POZICIA = [250, 250]

root = tk.Tk()
root.title("Môj program")
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

with open(SUBOR, "r")as fr:
    nacitane_riadky = fr.readlines()

def kreslenie(prikaz:str):
    global AKTUALNY_SMER, AKTUALNA_POZICIA
    if prikaz[0] == "ciara":
        canvas.create_line(
            AKTUALNA_POZICIA[0], AKTUALNA_POZICIA[1],
            AKTUALNA_POZICIA[0] + (SMERY_VEKTORY[AKTUALNY_SMER][0] * 50), AKTUALNA_POZICIA[1] + (SMERY_VEKTORY[AKTUALNY_SMER][1] * 50),width=2, fill="black")
        AKTUALNA_POZICIA[0] = AKTUALNA_POZICIA[0] + (SMERY_VEKTORY[AKTUALNY_SMER][0] * 50)
        AKTUALNA_POZICIA[1] = AKTUALNA_POZICIA[1] + (SMERY_VEKTORY[AKTUALNY_SMER][1] * 50)
    else:
        if prikaz[0] == "vpravo":
            if AKTUALNY_SMER == "hore":
                AKTUALNY_SMER = "vpravo"
            elif AKTUALNY_SMER == "vpravo":
                AKTUALNY_SMER = "dole"
            elif AKTUALNY_SMER == "dole":
                AKTUALNY_SMER = "vlavo"
            elif AKTUALNY_SMER == "vlavo":
                AKTUALNY_SMER = "hore"
        elif prikaz[0] == "vlavo":
            if AKTUALNY_SMER == "hore":
                AKTUALNY_SMER = "vlavo"
            elif AKTUALNY_SMER == "vlavo":
                AKTUALNY_SMER = "dole"
            elif AKTUALNY_SMER == "dole":
                AKTUALNY_SMER = "vpravo"
            elif AKTUALNY_SMER == "vpravo":
                AKTUALNY_SMER = "hore"

def opakovanie(prikazy, kolko):
    global AKTUALNY_SMER, kreslenie
    for _ in range(kolko):
        for prikaz in prikazy:
            temp = []
            temp.append(prikaz.strip())
            kreslenie(temp)

for index, prikaz in enumerate(nacitane_riadky):
    prikaz = list(prikaz.split())
    if prikaz[0] == "opakuj":
        index_koniecopakuj = nacitane_riadky.index("koniecopakuj\n")
        prikazy_na_opakovanie = nacitane_riadky[index + 1: index_koniecopakuj]
        nacitane_riadky = nacitane_riadky[index_koniecopakuj:]
        opakovanie(prikazy_na_opakovanie, (int(prikaz[1]) - 1))
    elif prikaz[0] != "koniecopakuj":
        kreslenie(prikaz)
    else:
        pass


root.mainloop()
import tkinter as tk
import random as rd

SIRKA = 400
VYSKA = 300
ZOZNAM_ZAPALIEK = []
VELKOST = 10
MEDZERA = 15
KROK = VELKOST + MEDZERA
X = 25
Y = 150
ZAPALKY=15
HRAC=1

root = tk.Tk()
root.title("Môj program")
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

canvas.create_text(SIRKA//2, 50, text="Ťahá hráč: 1", fill="black", font=("Arial", 20), anchor="w", tags="hraci")
canvas.create_text(100, 100, text=f"Zostáva Zápaliek: {ZAPALKY}", fill="black", font=("Arial", 20), anchor="w", tags="zapalky")

def vykreslenie():
    global ZOZNAM_ZAPALIEK
    for i in range(15):
        x = X + i * KROK
        id = canvas.create_line(x, Y, x, Y+100, width=5, fill='yellow')
        id2 = canvas.create_oval(x-5, Y-5, x+5, Y+8, fill='brown', outline='brown')
        ZOZNAM_ZAPALIEK.append(id)
        ZOZNAM_ZAPALIEK.append(id2)

vykreslenie()
print(ZOZNAM_ZAPALIEK)

def klik(event):
    global ZAPALKY, HRAC
    nalez = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    for objekt_id in nalez:
        if objekt_id in ZOZNAM_ZAPALIEK:
            cislo = int(objekt_id)
            canvas.delete(cislo)
            canvas.delete(cislo+1)
            ZAPALKY-=1
            canvas.delete("hraci")
            canvas.delete("zapalky")
            canvas.create_text(100, 100, text=f"Zostáva Zápaliek: {ZAPALKY}", fill="black", font=("Arial", 20), anchor="w", tags="zapalky")
            if HRAC == 1:
                HRAC=2
                canvas.create_text(SIRKA//2, 50, text=f"Ťahá hráč: {HRAC}", fill="black", font=("Arial", 20), anchor="w", tags="hraci")
            else:
                HRAC=1
                canvas.create_text(SIRKA//2, 50, text=f"Ťahá hráč: {HRAC}", fill="black", font=("Arial", 20), anchor="w", tags="hraci")

canvas.bind("<Button-1>", klik)

root.mainloop()
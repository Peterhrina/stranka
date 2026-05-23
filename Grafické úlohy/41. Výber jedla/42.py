import tkinter as tk
import random as rd

SIRKA = 800
VYSKA = 500
CESTA_K_SUBORU = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/41. Výber jedla/vyber_jedla.txt"

root = tk.Tk()
root.title("Môj program")
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

tk.Label(root, text="Kód študenta:").pack()

vstup_entry = tk.Entry(root)
vstup_entry.pack()

with open(CESTA_K_SUBORU, "w", encoding="utf-8") as fw:
    pass

def pisac(nazov:str):
    hodnota_vstupu = vstup_entry.get()
    
    if hodnota_vstupu != "":
        vstup_kod = int(hodnota_vstupu)
        
        with open(CESTA_K_SUBORU, "a", encoding="utf-8") as fw: # Používame mód "a" pre postupné pridávanie (Append)
            fw.write(f"{vstup_kod} {nazov}\n")
    else:
        print("Najprv zadaj kód študenta!")

canvas.create_text(SIRKA//2, 50, text="VÝBER JEDLA", fill="red", font=("Arial", 50))

id1 = canvas.create_rectangle(5, 200, 195, 400, fill="green", outline="black", width=2, tags="tvar")

id2 = canvas.create_rectangle(205, 200, 395, 400, fill="red", outline="black", width=2, tags="tvar")

id3 = canvas.create_rectangle(405, 200, 595, 400, fill="blue", outline="black", width=2, tags="tvar")

id4 = canvas.create_rectangle(605, 200, 795, 400, fill="yellow", outline="black", width=2, tags="tvar")

taniare = {
    id1: "green",
    id2: "red",
    id3: "blue",
    id4: "yellow"
}

def klik(event):
    nalez = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    for objekt_id in nalez:
        if objekt_id in taniare:
            pisac(taniare[objekt_id])

canvas.bind("<Button-1>", klik)


root.mainloop()
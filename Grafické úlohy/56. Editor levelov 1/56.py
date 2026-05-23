import tkinter as tk

SIRKA = 600
VYSKA = 600
FARBA = "black"

root = tk.Tk()
root.title("Môj program")
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

ZACIATOK_X = 0
ZACIATOK_Y = 0
KROK = 60
POCET_RIADKOV = 10
POCET_STLPCOV = 10
ID = []

for rad in range(POCET_RIADKOV):
    for stlpec in range(POCET_STLPCOV):
        x = ZACIATOK_X + stlpec * KROK
        y = ZACIATOK_Y + rad * KROK
        id = canvas.create_rectangle(x, y, x + 60, y + 60, outline="black", fill="white")
        ID.append(id)

def ulozit_farbu():
    global FARBA
    FARBA = vstup.get()
    print(FARBA)

vstup = tk.Entry(root)
vstup.pack()
tlacidlo = tk.Button(root, text="Potvrdiť", command=ulozit_farbu)
tlacidlo.pack()

def klik(event):
    global FARBA
    nalez = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    for objekt_id in nalez:
        if objekt_id in ID:
            canvas.itemconfig(objekt_id, fill=FARBA)


canvas.bind("<Button-1>", klik)

root.mainloop()
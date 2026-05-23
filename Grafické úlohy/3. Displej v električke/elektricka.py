import tkinter

vstup = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/3. Displej v električke/zastavky.txt"

def citanie_suboru(vstup):
    zastavky = list()
    with open(vstup, "r", encoding = "utf-8") as subor:
        for riadok in subor:
            zastavky.append(riadok.strip())
    return zastavky

def spracovanie_klaves(event):
    global aktualny_index, zastavky
    if event.keysym == "space":
        if aktualny_index + 1 == len(zastavky):
            aktualny_index = 0
        else:
            aktualny_index += 1

def animuj(id1, id2):
    global aktualny_index, zastavky
    x1 = canvas.coords(id1)[0]
    x2 = canvas.coords(id2)[0]
    
    #logika pohybu
    canvas.move(id1, -5, 0)
    canvas.move(id2, -5, 0)
    if x1 < -SIRKA_OKNA // 2:
        canvas.coords(id1, SIRKA_OKNA + (SIRKA_OKNA // 2), VYSKA_OKNA // 2)
    if x2 < -SIRKA_OKNA // 2:
        canvas.coords(id2, SIRKA_OKNA + (SIRKA_OKNA // 2), VYSKA_OKNA // 2)
    
    if not canvas.itemcget(id1, "text") == zastavky[aktualny_index]:
        if aktualny_index + 1 == len(zastavky):
            canvas.itemconfig(id1, text = zastavky[aktualny_index] + " Vystúpte!")
            canvas.itemconfig(id2, text = zastavky[aktualny_index] + " Vystúpte!")
        else:
            canvas.itemconfig(id1, text = zastavky[aktualny_index])
            canvas.itemconfig(id2, text = zastavky[aktualny_index])
    root.after(25, animuj, id1, id2)

SIRKA_OKNA = 1000
VYSKA_OKNA = 100
aktualny_index = 0
zastavky = citanie_suboru(vstup)

root = tkinter.Tk()
canvas = tkinter.Canvas(
    width = SIRKA_OKNA, height = VYSKA_OKNA,
    background = "black"
)
canvas.pack()

text1_id = canvas.create_text(
    SIRKA_OKNA // 2, VYSKA_OKNA // 2,
    text = zastavky[0], font = ("Arial", 50, "bold"), fill = "red"
)
text2_id = canvas.create_text(
    SIRKA_OKNA + SIRKA_OKNA // 2, VYSKA_OKNA // 2,
    text = zastavky[0], font = ("Arial", 50, "bold"), fill = "red"
)
animuj(text1_id, text2_id)

root.bind_all("<Key>", spracovanie_klaves)

root.mainloop()
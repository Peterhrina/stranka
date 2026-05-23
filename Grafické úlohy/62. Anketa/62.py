import tkinter as tk

SIRKA=600
VYSKA=300
VSTUP="Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/62. Anketa/anketa.txt"

with open(VSTUP, "r", encoding="windows-1250") as fr:
    nacitane_riadky: list=fr.readlines()
hodnoty=[int(cislo) for cislo in nacitane_riadky[1].strip().split()]

root=tk.Tk()
canvas=tk.Canvas(
    width=SIRKA, height=VYSKA, background="white"
)
canvas.pack()

canvas.create_text(
    SIRKA//2, 50, fill="black",
    text=nacitane_riadky[0]
)

canvas.create_text(
    50, 100, fill="black",
    text=f"1) Áno - {hodnoty[0]}", tags="jeden"
)
canvas.create_rectangle(
    100, 85, 100+hodnoty[0]*7, 115, fill="green", tags="jeden"
)

canvas.create_text(
    50, 150, fill="black",
    text=f"2) Nie - {hodnoty[1]}", tags="dva"
)
canvas.create_rectangle(
    100, 135, 100+hodnoty[1]*7, 165, fill="red", tags="dva"
)

canvas.create_text(
    50, 200, fill="black",
    text=f"3) Neviem - {hodnoty[2]}", tags="tri"
)
canvas.create_rectangle(
    100, 185, 100+hodnoty[2]*7, 215, fill="red", tags="tri"
)


def key_handler(event):
    if event.char == "1":
        hodnoty[0] += 1
    elif event.char == "2":
        hodnoty[1] += 1
    elif event.char == "3":
        hodnoty[2] += 1
    else:
        return
    
    najviac = max(hodnoty)
    
    canvas.delete("jeden", "dva", "tri")
    
    farba1 = "green" if hodnoty[0] == najviac else "red"
    farba2 = "green" if hodnoty[1] == najviac else "red"
    farba3 = "green" if hodnoty[2] == najviac else "red"
    
    canvas.create_text(50, 100, fill="black", text=f"1) Áno - {hodnoty[0]}", tags="jeden")
    canvas.create_rectangle(100, 85, 100+hodnoty[0]*7, 115, fill=farba1, tags="jeden")
    
    canvas.create_text(50, 150, fill="black", text=f"2) Nie - {hodnoty[1]}", tags="dva")
    canvas.create_rectangle(100, 135, 100+hodnoty[1]*7, 165, fill=farba2, tags="dva")
    
    canvas.create_text(50, 200, fill="black", text=f"3) Neviem - {hodnoty[2]}", tags="tri")
    canvas.create_rectangle(100, 185, 100+hodnoty[2]*7, 215, fill=farba3, tags="tri")


root.bind("<Key>", key_handler)

root.mainloop()
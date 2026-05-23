import tkinter as tk
import random as rd

SIRKA=800
VYSKA=600
ZACIATOK_X=50
ZACIATOK_Y=50
VSTUP="Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/64. Zasadací poriadok/zasadaci_poriadok.csv"

with open(VSTUP, "r", encoding="windows-1250") as fr:
    nacitane_riadky = fr.readlines()

spracovane_mena = [riadok.strip().split(";") for riadok in nacitane_riadky]

root = tk.Tk()
canvas = tk.Canvas(root,
            width=SIRKA, height=VYSKA,
            background="white"
        )
canvas.pack()

tk.Label(root,
    text="Počet radov:"
).pack()

entry_rady = tk.Entry(root)
entry_rady.pack()

tk.Label(root,
    text="Počet lavíc:"
).pack()

entry_lavic = tk.Entry(root)
entry_lavic.pack()

def vykreslenie():
    canvas.delete("all")
    zamiesane_riadky = spracovane_mena.copy()
    rd.shuffle(zamiesane_riadky)
    
    rady = int(entry_rady.get())
    lavice = int(entry_lavic.get())
    
    if (rady * lavice) >= len(zamiesane_riadky):
        for rad in range(rady):
            for lavica_v_rade in range(lavice):
                zaciatok_x = ZACIATOK_X + lavica_v_rade * 110
                zaciatok_y = ZACIATOK_Y + rad * 60
                
                canvas.create_rectangle(
                    zaciatok_x, zaciatok_y, zaciatok_x + 100, zaciatok_y + 50,
                    width=2, outline="grey"
                )
                
                if len(zamiesane_riadky) > 0:
                    Priezvisko = zamiesane_riadky[0][0]
                    Meno = zamiesane_riadky[0][1]
                    
                    canvas.create_text(
                        zaciatok_x + 50, zaciatok_y + 15,
                        text=Priezvisko, fill="red"
                    )
                    canvas.create_text(
                        zaciatok_x + 50, zaciatok_y + 35,
                        text=Meno, fill="blue"
                    )
                    
                    zamiesane_riadky.pop(0)



tlacidlo = tk.Button(root,
                text="Potvrdiť", command=vykreslenie
            )
tlacidlo.pack()

root.mainloop()
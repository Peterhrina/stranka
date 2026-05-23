import tkinter as tk
import random as rd

SIRKA=500
VYSKA=300
FARBY_ANO=["green", "yellow", "blue","green", "yellow", "blue","green", "yellow", "blue","green", "yellow", "blue","green", "yellow", "blue","green", "yellow", "blue","green", "yellow", "blue"]
FARBY_NIE="red"

root=tk.Tk()
canvas=tk.Canvas(
    width=SIRKA, height=VYSKA, background="white"
)
canvas.pack()

delenec=rd.randint(11,20)
delitel=rd.randint(2,9)

canvas.create_text(
    50, 25, text=f"{delenec} / {delitel} =", fill="black", font=("Arial", 20)
)

def over():
    cislo=int(cislo_entry.get())
    
    if delenec//delitel==cislo:
        canvas.create_text(SIRKA//2, 50,
                text="SPRÁVNE", fill="black", font=("Arial", 20)
            )
        
        zvysok = delenec - delitel * cislo
        nakreslene_kruhy = 0
        
        for skupina in range(cislo):
            for k in range(delitel):
                iks = 20 + nakreslene_kruhy * 30
                canvas.create_oval(
                    iks, 100, iks+20, 120, fill=FARBY_ANO[skupina]
                )
                nakreslene_kruhy += 1
                
        for k in range(zvysok):
            iks = 40 + nakreslene_kruhy * 30
            canvas.create_oval(
                iks, 100, iks+20, 120, fill=FARBY_NIE
            )
            nakreslene_kruhy += 1
            
    else:
        canvas.create_text(SIRKA//2, 50,
                text="NESPRÁVNE", fill="black", font=("Arial", 20)
            )

cislo_entry=tk.Entry(root)
cislo_entry.pack()

tk.Button(root, command=over, text="Over"
).pack()

root.mainloop()
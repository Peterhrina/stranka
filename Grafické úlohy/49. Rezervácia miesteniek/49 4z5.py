import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(width=600, height=300, bg='white')
canvas.pack()

pocetradov = 10
VEL = 40
busx, busy = 50, 50

VOLNE=40
OBSADENE=0
ULICKA_CISLA=[2, 3, 6, 7, 10, 11, 14,15, 18,19,22,23, 26,27,30,31,34,35,38,39]
ULICKA=20

canvas.create_text(15, 230, text="Počet voľných: 40", fill="black", anchor="w", tags="volne")
canvas.create_text(15, 250, text="Počet obsadených: 0", fill="black", anchor="w", tags="obsadene")
canvas.create_text(15, 270, text="Počet voľných pri uličke: 20", fill="black", anchor="w", tags="ulicka")

def zafarbi(sedadlo, farba):
    canvas.itemconfig('sedadlo_' + str(sedadlo), fill=farba)
    
def kresli(x, y, pocet):
    cislo = 0
    for i in range(pocet):
        for j in range(4):
            cislo += 1
            canvas.create_rectangle(x+i*VEL, y+j*VEL,
                                    x+(i+1)*VEL-10, y+(j+1)*VEL-10,
                                    tags='sedadlo_'+str(cislo), fill="light green", outline="black")
            canvas.create_text(x+i*VEL+VEL/2-5, y+j*VEL+VEL/2-5, text=cislo, fill="black")

def klik(event):
    global VOLNE, OBSADENE, ULICKA
    if (busx < event.x < busx + VEL * pocetradov and
        busy < event.y < busy + VEL * 4):
        ix = (event.x - busx) // VEL
        iy = (event.y - busy) // VEL
        sedadlo = ix * 4 + iy + 1
        aktualna_farba = canvas.itemcget('sedadlo_' + str(sedadlo), "fill")
        if aktualna_farba == "red":
            zafarbi(sedadlo, 'light green')
            if sedadlo in ULICKA_CISLA:
                ULICKA+=1
            OBSADENE-=1
            VOLNE+=1
            
            canvas.delete("volne", "obsadene", "ulicka")
            
            canvas.create_text(15, 230, text=f"Počet voľných: {VOLNE}", fill="black", anchor="w", tags="volne")
            canvas.create_text(15, 250, text=f"Počet obsadených: {OBSADENE}", fill="black", anchor="w", tags="obsadene")
            canvas.create_text(15, 270, text=f"Počet voľných pri uličke: {ULICKA}", fill="black", anchor="w", tags="ulicka")       
        else:
            zafarbi(sedadlo, 'red')
            if sedadlo in ULICKA_CISLA:
                ULICKA-=1
            OBSADENE+=1
            VOLNE-=1
            
            canvas.delete("volne", "obsadene", "ulicka")
            
            canvas.create_text(15, 230, text=f"Počet voľných: {VOLNE}", fill="black", anchor="w", tags="volne")
            canvas.create_text(15, 250, text=f"Počet obsadených: {OBSADENE}", fill="black", anchor="w", tags="obsadene")
            canvas.create_text(15, 270, text=f"Počet voľných pri uličke: {ULICKA}", fill="black", anchor="w", tags="ulicka")     
        
        print(sedadlo)
        

kresli(busx, busy, pocetradov)
canvas.bind('<Button-1>', klik)

root.mainloop()
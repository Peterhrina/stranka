import tkinter as tk

SIRKA=500
VYSKA=300
LIST=[["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], ["C", "+", "-", "="]]

root = tk.Tk()
canvas=tk.Canvas(
    width=SIRKA, height=VYSKA, background="grey"
)
canvas.pack()

priklad="0"

zaciatok_y=100
for riadok in LIST:
    zaciatok_x=20
    for znak in riadok:
        
        canvas.create_rectangle(
            zaciatok_x, zaciatok_y, zaciatok_x+40, zaciatok_y+40, outline="black", width=2
        )
        
        canvas.create_text((zaciatok_x+20), (zaciatok_y+20), text=znak)
        zaciatok_x += 40
    zaciatok_y+=40

def klik(event):
    global priklad
    if 100 <= event.y <= 140:
        stlpec = (event.x - 20) // 40
        
        if 0 <= stlpec <= 9:
            canvas.delete("riadok")
            if priklad == "0":
                priklad = str(stlpec)
            else:
                priklad+=str(stlpec)
            canvas.create_text(50,50, text=priklad, font=("utopia", 20), tags="riadok", anchor="w")
    
    elif 140 <= event.y <= 180:
        stlpec = (event.x - 20) // 40
        
        if stlpec == 0:
            canvas.delete("riadok")
            priklad="0"
            canvas.create_text(50,50, text=priklad, font=("utopia", 20), tags="riadok", anchor="w")
        
        if stlpec == 1:
            canvas.delete("riadok")
            priklad+="+0"
            canvas.create_text(50,50, text=priklad, font=("utopia", 20), tags="riadok", anchor="w")
        
        if stlpec == 2:
            canvas.delete("riadok")
            priklad+="-0"
            canvas.create_text(50,50, text=priklad, font=("utopia", 20), tags="riadok", anchor="w")
        
        if stlpec == 3:
            canvas.delete("riadok")
            canvas.create_text(50,50, text=eval(priklad), font=("utopia", 20), tags="riadok", anchor="w")
            priklad="0"
            
            
canvas.create_text(50,50, text=priklad, font=("utopia", 20), tags="riadok", anchor="w")

canvas.bind("<Button-1>", klik)

root.mainloop()
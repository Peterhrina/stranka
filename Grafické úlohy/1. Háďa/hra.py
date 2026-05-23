import tkinter

SIRKA_OKNA = 500
VYSKA_OKNA = 500
VELKOST_HADA = 10
RYCHLOST = 70

root = tkinter.Tk()
canvas = tkinter.Canvas(
    width = SIRKA_OKNA, height = VYSKA_OKNA,
    background = "black"
)
canvas.pack()

bezi_hra = True
smer = "hore"
x, y = 250, 250
kde_som_bol = set()

def zmena_smeru(event):
    global smer
    if event.keysym == "w" and smer != "dole":
        smer = "hore"
    
    elif event.keysym == "a" and smer != "do prava":
        smer = "do lava"
    
    elif event.keysym == "s" and smer != "hore":
        smer = "dole"
    
    elif event.keysym == "d" and smer != "do lava":
        smer = "do prava"

def vykreslenie_hada(poloha: tuple):
    global kde_som_bol, bezi_hra
    x, y = poloha
    
    if poloha in kde_som_bol or not (0 <= x <= SIRKA_OKNA) or not (0 <= y <= VYSKA_OKNA):
        canvas.create_text(
            SIRKA_OKNA // 2, VYSKA_OKNA // 2,
            text = "PREHRAL SI", font = ("Arial", 50, "bold"), fill = "red")
        bezi_hra = False
    
    kde_som_bol.add(poloha)
    
    canvas.create_rectangle(
        x, y,
        x + VELKOST_HADA, y + VELKOST_HADA,
        fill = "white"
    )

def hranie():
    global smer, x, y, bezi_hra
    
    if smer == "hore":
        vykreslenie_hada((x, y))
        y -= VELKOST_HADA
    
    elif smer == "do lava":
        vykreslenie_hada((x, y))
        x -= VELKOST_HADA
    
    elif smer == "dole":
        vykreslenie_hada((x, y))
        y += VELKOST_HADA
    
    elif smer == "do prava":
        vykreslenie_hada((x, y))
        x += VELKOST_HADA
    
    if bezi_hra: root.after(RYCHLOST, hranie)


root.bind_all("<Key>", zmena_smeru)
hranie()

root.mainloop()
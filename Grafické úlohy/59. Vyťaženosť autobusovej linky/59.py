import tkinter as tk

SIRKA = 800
VYSKA = 600
VSTUP = "Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/59. Vyťaženosť autobusovej linky/vytazenost_autobusevej_linky.txt"

root = tk.Tk()
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

with open(VSTUP, "r", encoding="utf-8") as fr:
    nacitane_riadky = fr.readlines()

max_kapacita = int(nacitane_riadky[0].strip())

# Spracujeme textový súbor do pekného zoznamu
zoznam_zastavok = []
for riadok in nacitane_riadky[1:]:
    casti = riadok.split()
    nastup = int(casti[0])
    vystup = int(casti[1])
    # Tretie a ďalšie slová spojíme (kvôli dvosjlovným názvom)
    nazov = " ".join(casti[2:])
    zoznam_zastavok.append({"nastup": nastup, "vystup": vystup, "nazov": nazov})

ZACIATOK_Y = 50
VELKOST_STVORCA = 20
MEDZERA = 15
KROK = VELKOST_STVORCA + MEDZERA

# 1. Po spustení rovno vypíšeme len texty zoznamu zastávok pod seba
for index in range(len(zoznam_zastavok)):
    y = ZACIATOK_Y + index * KROK
    # y+10 použijeme, aby bol text narovnako s obdĺžnikom, ktorý bude mať 20px
    canvas.create_text(20, y + 10, text=zoznam_zastavok[index]["nazov"], fill="black", anchor="w")

# Tieto dve premenné si držíme pomimo funkcií, aby sme sledovali plynule celú jazdu
aktualna_zastavka = 0
pocet_ludi = 0

def stlacenie_klavesy(event):
    global aktualna_zastavka, pocet_ludi
    
    # Kreslíme iba ak ešte zastávky vôbec v zozname existujú
    if aktualna_zastavka < len(zoznam_zastavok):
        # 1. Vypočítame počet ľudí
        zastavka = zoznam_zastavok[aktualna_zastavka]
        pocet_ludi = pocet_ludi + zastavka["nastup"] - zastavka["vystup"]
        
        # 2. Vyrátame Y súradnicu pre túto konkrétnu zastávku (náš zlatý vzorec)
        y = ZACIATOK_Y + aktualna_zastavka * KROK
        
        # 3. Určíme si, aký dlhý má byť obdĺžnik a akú má mať farbu (Trojčlenka z kapacity)
        MAX_DLSKA_OBDLZNIKA = 150 
        dlzka_pruhu = (pocet_ludi / max_kapacita) * MAX_DLSKA_OBDLZNIKA
        
        if pocet_ludi <= max_kapacita:
            farba = "green"
        else:
            farba = "red"
            
        # 4. Samotne kreslenie! (začneme ich kresliť napríklad od X=150)
        # Prázdny ohraničujúci rám (kapacita autobusu max)
        canvas.create_rectangle(150, y, 150 + MAX_DLSKA_OBDLZNIKA, y + VELKOST_STVORCA, outline="black")
        
        # Výplň farebného pása (ak je to červené, hodnota dlzka_pruhu presiahne rám)
        canvas.create_rectangle(150, y, 150 + dlzka_pruhu, y + VELKOST_STVORCA, fill=farba, outline="black")
        
        # Po nakreslení ideme pomyselne o zastávku hlbšie pre prípad ďalšieho kliknutia
        aktualna_zastavka += 1

root.bind("<Key>", stlacenie_klavesy)

root.mainloop()

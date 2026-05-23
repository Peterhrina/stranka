import tkinter as tk

def dekompresia_a_kreslenie(subor_cesta: str, velkost_pixelu: int = 10):
    """
    Načíta skomprimovaný obrázok, dekomprimuje ho a vykreslí na plátno.
    0 je biela, 1 je čierna.
    """
    with open(subor_cesta, "r", encoding="UTF-8") as fr:
        riadky = fr.readlines()

    rozmery_str = riadky[0].split()
    sirka, vyska = int(rozmery_str[0]), int(rozmery_str[1])

    okno = tk.Tk()
    okno.title("Dekomprimovaný Obrázok")
    platno = tk.Canvas(okno, width=sirka * velkost_pixelu, height=vyska * velkost_pixelu, bg="white")
    platno.pack()

    aktualny_y = 0
    for riadok_dat in riadky[1:]:
        pocty = [int(p) for p in riadok_dat.strip().split()]
        aktualny_x = 0
        farba_index = 0  # 0 pre čiernu (podľa kompresie), 1 pre bielu

        for i, pocet in enumerate(pocty):
            if i % 2 == 0:
                farba = "black" # 0 v kompresii -> čierna
            else:
                farba = "white" # 1 v kompresii -> biela

            for _ in range(pocet):
                if aktualny_x < sirka:
                    x1 = aktualny_x * velkost_pixelu
                    y1 = aktualny_y * velkost_pixelu
                    x2 = x1 + velkost_pixelu
                    y2 = y1 + velkost_pixelu
                    platno.create_rectangle(x1, y1, x2, y2, fill=farba, outline=farba)
                    aktualny_x += 1
        aktualny_y += 1

    okno.mainloop()

# Spustenie funkcie s cestou k súboru, ktorý vygeneruje 29.py
dekompresia_a_kreslenie("Škola-hodiny/Precvičovanie/Material_dudo/29. Kompresia obrázka/kompresia_obrazka_1.txt")

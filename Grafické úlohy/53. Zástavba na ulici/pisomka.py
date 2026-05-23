import tkinter as tk

SIRKA = 500
VYSKA = 300
ROZDIEL = 100

fr = open(r"/Users/nkubala/Projekty/Python/skolsky-rok-2025-26/Škola-hodiny/Precvičovanie/Material_dudo/Grafické úlohy/53. Zástavba na ulici/zastavba_na_ulici.txt", "r", encoding="utf-8")
subor = fr.read()
subor_list = subor.split("\n")
fr.close()
data = []
for row in subor_list:
    data.append(row.split())    

root = tk.Tk()
canvas = tk.Canvas(root, height=VYSKA, width=SIRKA)
canvas.pack()

x_suradnica = 0
y_suradnica = VYSKA
for row in data:
    x1 = x_suradnica
    y1 = y_suradnica
    x2 = x_suradnica + int(row[0])
    y2 = y_suradnica - int(row[1])
    if y2 == y_suradnica:
        canvas.create_rectangle(x1, y1, x2, y2, fill="green", width=2, outline="green")
    else:
        canvas.create_rectangle(x1, y1, x2, y2, fill="grey")
    x_suradnica = x2

entry1 = tk.Entry(root)
entry1.pack()

button = tk.Button(root, text="Potvrď", width=25, command=root.destroy)
button.pack()

root.mainloop()
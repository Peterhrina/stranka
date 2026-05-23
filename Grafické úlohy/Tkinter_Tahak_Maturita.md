# Tkinter Maturitný Ťahák (Grafické úlohy)

Tento dokument zhŕňa všetky kľúčové prvky, ktoré sme doteraz použili pri riešení grafických úloh (Zasadací poriadok, Kalkulačka, Anketa, Delenie...). Je to tvoj rýchly prehľad syntaxe a logiky pre úspešné zvládnutie maturity z Tkinteru.

---

## 1. Základná kostra programu
Každý Tkinter program začína importmi a vytvorením základného okna s plátnom (Canvas).

```python
import tkinter as tk
import random as rd  # Ak potrebuješ náhodné čísla alebo miešanie(shuffle)

SIRKA = 800
VYSKA = 600

root = tk.Tk()
canvas = tk.Canvas(root, width=SIRKA, height=VYSKA, background="white")
canvas.pack()

# ... Sem ide tvoj kód ...

root.mainloop()
```

---

## 2. Kreslenie na plátno (Canvas)
Plátno (`canvas`) je záchytný bod pre tvoje tvary. Vždy uvádzaš súradnice najskôr pre X a Y (prípadne ľavý horný a pravý dolný roh).

### a) Obdĺžnik (`create_rectangle`)
Vyžaduje 4 body: `(x1, y1, x2, y2)` - ľavý horný a pravý dolný roh.
```python
canvas.create_rectangle(50, 50, 150, 100, fill="red", outline="black", width=2, tags="tvar")
# fill = farba výplne
# outline = farba obrysu
# width = hrúbka obrysovej čiary
```

### b) Kruh / Elipsa (`create_oval`)
Zadáva sa rovnako ako obdĺžnik, do ktorého by si túto elipsu vpísal.
```python
canvas.create_oval(50, 50, 150, 150, fill="blue") 
```

### c) Text na plátne (`create_text`)
Vyžaduje len jeden bod (stred textu) X a Y. Defaultne sa text vycentruje!
```python
# POZOR NA ANCHOR! Ak chceš aby sa text roztiahol doprava a neušiel doľava, použi anchor="w" (West)
canvas.create_text(100, 100, text="Ahoj", fill="black", font=("Arial", 20), anchor="w")
```

### d) Mazanie objektov (`delete`)
Mazanie je ideálne buď kompletne na všetko, alebo pomocou "tagov" (čiže vygumovanie špecifických objektov).
```python
canvas.delete("all")      # Zmaže úplne všetko
canvas.delete("tvar")     # Zmaže len tie objekty, ktorým si pri zakladaní pridal parameter tags="tvar"
```

---

## 3. Vstupy od Používateľa (Ako v čistej aplikácii)
Toto sme použili pri **Zasadacom poriadku (64)** pre zadávanie počtu radov.

### a) Vytvorenie a umiestnenie
**NAJDÔLEŽITEJŠIE PRAVIDLO:** Vždy ukladaj Entry a Button do premennej a **.pack() na ďalší riadok!** Keby si to dal na jeden riadok (`tk.Entry().pack()`), uloží sa ti hodnota `None` a vyskočí ti chyba na `.get()`.

```python
# Nadpis
tk.Label(root, text="Zadaj niečo:").pack()

# Textové pole políčko
vstup = tk.Entry(root)
vstup.pack()

# Tlačidlo (priradí funkciu bez zátvoriek!)
tlacidlo = tk.Button(root, text="Potvrdiť", command=vykreslenie)
tlacidlo.pack()
```

### b) Čítanie z Entry políčka
Políčko ti hodnotu vráti **vždy ako reťazec (String)**. Ak s tým ideš počítať, musíš to zabaliť do `int()`.
```python
def vykreslenie():
    cislo_z_vstupu = int(vstup.get())
    print("Používateľ odpovedal", cislo_z_vstupu)
```

---

## 4. Trackovanie klikov a Myš/Klávesnica (Event Handler)
V úlohách ako **Anketa (62)** a **Kalkulačka (60)** sme museli reagovať na hardvérové akcie.

### a) Myš: Sledovanie polohy kliku (`<Button-1>`)
```python
def klik(event):
    # event.x a event.y obsahujú PRESNÝ pixel na plátne, kam si klikol myšou.
    stlpec = (event.x - 20) // 40  # Náš výpočet z Kalkulačky pre zistenie políčka
    print(f"Klik na X: {event.x}, Y: {event.y}")

canvas.bind("<Button-1>", klik)  # Všimni si, že viažeme udalosť na plátno!
```

### b) Klávesnica: Stlačenie klávesy (`<Key>`)
```python
def stlacenie_klavesy(event):
    # event.char schováva písmenko (alebo číslo ako string), ktoré bolo stlačené
    if event.char == "1":
        print("Užívateľ stlačil Jedničku!")

root.bind("<Key>", stlacenie_klavesy) # Klávesnicu viažeme zvyčajne na HLAVNÉ OKNO (root)
```

> **Poznámka k premenným vo vnútri funkcií:**
Ak vnútri "klik" alebo "stlacenie_klavesy" chceš **meniť** globálnu premennú (ako bol `priklad="0"` pri kalkulačke), musíš do funkcie napísať `global priklad`. Ak premennú len čítaš (nekombinuješ rovnítkom na novú hodnotu), global písať netreba.

---

## 5. Zlatý Vzorec: Rovnomerné (do radu) vykresľovanie
Či už to boli guličky z **Delenia (61)**, Kalkulačka alebo Zasadací poriadok, logika rastra je jedna:

**VZOREC PRE X / Y: Začiatok okraja + premenná_z_cyklu * (Veľkosť objektu + Voľná Medzera)**

```python
ZACIATOK_X = 20
VELKOST_STVORCA = 40
MEDZERA = 10
KROK = VELKOST_STVORCA + MEDZERA  # Teda 50!

for i in range(5):
    # O všetko posúvanie sa postará index (i)
    x = ZACIATOK_X + i * KROK 
    canvas.create_rectangle(x, 100, x + VELKOST_STVORCA, 100 + VELKOST_STVORCA)
```

Týmto nahradíš hrozivé snahy ako pripočítavať zakaždým vo vnútri cyklu `x = x + 50`.

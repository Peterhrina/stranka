import tkinter as tk
import random as rd

# --- KONŠTANTY A GLOBÁLNE PREMENNÉ ---

# Pôvodné rozmery okna
START_WIDTH = 600
START_HEIGHT = 800

# Premenné, ktoré sledujú aktuálnu veľkosť okna
aktualna_sirka = START_WIDTH
aktualna_vyska = START_HEIGHT

# Cesta k súboru so slovami
zoznam_slov_txt = "Precvičovanie/Material_dudo/44. Hlasovanie 2/vysledok.txt"

# Premenné pre stav hry
hra_bezi = False
skore_vyhra = 0
skore_prehra = 0
vybrane_slovo_original = ""
vybrane_slovo_na_hadanie = ""
upraveny_text = ""

# Globálne premenné pre Tkinter widgety (ID)
hviezdy_text = None
canvas = None
skore_vyhra_label = None
skore_prehra_label = None
obtiaznost_slider = None

# --- NAČÍTANIE SÚBORU ---

try:
    with open(zoznam_slov_txt, "r", encoding = "UTF-8") as fr:
        zoznam_slov = [slovo.strip() for slovo in fr.readlines()]
except FileNotFoundError:
    print(f"Súbor so slovami nenájdený, používam záložný.")
    zoznam_slov = ["jablko", "strom", "dom"]

# --- DEFINÍCIE FUNKCIÍ ---

def vyberanie_slov():
    """Vráti jedno náhodné slovo zo zoznamu."""
    return rd.choice(zoznam_slov)

def get_font_sizes():
    """Vypočíta dynamické veľkosti písma podľa aktuálnej výšky okna."""
    game_font_size = max(10, int(aktualna_vyska / 25))
    end_font_size = max(18, int(aktualna_vyska / 12))
    sub_font_size = max(8, int(aktualna_vyska / 40))
    return game_font_size, end_font_size, sub_font_size

# --- Hlavná herná logika ---

def start_nove_kolo():
    """Resetuje hru a spustí nové kolo."""
    global hra_bezi, vybrane_slovo_original, vybrane_slovo_na_hadanie, hviezdy_text, upraveny_text
    
    hra_bezi = True
    
    canvas.delete("koncovy_text")
    
    vybrane_slovo_original = vyberanie_slov()
    vybrane_slovo_na_hadanie = vybrane_slovo_original
    upraveny_text = "*" * len(vybrane_slovo_na_hadanie)
    
    game_font_size, _, _ = get_font_sizes()
    
    if hviezdy_text is None:
        hviezdy_text = canvas.create_text(
        aktualna_sirka / 2, 50,
        text = upraveny_text,
        fill = "white",
        font = ("Arial", game_font_size),
        tags = ("na_stred", "game_word")
        )
    else:
        canvas.coords(hviezdy_text, aktualna_sirka / 2, 50)
        canvas.itemconfig(hviezdy_text, text = upraveny_text, font=("Arial", game_font_size))
    
    padanie()

def padanie():
    """Hlavná herná slučka (game loop), ktorá posúva slovo."""
    global hra_bezi,vybrane_slovo_original, vybrane_slovo_na_hadanie, hviezdy_text, upraveny_text, skore_prehra, skore_prehra_label
    posun_y = 10
    
    if not hra_bezi:
        return
    
    canvas.move(hviezdy_text, 0, posun_y)
    
    if canvas.coords(hviezdy_text)[1] > aktualna_vyska - 50:
        hra_bezi = False
        
        skore_prehra += 1
        skore_prehra_label.config(text=f"Prehrané: {skore_prehra}")
        
        _, end_font_size, sub_font_size = get_font_sizes()
        
        canvas.create_text(
            aktualna_sirka / 2,
            aktualna_vyska / 2,
            text = f"PREHRAL SI!",
            fill = "red",
            font = ("Arial", end_font_size, "bold"),
            tags = ("koncovy_text", "na_stred", "end_main_text")
        )
        canvas.create_text(
            aktualna_sirka / 2,
            aktualna_vyska / 2 + (end_font_size / 2) + 10,
            text = f"Bolo to slovo: {vybrane_slovo_original}",
            fill = "white",
            font = ("Arial", sub_font_size, "bold"),
            tags = ("koncovy_text", "na_stred", "end_sub_text")
        )
    else:
        rychlost = obtiaznost_slider.get()
        canvas.after(rychlost, padanie)
        
def uhadnutie_pismenka(event):
    """Spracuje stlačenie klávesu a skontroluje výhru."""
    global hra_bezi,vybrane_slovo_original, vybrane_slovo_na_hadanie, hviezdy_text, upraveny_text, skore_vyhra, skore_vyhra_label
    
    if not hra_bezi:
        return
        
    stlacene_pismenko = event.char
    
    if not stlacene_pismenko.isalpha():
        return
    
    if stlacene_pismenko in vybrane_slovo_na_hadanie:
        # Táto logika .find() nájde len prvý výskyt písmena.
        # Pre slová ako "mama" to bude treba ešte vylepšiť!
        pozicia = vybrane_slovo_na_hadanie.find(stlacene_pismenko)
        upraveny_text = upraveny_text[:pozicia] + stlacene_pismenko + upraveny_text[pozicia + 1:]
        vybrane_slovo_na_hadanie = vybrane_slovo_na_hadanie[:pozicia] + "*" + vybrane_slovo_na_hadanie[pozicia + 1:]
        canvas.itemconfig(hviezdy_text, text = upraveny_text)
        
        if "*" not in upraveny_text:
            hra_bezi = False
            skore_vyhra += 1
            skore_vyhra_label.config(text=f"Výhrané: {skore_vyhra}")
            
            _, end_font_size, _ = get_font_sizes()
            
            canvas.create_text(
                aktualna_sirka / 2, aktualna_vyska / 2,
                text="VYHRAL SI!",
                fill="green",
                font=("Arial", end_font_size, "bold"),
                tags=("koncovy_text", "na_stred", "end_main_text")
            )

# --- Funkcie pre GUI (Udalosti) ---

def on_resize(event):
    """Prispôsobí obsah plátna novej veľkosti okna."""
    global aktualna_sirka, aktualna_vyska
    
    novy_stred_x = event.width / 2
    stary_stred_x = aktualna_sirka / 2
    posun_x = novy_stred_x - stary_stred_x
    
    aktualna_sirka = event.width
    aktualna_vyska = event.height
    
    # Posunie všetky objekty so značkou "na_stred"
    canvas.move("na_stred", posun_x, 0)
    
    # Prepočíta a nastaví nové veľkosti písma
    game_font_size, end_font_size, sub_font_size = get_font_sizes()
    
    canvas.itemconfig("game_word", font=("Arial", game_font_size))
    canvas.itemconfig("end_main_text", font=("Arial", end_font_size, "bold"))
    canvas.itemconfig("end_sub_text", font=("Arial", sub_font_size, "bold"))

def on_press(event):
    """Vizuálny efekt stlačenia tlačidla."""
    event.widget.config(bg="#444444", relief="sunken")

def on_release(event):
    """Vizuálny efekt pustenia tlačidla a spustenie novej hry."""
    event.widget.config(bg="#555555", relief="raised")
    start_nove_kolo()
    
# --- TVORBA GUI A LAYOUT ---

win = tk.Tk()
win.title("Padajúca hra PRO")

main_frame = tk.Frame(win)
main_frame.pack(fill=tk.BOTH, expand=True)

# --- Pravý stĺpec (Ovládací panel) ---
controls_frame = tk.Frame(main_frame, width=200, bg='#333333')
controls_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
controls_frame.pack_propagate(False)

skore_vyhra_label = tk.Label(controls_frame, text = "Výhrané: 0", font = ("Arial", 16), bg="#333333", fg="white")
skore_vyhra_label.pack(pady=10)

skore_prehra_label = tk.Label(controls_frame, text = "Prehrané: 0", font = ("Arial", 16), bg="#333333", fg="white")
skore_prehra_label.pack(pady=10)

nove_slovo_label = tk.Label(
    controls_frame,
    text = "Ďalšie kolo",
    bg="#555555",
    fg="white",
    font=("Arial", 13),
    relief="raised",
    borderwidth=2
)
nove_slovo_label.pack(pady=10, ipady=4, ipadx=10) 

obtiaznost_slider = tk.Scale(
    controls_frame,
    from_ = 2000,
    to = 10,
    orient = "horizontal",
    label = "Rýchlosť padania (ms)",
    bg="#333333",
    fg="white",
    troughcolor="#555555",
    activebackground="#666666"
)
obtiaznost_slider.set(1000)
obtiaznost_slider.pack(pady=10, padx=10)

# --- Ľavý stĺpec (Herná plocha) ---
game_frame = tk.Frame(main_frame)
game_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(game_frame, width=START_WIDTH, height=START_HEIGHT, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)

# --- VIAZANIE UDALOSTÍ (EVENT BINDING) ---

nove_slovo_label.bind("<ButtonPress-1>", on_press)
nove_slovo_label.bind("<ButtonRelease-1>", on_release)
canvas.bind("<Configure>", on_resize)
win.bind("<Key>", uhadnutie_pismenka)

# --- ŠTART APLIKÁCIE ---

win.mainloop()
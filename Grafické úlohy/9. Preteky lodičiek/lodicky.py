import tkinter as tk, random as rd

#KONŠTANTY
SIRKA = 700
VYSKA = 800
ZACIATOK_LODICIEK = 50, 50
POCET_LODICIEK = 15
RYCHLOST_LODIEK = 100

class Lodicka:
    def __init__(self, pozicia: tuple):
        self.pozicia = pozicia

class Hra:
    def __init__(self, root):
        self.canvas = tk.Canvas(width=SIRKA, height=VYSKA, background="white", )
        self.canvas.pack()
        
        self.lodicky_posledne_polohy: dict = dict()
        self.ciel_info: dict = dict()
        
        self.vytvorenie_lodiciek_zaciatok(POCET_LODICIEK)
        self.vykreslenie_ciela()
        self.posuvanie()
    
    def vykreslenie_ciela(self):
        id_ciela: int = self.canvas.create_line( 
                        SIRKA - 100, 0,
                        SIRKA - 100, VYSKA,
                        fill="red", width=3
                    )
        hitbox_ciela = self.canvas.bbox(id_ciela)
        
        self.ciel_info: dict[int] = {
            "id_ciela": id_ciela,
            "x1": hitbox_ciela[0],
            "y1": hitbox_ciela[1],
            "x2": hitbox_ciela[2],
            "y2": hitbox_ciela[3]
        }
    
    def lodicka(self, x: int, y: int) -> tuple[int, int]:
        plachta: int = rd.randint(-3, 3)
        ciara: int = self.canvas.create_line(
            x, y, x, y-25, x+10+plachta, y-10, x, y-5,
            fill="black", tags="lodicka"
        )
        spodok: int = self.canvas.create_polygon(
            x-20, y, x+20, y, x+10, y+8, x-10, y+8,
            fill="black", tags="lodicka"
        )
        return ciara, spodok
    
    def vytvorenie_lodiciek_zaciatok(self, pocet: int):
        x, y = ZACIATOK_LODICIEK
        for i in range(pocet):
            id_ciara, id_spodok = self.lodicka(x, y + (50 * i))
            self.lodicky_posledne_polohy[i] = x
    
    def posuvanie(self):
        self.canvas.delete("lodicka")
        
        x, y = ZACIATOK_LODICIEK
        #vytvorenie nových lodiciek pre efekt plavania
        for i in range(POCET_LODICIEK):
            posledne_x: int = self.lodicky_posledne_polohy[i]
            posledne_x: int = posledne_x + rd.randint(1, 10)
            self.lodicka(posledne_x, y + (50 * i))
            
            self.lodicky_posledne_polohy[i] = posledne_x
        
        vitazi: list[int] = self.check_vyhry()
        if vitazi:
            self.koniec(vitazi)
            return
        
        self.root.after(RYCHLOST_LODIEK, self.posuvanie)
    
    def check_vyhry(self) -> list[int]:
        vitazi: list[int] = list()
        lavy_hitbox_ciela: int = self.ciel_info["x1"]
        for cislo_lodky in self.lodicky_posledne_polohy:
            if self.lodicky_posledne_polohy[cislo_lodky] >= lavy_hitbox_ciela:
                vitazi.append(cislo_lodky)
        if len(vitazi) != 0: return vitazi
    
    def koniec(self, vitazi: list[int]):
        self.canvas.create_text(
            SIRKA // 2, VYSKA // 2,
            text=f"Víťazmi sú lodičky s číslom: {" ".join(map(str, vitazi))}",
            font=("Arial", 15, "bold"), fill="red" 
        )

root = tk.Tk()
hra = Hra(root)
root.mainloop()
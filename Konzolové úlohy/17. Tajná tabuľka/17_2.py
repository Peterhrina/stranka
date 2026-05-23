def tabulka():
    tabulka = [" ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
    
    inp = input("Zadaj vetu:").upper()
    
    veta_zoznam = [slovo for slovo in inp.split()]
    
    def sifruj(pismenko):
        for index, znaky in enumerate(tabulka):
            if pismenko in znaky:
                return str(index) * (znaky.find(pismenko) + 1)
    
    vysledok = []
    pocty = {}
    for slovo in veta_zoznam:
        for pismenko in slovo:
            zasifrovane = sifruj(pismenko)
            vysledok.append(zasifrovane)
            
            if zasifrovane[0] not in pocty:
                pocty[zasifrovane[0]] = len(zasifrovane)
            else:
                pocty[zasifrovane[0]] += len(zasifrovane)
        vysledok.append(str(0))
    print((" ").join(vysledok[:-1]))
    
    najviac_pouzite = max(pocty.values())
    for policko, pocet in pocty.items():
        if pocet == najviac_pouzite:
            print(f"Najčastejšie zvolené políčka: {policko}")
tabulka()

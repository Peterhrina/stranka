def tabulka():
    tabulka = [" ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
    inp = input("Zadaj vetu:").upper()
    
    def sifrovac(pismenko):
        for index, znaky in enumerate(tabulka):
            if pismenko in znaky:
                return str(index) * (znaky.find(pismenko) + 1)
    
    vysledok = []
    pocet = {}
    for znak in inp:
        if znak == " ":
            vysledok.append(str(0))
        else:
            zasifrovane = sifrovac(znak)
            vysledok.append(zasifrovane)
            if zasifrovane[0] in pocet:
                pocet[zasifrovane[0]] += len(zasifrovane)
            else:
                pocet[zasifrovane[0]] = len(zasifrovane)
    
    najviac_pouzite = max(pocet.values())
    print(f"Zašifrované: {(" ").join(vysledok)}")
    for znak, idk in pocet.items():
        if idk == najviac_pouzite:
            print(f"Najčastejšie zvolené políčka: {znak}")
tabulka()

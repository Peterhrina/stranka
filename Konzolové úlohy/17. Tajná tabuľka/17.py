def tabulka():
    tabulka = [" ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
    
    def hladac(char):
        for index_bunky, obsah_bunky in enumerate(tabulka):
            if char in obsah_bunky:
                index_pismena = obsah_bunky.find(char)
                return str(index_bunky) * (index_pismena + 1)
            
    
    inp = input("Zadaj text:").upper()
    
    zasifrovane_znaky = []
    for znak in inp:
        zasifrovany = hladac(znak)
        zasifrovane_znaky.append(zasifrovany)
    vysledna_sprava = " ".join(zasifrovane_znaky)
    print(vysledna_sprava)
    
    def pocitadlo(zasifrovane_znaky):
        slovnik = {}
        for znak in zasifrovane_znaky:
            cisielko = znak[0]
            if cisielko not in slovnik:
                slovnik[cisielko] = 1
            else:
                slovnik[cisielko] += 1
        max_hodnota = max(slovnik, key = slovnik.values())
        print(slovnik)
        print(max_hodnota)
    
    pocitadlo(zasifrovane_znaky)
tabulka()

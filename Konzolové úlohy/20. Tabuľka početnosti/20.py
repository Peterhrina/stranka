def pocetnost(vstup):
    with open(vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    for riadok in nacitane_riadky:
        print(riadok.strip())
    
    abeceda = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    
    pocty = {}
    for znak in abeceda:
        pocty[znak] = 0
        for riadok in nacitane_riadky:
            riadok_super = riadok.strip().upper()
            if znak in riadok_super:
                pocty[znak] += riadok_super.count(znak)
    
    nepouzite_znaky = []
    print("Počty jednotlivých znakov v texte:")
    for znak, pocet in pocty.items():
        if pocet == 0:
            nepouzite_znaky.append(znak)
        else:
            print(f"{znak} - {pocet}")
    print(f"Nepoužité znaky: {(", ").join(nepouzite_znaky)}")

vstup = "Precvičovanie/Material_dudo/20. Tabuľka početnosti/tabulka_pocetnosti.txt"
pocetnost(vstup)
def sifrovanie():
    veta = input("Zadajte vetu (bez diakritiky): ")
    kluc = input("Zadajte klúč (iba písmená bez diakritiky): ")
    
    if not kluc.isalpha():
        print("Klúč musí byť písmená!")
        return
    
    kluc = kluc * len(veta)
    i = 0
    
    vysledok = []
    for pismenko in veta:
        if "a" <= pismenko <= "z":
            posun = ord(kluc[i]) - ord("a") + 1
            i += 1
            stary_index = ord(pismenko) - ord("a")
            novy_index = (stary_index + posun) % 26
            nove_pismenko = chr(novy_index + ord("a"))
            vysledok.append(nove_pismenko)
        else:
            i += 1
            vysledok.append(pismenko)
    
    print(("").join(vysledok))

sifrovanie()
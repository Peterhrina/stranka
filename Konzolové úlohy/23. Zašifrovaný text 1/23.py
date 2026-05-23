from itertools import cycle

def uloha23() -> str:
    input_veta: str = input("Zadaj vetu čo chceš zašifrovať: ").lower()
    input_kluc: str = input("Zadaj kľúč ktorým chceš šifrovať: ").lower()
    
    cyklicky_input_kluc = cycle([ord(pismenko) - 96 for pismenko in input_kluc])
    
    vysledok = []
    for slovo in input_veta.split():
        temp_slovo = []
        for pismenko in slovo:
            key_char = next(cyklicky_input_kluc)
            premenene_pismenko = chr(ord(pismenko) + key_char)
            temp_slovo.append(premenene_pismenko)
        vysledok.append(("").join(temp_slovo))
    print((" ").join(vysledok))
    
uloha23()
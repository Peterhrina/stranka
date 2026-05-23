from itertools import cycle

def sifrovac(veta: str, kluc: str) -> str:
    
    if not veta.isalpha() or not kluc.isalpha():
        raise ValueError("Veta alebo klúč obsahuje iné znaky ako písmenka malej abecedy!")
    
    vysledok: list[str] = []
    zacykleny_kluc = cycle(kluc)
    zaciatok_abecedy: int = ord("a")
    for znak in veta:
        if "a" <= znak <= "z":
            posun: int = ord(next(zacykleny_kluc)) - ord("a") + 1
            stary_index: int = ord(znak) - zaciatok_abecedy
            novy_index: int = (stary_index + posun) % 26
            nove_pismenko: str = chr(novy_index + zaciatok_abecedy)
            vysledok.append(nove_pismenko)
        else:
            next(zacykleny_kluc)
            vysledok.append(znak)
    return "".join(vysledok)

def main() -> None:
    veta_input: str = input("Napíšte vetu ktorú chcete zašifrovať:").lower()
    kluc_input: str = input("Napíšte kľúč ktorým budete šifrovať, napr: abc, jlaje, ...:").lower()
    
    print(sifrovac(veta_input, kluc_input))

if __name__ == "__main__":
    main()
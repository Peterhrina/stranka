from itertools import cycle

def sifruj_text(veta: str, kluc: str) -> str:
    
    if not kluc or not kluc.isalpha():
        # Ak je kľúč neplatný, vyvoláme chybu ValueError.
        raise ValueError("Kľúč nemôže byť prázdny a musí obsahovať len písmená.")
    
    # Cycle nám možňuje donekonečna opakovať sekvenciu (v našom prípade kľúč).
    kluc_cyklus = cycle(kluc)
    
    zasifrovane_pismena: list[str] = []
    for pismenko in veta:
        if "a" <= pismenko <= "z":
            posun: int = ord(next(kluc_cyklus)) - ord("a") + 1 # Next nech prechádzame cyklus kľúča.
            
            start_abecedy: int = ord("a")
            pismenko_index: int = ord(pismenko) - start_abecedy
            
            # Aplikujeme posun a operátor modulo (%) zabezpečí,
            # že sa po 'z' vrátime späť na 'a'.
            novy_index: int = (pismenko_index + posun) % 26
            nove_pismenko: str = chr(start_abecedy + novy_index)
            zasifrovane_pismena.append(nove_pismenko)
        else:
            # Ostatné znaky (medzery, interpunkcia) pridáme bez zmeny.
            zasifrovane_pismena.append(pismenko)
            
    return "".join(zasifrovane_pismena)

def main() -> None:
    veta: str = input("Zadaj vetu čo chceš zašifrovať: ").lower()
    kluc: str = input("Zadaj kľúč ktorým chceš šifrovať: ").lower()
    
    zasifrovana_veta: str = sifruj_text(veta, kluc)
    print("Zašifrovaná veta:", zasifrovana_veta)


if __name__ == "__main__":
    main()
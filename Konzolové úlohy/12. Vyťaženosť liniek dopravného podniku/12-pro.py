#PETO TY HOVNO IBA POZNAMKY MI ROBILO AIKO JEDNODUCHSI KOD MAS V SUBORE 12
def vytazenost_liniek(cesta_k_suboru):

    # Načítanie všetkých riadkov zo súboru.
    with open(cesta_k_suboru, "r", encoding = "UTF-8") as fr:
        zaznamy_riadky = fr.readlines()

    # Prvý riadok v súbore je maximálna kapacita.
    max_kapacita = int(zaznamy_riadky[0].strip())

    zaznam_zoznam = []
    # Spracovanie riadkov so zastávkami (preskočenie prvého riadku s kapacitou).
    for zaznam in zaznamy_riadky[1:]:
        # split(" ", 2) je dôležitý pre názvy zastávok s medzerami.
        nastupujuci, vystupujuci, zastavka = zaznam.strip().split(" ", 2)

        # Uloženie dát do slovníka, čísla sú rovno pretypované na int.
        zaznam_slovnik = {
            "Nastupujúci": int(nastupujuci),
            "Vystupujúci": int(vystupujuci),
            "Zastávka": zastavka
        }
        zaznam_zoznam.append(zaznam_slovnik)

    print(f"Počet zastávok: {len(zaznam_zoznam)}")

    # Získanie zoznamu názvov zastávok pomocou list comprehension.
    zastavky_nazov_zoznam = [zaznam["Zastávka"] for zaznam in zaznam_zoznam]
    # Spojenie názvov do jedného reťazca pre výpis.
    zastavky_nazov_string = (", ").join(zastavky_nazov_zoznam)
    print(f"Názvy zástavok: {zastavky_nazov_string}")

    # Premenné pre simuláciu jazdy.
    priebezny_pocet = 0
    max_plny = 0

    # Prechod zastávkami a výpočet vyťaženosti.
    for zastavenie in zaznam_zoznam:
        # Aktualizácia počtu ľudí v autobuse.
        priebezny_pocet += zastavenie["Nastupujúci"]
        priebezny_pocet -= zastavenie["Vystupujúci"]

        # Kontrola, či je autobus preplnený.
        if priebezny_pocet > max_kapacita:
            print(f"Na zastávke {zastavenie["Zastávka"]} bol autobus preplnený!")

        # Zaznamenanie nového maxima vyťaženosti.
        if priebezny_pocet > max_plny:
            max_plny = priebezny_pocet

    # Výpis finálneho prekročenia kapacity.
    print(f"Autobus bol najviac preplnený o {max_plny - max_kapacita} ľudí.")

# Definovanie súboru a spustenie funkcie.
subor = "Precvičovanie/Material_dudo/12. Vyťaženosť liniek dopravného podniku/bus_vytazenost.txt"
vytazenost_liniek(subor)
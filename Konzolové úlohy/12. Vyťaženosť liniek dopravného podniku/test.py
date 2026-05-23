def vytazenost_liniek(subor):

    with open(subor, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()

    max_kapacita = int(nacitane_riadky[0].strip())

    zastavka_zoznam = []
    for zastavenie in nacitane_riadky[1:]:
        nastupujuci, vystupujuci, zastavka = zastavenie.strip().split(" ", 2)
        zastavka_slovnik = {
            "Počet_nastupujúcich": int(nastupujuci),
            "Počet_vystupujúcich": int(vystupujuci),
            "Názov_zástavky": zastavka
        }
        zastavka_zoznam.append(zastavka_slovnik)

    print(f"Počet zastávok: {len(zastavka_zoznam)}")

    zastavky_zoznam = []
    for zastavenie in zastavka_zoznam:
        zastavky_zoznam.append(zastavenie["Názov_zástavky"])
    zastavky_str = ", ".join(zastavky_zoznam)
    print(f"Zastávky: {zastavky_str}")

    priebezny_pocet = 0
    max_prekrocenie = 0
    for zastavenie in zastavka_zoznam:
        priebezny_pocet += zastavenie["Počet_nastupujúcich"]
        priebezny_pocet -= zastavenie["Počet_vystupujúcich"]
        if priebezny_pocet > max_kapacita:
            print(f"Na zastávke {zastavenie["Názov_zástavky"]} je veľa ľudí.")
        if priebezny_pocet > max_prekrocenie:
            max_prekrocenie = priebezny_pocet

    print(f"Najviac ľudí prekročilo o {max_prekrocenie - max_kapacita}.")

subor = "Precvičovanie/Material_dudo/12. Vyťaženosť liniek dopravného podniku/bus_vytazenost.txt"
vytazenost_liniek(subor)
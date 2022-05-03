import sys

f = open(sys.argv[1])

linia = f.readline().strip()

akcja = linia
historia = []
hist_tmp = []
saldo = 0
magazyn = {}
ilosc_szt = 0


def dodawanie_historii(argument):

    f = sys.argv[1]
    with open(f, "a") as plik:
        plik.write(str(argument) + "\n")



### HISTORIA

while True:

    if akcja not in ["saldo", "zakup", "sprzedaz"]:
        print()
        print("Brak akcji saldo/sprzedaz/zakup!")
        print("Nieprawidlowy input!")
        print()
        exit()

    if akcja == "saldo":
        saldo_zmiana = int(f.readline().strip())
        saldo_koment = f.readline().strip()

        hist_tmp.append(akcja)
        hist_tmp.append(saldo_zmiana)
        hist_tmp.append(saldo_koment)

        historia.append(hist_tmp)
        hist_tmp = []

        saldo += (saldo_zmiana)

    elif akcja == "zakup":

        produkt = f.readline().strip()
        cena = int(f.readline().strip())
        szt = int(f.readline().strip())

        hist_tmp.append(akcja)
        hist_tmp.append(produkt)
        hist_tmp.append(cena)
        hist_tmp.append(szt)

        historia.append(hist_tmp)
        hist_tmp = []

        saldo = saldo - (cena * szt)

        if saldo < 0:
            print()
            print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
            print()
            exit()

        if produkt not in magazyn:
            magazyn[produkt] = szt

        elif produkt in magazyn:

            x = magazyn[produkt]
            ilosc_szt = x + szt
            magazyn[produkt] = ilosc_szt

    elif akcja == "sprzedaz":
        produkt = f.readline().strip()
        cena = int(f.readline().strip())
        szt = int(f.readline().strip())

        hist_tmp.append(akcja)
        hist_tmp.append(produkt)
        hist_tmp.append(cena)
        hist_tmp.append(szt)

        historia.append(hist_tmp)
        hist_tmp = []

        saldo = saldo + (cena * szt)

        if produkt not in magazyn:
            print()
            print("Błąd!""\nNie ma takiego produktu w magazynie!")
            print()
            exit()
        if produkt in magazyn:
            x = magazyn[produkt]
            ilosc_szt = x - szt
            magazyn[produkt] = ilosc_szt

            if ilosc_szt == 0:
                del magazyn[produkt]

            elif ilosc_szt < 0:
                print()
                print("Nieprawidłowa operacja: za duża ilość sprzedanych elementów!")
                print()
                exit()

    akcja = f.readline().strip()
    if akcja == "":
        f.close()
        break


### SYS.ARGV

# def dozwolone_komendy():
#     if sys.argv[2] not in ["konto", "magazyn", "przeglad",
#                            "saldo", "zakup", "sprzedaz", "historia", "stan"]:  # USUNAC HISTORIĘ
#         print()
#         print("Niedozwolona akcja!")
#         print()
#         exit()

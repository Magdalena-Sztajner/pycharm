import sys
import accountant_3_historia

from accountant_3_historia import dodawanie_historii, historia, magazyn


def sprz():
    from accountant_3_historia import hist_tmp, saldo
    if sys.argv[2] == "sprzedaz":
        produkt = sys.argv[3]
        cena = int(sys.argv[4])
        szt = int(sys.argv[5])

        if produkt not in magazyn:
            print()
            print("Błąd!""\nNie można sprzedać produktu którego nie ma w magazynie!")
            print()
            exit()
        elif produkt in magazyn:
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

        hist_tmp.append(sys.argv[2])
        dodawanie_historii(sys.argv[2])
        hist_tmp.append(produkt)
        dodawanie_historii(produkt)
        hist_tmp.append(cena)
        dodawanie_historii(cena)
        hist_tmp.append(szt)
        dodawanie_historii(szt)

        historia.append(hist_tmp)
        hist_tmp = []

        saldo = saldo + (cena * szt)

    # print()
    # print()
    # for element in historia:
    #     print(element)


import accountant_3_Manager

# print()
# print("Saldo:", saldo)
# print()
# print("Magazyn:", magazyn)
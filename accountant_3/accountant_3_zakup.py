import sys
# import acc3

from acc3 import historia, magazyn, dodawanie_historii, saldo, hist_tmp


# dozwolone_komendy()

def zak():
    from acc3 import saldo, hist_tmp
    produkt = sys.argv[3]
    cena = int(sys.argv[4])
    szt = int(sys.argv[5])

    saldo = saldo - (cena * szt)

    if saldo < 0:
        print()
        print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
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

    if produkt not in magazyn:
        magazyn[produkt] = szt
    else:
        x = magazyn[produkt]
        ilosc_szt = x + szt
        magazyn[produkt] = ilosc_szt


import man


# print()
# print("Saldo:", saldo)
# print()
# print("Magazyn:", magazyn)

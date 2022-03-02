akcja = input()
historia = []
hist_tmp = []
saldo = 0
magazyn = {}
ilosc_szt = 0

while True:


    if akcja not in ["saldo", "zakup", "sprzedaz"]:
        print()
        print("Brak akcji saldo/sprzedaz/zakup!")
        print("Nieprawidlowy input!")
        print()
        exit()

    if akcja == "saldo":
        saldo_zmiana = int(input())
        saldo_koment = input()

        hist_tmp.append(akcja)
        hist_tmp.append(saldo_zmiana)
        hist_tmp.append(saldo_koment)

        saldo += (saldo_zmiana)

        historia.append(hist_tmp)
        hist_tmp = []

    elif akcja == "zakup":
        produkt_zakup = input()
        cena_zakupu = int(input())
        szt_zakup = int(input())

        hist_tmp.append(akcja)
        hist_tmp.append(produkt_zakup)
        hist_tmp.append(cena_zakupu)
        hist_tmp.append(szt_zakup)

        saldo = saldo - (cena_zakupu * szt_zakup)

        if saldo < 0:
            print()
            print("Nie można dokonać zakupu!" "\nZa mało pieniędy na koncie!")
            print()
            exit()

        historia.append(hist_tmp)
        hist_tmp = []

        if produkt_zakup not in magazyn:
            magazyn[produkt_zakup] = szt_zakup
        else:
            x = magazyn[produkt_zakup]
            ilosc_szt = x + szt_zakup
            magazyn[produkt_zakup] = ilosc_szt


    elif akcja == "sprzedaz":
        produkt_sprzedaz = input()
        cena_sprzedazy = int(input())
        szt_sprzedaz = int(input())


        hist_tmp.append(akcja)
        hist_tmp.append(produkt_sprzedaz)
        hist_tmp.append(cena_sprzedazy)
        hist_tmp.append(szt_sprzedaz)

        saldo = saldo + (cena_sprzedazy * szt_sprzedaz)

        historia.append(hist_tmp)
        hist_tmp = []

        if produkt_sprzedaz not in magazyn:
            print()
            print("Błąd!""\nNie można sprzedać produktu którego nie ma w magazynie!")
            print()
            exit()
        if produkt_sprzedaz in magazyn:
            x = magazyn[produkt_sprzedaz]
            ilosc_szt = x - szt_sprzedaz
            magazyn[produkt_sprzedaz] = ilosc_szt

            if ilosc_szt == 0:
                del magazyn[produkt_sprzedaz]

            elif ilosc_szt <0:
                print()
                print("Nieprawidłowa operacja: za duża ilość sprzedanych elementów!")
                print()
                exit()

    akcja = input()
    if akcja == "stop":
        break


# print()
#
# for element in historia:
#     print(element)
#
# print()
#
# print("Saldo:", saldo)
#
# print()
#
# print("Magazyn:", magazyn)


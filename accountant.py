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
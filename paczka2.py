waga_elementu = int(input())
waga_paczki = 0
wyslane_paczki = 0
waga_ostatniego_elementu = 0
suma_pustych_kg_w_paczkach = 0
puste_kg_w_paczce = 0
razem_kg = 0
max_pustych_kg = 0
nr_paczki = 0


while waga_elementu:

    if waga_elementu == 0 or waga_elementu > 10 or waga_elementu == -111:
        break

    waga_paczki += waga_elementu

    if waga_paczki < 20:
        print("Dobieram element")
        max_pustych_kg = puste_kg_w_paczce
        waga_ostatniego_elementu = waga_paczki

    elif waga_paczki == 20:
        print("Idealnie! Wysyłam")
        razem_kg += waga_paczki
        puste_kg_w_paczce = 20 - waga_paczki
        suma_pustych_kg_w_paczkach += puste_kg_w_paczce
        wyslane_paczki = wyslane_paczki + 1
        waga_paczki = 0
        waga_ostatniego_elementu = 0

    else:
        print("Maksymalna waga paczki przekroczona! Odejmuję element i wysyłam")
        waga_paczki -= waga_elementu
        wyslane_paczki = wyslane_paczki + 1
        puste_kg_w_paczce = 20 - waga_paczki
        suma_pustych_kg_w_paczkach += puste_kg_w_paczce
        razem_kg += waga_paczki
        waga_paczki = waga_elementu
        waga_ostatniego_elementu = waga_elementu


    waga_elementu = int(input())


    if waga_elementu == 0 or waga_elementu > 10 or waga_elementu == -111: #-111: end of file
            if waga_ostatniego_elementu > 0:
                waga_paczki = waga_paczki - waga_ostatniego_elementu
                wyslane_paczki = wyslane_paczki + 1
                puste_kg_w_paczce = 20 - waga_ostatniego_elementu
                suma_pustych_kg_w_paczkach += puste_kg_w_paczce
                razem_kg += waga_ostatniego_elementu

    if puste_kg_w_paczce > max_pustych_kg:
        max_pustych_kg = puste_kg_w_paczce
        nr_paczki = wyslane_paczki



print()

if waga_elementu == 0:
    print("BŁĄD! Element waży za mało\nWysyłam resztę i przerywam pracę")

if waga_elementu > 10:
    print("BŁĄD! Element za ciężki\nWysyłam resztę i przerywam pracę")

if waga_elementu == -111:
    print("BŁĄD! Koniec elementów\nWysyłam resztę i przerywam pracę")

print()

szablon_podsumowania = ("Ilość wysłanych paczek to: {} szt."
                        "\nRazem wysłano: {} kg \nŁącznie puste kg: {} kg"
                        "\nNajwięcej pustych kg w paczce to: {} kg"
                        "\nNajwięcej pustych kg miała paczka nr: {}")

podsumowanie = szablon_podsumowania.format(wyslane_paczki, razem_kg,
               suma_pustych_kg_w_paczkach, max_pustych_kg, nr_paczki)
print(podsumowanie)

print()
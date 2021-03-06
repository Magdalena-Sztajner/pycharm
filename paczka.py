waga_elementu = int(input())
waga_paczki = 0
wyslane_paczki = 0
waga_ostatniego_elementu = 0
suma_pustych_kg = 0
puste_kg = 0
razem_kg = 0
max_pustych_kg = 0
nr_paczki = 0


while waga_elementu and waga_elementu <= 10:

    waga_paczki += waga_elementu

    if waga_paczki < 20:
        print("Dobieram element")
        max_pustych_kg = puste_kg
        waga_ostatniego_elementu = waga_paczki

    elif waga_paczki == 20:
        print("Idealnie! Wysyłam")
        razem_kg += waga_paczki
        puste_kg = 20 - waga_paczki
        suma_pustych_kg += puste_kg
        wyslane_paczki = wyslane_paczki + 1
        waga_paczki = 0
        waga_ostatniego_elementu = 0

    else:
        print("Maksymalna waga paczki przekroczona! Odejmuję element i wysyłam")
        waga_paczki -= waga_elementu
        wyslane_paczki = wyslane_paczki + 1
        puste_kg = 20 - waga_paczki
        suma_pustych_kg += puste_kg
        razem_kg += waga_paczki
        waga_paczki = waga_elementu
        waga_ostatniego_elementu = waga_elementu

    waga_elementu = int(input())


    # wysłanie ostatniego elementu/elementów, (jeżeli nie było błędu wszystkie elementy muszą zostać wysłane)
    # dodane 404 by pozbyć się błędu "EOFError: EOF when reading a line"
    if waga_elementu == 404 and waga_ostatniego_elementu > 0:
        print("Koniec elementów! Wysyłam resztę.")
        waga_paczki = waga_paczki - waga_elementu
        wyslane_paczki = wyslane_paczki + 1
        puste_kg = 20 - waga_ostatniego_elementu
        suma_pustych_kg += puste_kg
        razem_kg += waga_ostatniego_elementu

    if puste_kg > max_pustych_kg:
        max_pustych_kg = puste_kg
        nr_paczki = wyslane_paczki

print()

if waga_elementu < 1:
    print("BŁĄD! Element waży za mało\nPrzerywam pracę")

if waga_elementu > 10 and waga_elementu != 404:
    print("BŁĄD! Element za ciężki\nPrzerywam pracę")

print()

szablon_podsumowania = ("Ilość wysłanych paczek to: {} szt."
                        "\nRazem wysłano: {} kg \nŁącznie puste kg: {} kg"
                        "\nNajwięcej pustych kg w paczce to: {} kg"
                        "\nNajwięcej pustych kg miała paczka nr: {}")

podsumowanie = szablon_podsumowania.format(wyslane_paczki, razem_kg, suma_pustych_kg, max_pustych_kg, nr_paczki)
print(podsumowanie)

print()
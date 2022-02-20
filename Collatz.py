print("Podaj liczbę")
wybrana_liczba = int(input())
dlugosc_ciagu = 0
liczba_poczatkowa = wybrana_liczba

while wybrana_liczba != 1:

      if wybrana_liczba % 2 == 0:
            wybrana_liczba = wybrana_liczba/2
            dlugosc_ciagu += 1

      else:
            wybrana_liczba = 3 * wybrana_liczba + 1
            dlugosc_ciagu += 1

import math
#
m1_godziny = 0
m2_godziny = 0
m3_godziny = 0
lacznie_czas_naprawy = 0
m1_dni_pracy = 0
m2_dni_pracy = 0
m3_dni_pracy = 0
dyspozycyjnosc_wszystkich_mechanikow = 0
max_liczba_dni = 0
numer_kolejnych_zlecenia = 0
numer_zlecenia = 1
lista_dyspo = []

liczba_zlecen = int(input("Ile jest samochodów do naprawy? "))
numer = liczba_zlecen
for i in range(numer):
        numer_kolejnych_zlecenia += numer_zlecenia
        czas_naprawy = int(input(f"Ile czasu zajmie naprawa nr {numer_kolejnych_zlecenia}? : "))

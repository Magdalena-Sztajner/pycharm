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
        if m1_godziny <= m2_godziny and m1_godziny <= m3_godziny:
            m1_godziny += czas_naprawy
            m1_dni_pracy = math.ceil(m1_godziny / 8)
            lista_dyspo.append(m1_dni_pracy)


        elif m2_godziny > m3_godziny:
            m3_godziny += czas_naprawy
            m3_dni_pracy = math.ceil(m3_godziny / 8)
            lista_dyspo.append(m3_dni_pracy)

        else:
            m2_godziny += czas_naprawy
            m2_dni_pracy = math.ceil(m2_godziny / 8)
            lista_dyspo.append(m2_dni_pracy)

        if m1_dni_pracy > m2_dni_pracy and m1_dni_pracy > m3_dni_pracy:
            max_liczba_dni = m1_dni_pracy

        elif m2_dni_pracy > m3_dni_pracy:
            max_liczba_dni = m2_dni_pracy

        else:
            max_liczba_dni = m3_dni_pracy


lacznie_czas_naprawy += czas_naprawy

dyspozycyjnosc_wszystkich_mechanikow = (m1_dni_pracy + m2_dni_pracy + m3_dni_pracy) + 1
lista_dyspozz = min(lista_dyspo)
mechanik_najszybciej_dostepny = lista_dyspozz + 1



tmp =  (f"Czas pracy mechanika 1: {m1_godziny}, Czas pracy mechanika 2: {m2_godziny}, Czas pracy mechanika 3: {m3_godziny}")
tmp1 = (f"Dni pracy mechanika 1: {m1_dni_pracy}, Dni pracy mechanika 2: {m2_dni_pracy}, Dni pracy mechanika 3: {m3_dni_pracy}")

print(tmp)
print(f"Liczba zlecen: , {liczba_zlecen}, Czas wykonania zlecen: "
          f"{lacznie_czas_naprawy}, {tmp1}")
print(f"Wszyscy mechanicy beda wolni za: {max_liczba_dni + 1}, "
          f"Najszybciej bedzie wolny mechanik: {lista_dyspozz}")


print(f"Wszyscy mechanicy beda wolni za: {max_liczba_dni + 1}, "
          f"Najbliższy mechanik będzie wolny w ciągu: {mechanik_najszybciej_dostepny} dni")

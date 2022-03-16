'''''''''
# wszystkie dane wpisujemy z cudzysłowiem

# nazwa klasy = wychowawca i uczniowie
# wychowawca = uczniowie wychowawcy
# nauczyciel = wychowawcy wszystkich klas, z którym ma zajęcia nauczyciel
# uczen = lekcje ucznia  i nauczyciele prowadzący lekcje
 '''''''''

import sys

file_path = r"baza_szkolna.txt"
with open(file_path, "r") as plik:
    wszystko = plik.read().split("\n")
if sys.argv[1] not in wszystko:
    print("Nie znaleziono w bazie")
    exit()

pobierz = input()
klasa_wych = {}
wychowawca = {}
nauczyciel = {}
nauczyciel_klasy = {}
uczniowie_wg_klas = {}
wychowawcy_lista = []
nauczyciele_lista = []
uczniowie_lista = []
uczniowie_klasy_slownik = {}

while True:
    if pobierz == "wychowawca":
        lista_tmp = []
        lista_tmp2 = []
        pobierz = input()
        wychowawcy_lista.append(pobierz)
        lista_tmp.append(pobierz)
        wych_klucz = pobierz
        pobierz = input()
        while len(pobierz) == 2:
            klasa_wych[pobierz] = lista_tmp
            lista_tmp2.append(pobierz)
            pobierz = input()
        wychowawca[wych_klucz] = lista_tmp2
    if pobierz == "nauczyciel":
        lista_tmp = []
        lista_tmp2 = []

        pobierz = input()
        naucz_imie = pobierz
        nauczyciele_lista.append(pobierz)
        lista_tmp2.append(naucz_imie)
        pobierz = input()
        lista_tmp.append(pobierz)
        lista_tmp2.append(pobierz)
        lista_tmp2.reverse()
        pobierz = input()
        while len(pobierz) == 2:
            if pobierz not in nauczyciel_klasy.keys():
                lista_tmp.append(pobierz)
                nauczyciel_klasy[pobierz] = lista_tmp2
                nauczyciel[naucz_imie] = lista_tmp
                pobierz = input()
            if pobierz in nauczyciel_klasy.keys():
                duplikat_klucz = nauczyciel_klasy[pobierz]
                lista_duplikat = duplikat_klucz + lista_tmp2
                nauczyciel_klasy[pobierz] = lista_duplikat
                lista_tmp.append(pobierz)
                nauczyciel[naucz_imie] = lista_tmp
                pobierz = input()
    if pobierz == "uczen":
        tmp = []
        uczen_imie = input()
        uczen_klasa = input()
        uczniowie_lista.append(uczen_imie)
        tmp.append(uczen_imie)
        uczniowie_klasy_slownik[uczen_imie] = uczen_klasa
        if uczen_klasa not in uczniowie_wg_klas.keys():
            uczniowie_wg_klas[uczen_klasa] = tmp
        elif uczen_klasa in uczniowie_wg_klas.keys():
            lista_uczniow_w_klasie = uczniowie_wg_klas[uczen_klasa]
            dodanie_do_klasy = lista_uczniow_w_klasie + tmp
            uczniowie_wg_klas[uczen_klasa] = dodanie_do_klasy
        pobierz = input()
        if pobierz == "koniec":
            break

if len(sys.argv[1]) == 2:
    if sys.argv[1] not in klasa_wych.keys():
        print()
        print("Klasa", sys.argv[1], "nie ma wychowawcy")
        print("Uczniowie", sys.argv[1], ": ", uczniowie_wg_klas[sys.argv[1]])
        exit()
    elif sys.argv[1] in uczniowie_klasy_slownik.values():
        print()
        print("Wychowawca", sys.argv[1], ": ", klasa_wych[sys.argv[1]])
        print("Uczniowie", sys.argv[1], ": ", uczniowie_wg_klas[sys.argv[1]])
        exit()

if sys.argv[1] in wychowawcy_lista:
    uczniowie_wychowawcy_lst = []
    if sys.argv[1] in wychowawca.keys():
        for x in wychowawca[sys.argv[1]]:
            for uczniowie in uczniowie_wg_klas[x]:
                uczniowie_wychowawcy_lst.append(uczniowie)
        print()
        print("Uczniowie nauczyciela", sys.argv[1], ": ", uczniowie_wychowawcy_lst, end=", ")

if sys.argv[1] in uczniowie_klasy_slownik.keys():
    ttt = uczniowie_klasy_slownik.get(sys.argv[1])
    print("\nLekcje ucznia", sys.argv[1], "i nauczyciel przedmiotu:", nauczyciel_klasy[ttt])

if sys.argv[1] in nauczyciele_lista:
    klasy_nauczycieli = nauczyciel[sys.argv[1]]
    klasy_nauczycieli.pop(0)
    nauczyciele_lista_lst = []
    for element in klasy_nauczycieli:
        if element in klasa_wych:
            for klasy in klasa_wych[element]:
                nauczyciele_lista_lst.append(klasy)
        elif element not in klasa_wych:
            continue
    nauczyciele2 = set(nauczyciele_lista_lst)
    print("\nWychowawcy klas z którymi ma lekcje nauczyciel", sys.argv[1], ": ", list(nauczyciele2))


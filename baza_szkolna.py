'''''''''
# wszystkie dane wpisujemy z cudzysłowiem

# nazwa klasy = wychowawca i uczniowie
# wychowawca = uczniowie wychowawcy
# nauczyciel = wychowawcy wszystkich klas, z którym ma zajęcia nauczyciel
# uczen = lekcje ucznia  i nauczyciele prowadzący lekcje
 '''''''''

import sys

file_path = r"szkola.txt"
with open(file_path, "r") as plik:
    for linia in plik:
        wszystko = plik.read()
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

        pobierz = input()   #imię nauczyciela
        naucz_imie = pobierz
        nauczyciele_lista.append(pobierz)   # dodanie nauczycieli dla sprawdzenia sys.argv
        lista_tmp2.append(naucz_imie)

        pobierz = input()   # przedmiot nauczyciela
        lista_tmp.append(pobierz)
        lista_tmp2.append(pobierz)  #pobieranie przedmiotu nauczyciela
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
        uczniowie_lista.append(uczen_imie)  #dodanie ucznia do listy wszystkich uczniów (do sys.argv)
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


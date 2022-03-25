import os
import sys
import csv
import json
import pickle       # reader.py <src> <dst> <change1> <change2> ...

wczytaj_csv = sys.argv[1]
zapisz_jako = sys.argv[2]
wiersz = int(sys.argv[3])
kolumna = int(sys.argv[4])
wartosc = sys.argv[5]

sciezka_odczyt = os.path.dirname(wczytaj_csv)   # bez slasza: c:\users\mrc22\desktop, ze slaszem: ...\desktop\python
sciezka_zapis = os.path.dirname(zapisz_jako)

if os.path.isfile(wczytaj_csv): #sprawdzenie, czy istnieje plik do odczytu
    pass
else:
    if os.path.isdir(sciezka_odczyt):      #nie można dać do środka wczytaj_csv
        print()
        print(F"Podany plik nie istnieje. Zawartość katalogu [{sciezka_odczyt}]:",
                      "\n", os.listdir(sciezka_odczyt))
        print()
        exit()
    elif not os.path.isdir(sciezka_odczyt):
        print()
        print("Podana ścieżka nie istnieje")
        exit()

if os.path.isdir(sciezka_zapis):
    pass

else:
    try:    ## potrzebne try?
        print("Ścieżka do zapisu nie istnieje")
        print()
        print(F"Utworzyć [{zapisz_jako}] ?")
        tworzenie_sciezki = input("Tak/Nie""\n")    #stdin?

        if tworzenie_sciezki in ["Tak", "tak"]:
            os.makedirs(sciezka_zapis)
            print(F"Ścieżka {sciezka_zapis} została utworzona")
        elif tworzenie_sciezki in ["Nie", "nie"]:
            exit()
        else:
            print("Nieprawidłowa komenda")
            exit()

    except:
        print()
        print("Błędna ścieżka do zapisu")
        exit()

lista_tmp = []
def odczytaj_plik():
    global lista_tmp
    with open(wczytaj_csv, "r") as plik:
        for linia in csv.reader(plik):
            lista_tmp.append(linia)
    lista_tmp[wiersz][kolumna] = wartosc

if zapisz_jako.endswith(".csv"):    # endswith sprawdza rozszerzenie pliku
    odczytaj_plik()

    with open(zapisz_jako, "w", newline='') as plik:    #newline= zapobiega pustym enterom przy zapisywaniu
        writer = csv.writer(plik)
        writer.writerows(lista_tmp)

    print()
    with open(zapisz_jako, "r") as plik:
        for linia in csv.reader(plik):
            print(linia)
    print()
    exit()

elif zapisz_jako.endswith(".json"):
    odczytaj_plik()

    with open(zapisz_jako, "w") as plik:
        json.dump(lista_tmp, plik)

    print()
    with open(zapisz_jako, "r") as plik:
        for linia in json.load(plik):
            print(linia)
    print()
    exit()

elif zapisz_jako.endswith(".pickle"):
    odczytaj_plik()

    with open(zapisz_jako, "wb") as plik:
        pickle.dump(lista_tmp, plik)

    print()
    with open(zapisz_jako, "rb") as plik:
        print()
        for linia in pickle.load(plik):
            print(linia)
    print()
    exit()
else:
    print()
    print("Nieprawidłowe rozszerzenie pliku (.csv/.json/.pickle) \n  Plik nie został utworzony")

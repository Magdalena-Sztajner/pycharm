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

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
import csv
import json
import pickle       # reader.py <src> <dst> <change1> <change2> ...

from reader2_zmienne import Zmienne
from reader2_ispath import  IsPath
IsPath()
from reader2_OdczytCSV import OdczytCSV


class ZapiszWyswietlCSV(OdczytCSV):
    def __init__(self):
        Zmienne.__init__(self)
        OdczytCSV.__init__(self)
    def plik_CSV(self):
        with open(self.zapisz_jako, "w", newline='') as plik:
            writer = csv.writer(plik)
            writer.writerows(self.lista_tmp)
        with open(self.zapisz_jako, "r") as plik:
            for linia in csv.reader(plik):
                print(linia)
        exit()


class ZapiszWyswietlJSON(OdczytCSV):
    def __init__(self):
        Zmienne.__init__(self)
        OdczytCSV.__init__(self)
    def plik_JSON(self):
        with open(self.zapisz_jako, "w") as plik:
            json.dump(self.lista_tmp, plik)
        with open(self.zapisz_jako, "r") as plik:
            for linia in json.load(plik):
                print(linia)
        exit()


class ZapiszWyswietlPICKLE(OdczytCSV):
    def __init__(self):
        Zmienne.__init__(self)
        OdczytCSV.__init__(self)
    def plik_PICKLE(self):
        with open(self.zapisz_jako, "wb") as plik:
            pickle.dump(self.lista_tmp, plik)
        with open(self.zapisz_jako, "rb") as plik:
            print()
            for linia in pickle.load(plik):
                print(linia)
        exit()

zmienne = Zmienne()

if zmienne.zapisz_jako.endswith(".csv"):
    x = ZapiszWyswietlCSV()
    x.plik_CSV()

elif zmienne.zapisz_jako.endswith(".json"):
    x = ZapiszWyswietlJSON()
    x.plik_JSON()

elif zmienne.zapisz_jako.endswith(".pickle"):
    x = ZapiszWyswietlPICKLE()
    x.plik_PICKLE()

else:
    print("Nieprawidłowe rozszerzenie pliku (.csv/.json/.pickle) \n  Plik nie został utworzony")

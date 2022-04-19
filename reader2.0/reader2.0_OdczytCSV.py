import csv
from read2_zmienne import Zmienne

class OdczytCSV(Zmienne):
    def __init__(self):
        Zmienne.__init__(self)
        with open(self.wczytaj_csv, "r") as plik:
            for linia in csv.reader(plik):
                self.lista_tmp.append(linia)
        self.lista_tmp[self.wiersz][self.kolumna] = self.wartosc

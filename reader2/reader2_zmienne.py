import sys
import os

class Zmienne():
    def __init__(self):
        self.wczytaj_csv = sys.argv[1]
        self.zapisz_jako = sys.argv[2]
        self.wiersz = int(sys.argv[3])
        self.kolumna = int(sys.argv[4])
        self.wartosc = sys.argv[5]
        self.lista_tmp = []
        self.sciezka_odczyt = os.path.dirname(self.wczytaj_csv)
        self.sciezka_zapis = os.path.dirname(self.zapisz_jako)
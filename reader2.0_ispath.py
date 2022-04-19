import sys
import os
from read2_zmienne import Zmienne


class IsPath(Zmienne):
    def __init__(self):
        Zmienne.__init__(self)
        if os.path.isfile(self.wczytaj_csv):
            pass
        else:
            if os.path.isdir(self.sciezka_odczyt):
                print(F"Podany plik nie istnieje. Zawartość katalogu [{self.sciezka_odczyt}]:",
                      "\n", os.listdir(self.sciezka_odczyt))
                exit()
            elif not os.path.isdir(self.sciezka_odczyt):
                print("Podana ścieżka nie istnieje")
                exit()

        if os.path.isdir(self.sciezka_zapis):
            pass
        else:
            try:
                print("Ścieżka do zapisu nie istnieje")
                print(F"Utworzyć [{self.zapisz_jako}] ?")
                tworzenie_sciezki = input("Tak/Nie""\n")  # stdin?

                if tworzenie_sciezki in ["Tak", "tak"]:
                    os.makedirs(self.sciezka_zapis)
                    print(F"Ścieżka {self.sciezka_zapis} została utworzona")
                elif tworzenie_sciezki in ["Nie", "nie"]:
                    exit()
                else:
                    print("Nieprawidłowa komenda")
                    exit()
            except:
                print("Błędna ścieżka do zapisu")
                exit()
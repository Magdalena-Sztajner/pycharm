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
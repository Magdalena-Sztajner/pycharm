'''''''''
<plik.py> <plik.txt> <akcja> (dla konto, stan)
<plik.py> <plik.txt> <akcja> <przedmiot1> ... (dla magazyn)
<plik.py> <plik.txt> <akcja> <zakres1> <zakres2>(opcjonalnie) (dla przegląd)
<plik.py> <plik.txt> <akcja> <przedmiot> <cena> <szt.> (dla zakup, sprzedaż)

python acc3_sal.py acc3.txt saldo 500 zwrot
python acc3_zak.py acc3.txt zakup laptop 2000 2
python acc3_sprz.py acc3.txt sprzedaz laptop 3000 1
python acc3_mag.py acc3.txt stan  
python acc3_prze.py acc3.txt przeglad 0 2
'''''''''


import sys
import acc3
from acc3_sal import sal
from acc3_zak import zak
from acc3_sprz import sprz
from acc3_kon import kon
from acc3_mag import mag
from acc3_prze import prze



class Manager1:
    def __init__(self):
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb
        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)


menedzer = Manager1()


@menedzer.assign("saldo")
def saldo(menedzer):
    print("Wykonuję akcję: saldo")
    sal()

@menedzer.assign("zakup")
def zakup(menedzer):
    print("Wykonuję akcję: zakup")
    zak()

@menedzer.assign("sprzedaz")
def sprzedaz(menedzer):
    print("Wykonuję akcję: sprzedaz")
    sprz()

@menedzer.assign("magazyn")
def magazyn(menedzer):
    print("Wykonuję akcję: magazyn")
    mag()

@menedzer.assign("przeglad")
def przeglad(menedzer):
    print("Wykonuję akcję: przeglad")
    prze()

@menedzer.assign("konto")
def konto(menedzer):
    print("Wykonuję akcję: konto")
    kon()

@menedzer.assign("stan")
def stan(menedzer):
    print("Wykonuję akcję: stan magazynu")
    mag()

menedzer.execute(sys.argv[2])


# menedzer.actions = {
#     "saldo":sal,
#     "zakup":zak,
#     "konto":kon,
#     "magazyn":mag,
#     "stan":mag,
#     "przeglad":prze,
# }

from acc3 import historia, saldo
#
# for element in historia:
#     print(element)

# print(saldo, historia)



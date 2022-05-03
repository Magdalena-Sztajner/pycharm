'''''''''
<plik.py> <plik.txt> <akcja> (dla konto, stan)
<plik.py> <plik.txt> <akcja> <przedmiot1> ... (dla magazyn)
<plik.py> <plik.txt> <akcja> <zakres1> <zakres2>(opcjonalnie) (dla przegląd)
<plik.py> <plik.txt> <akcja> <przedmiot> <cena> <szt.> (dla zakup, sprzedaż)

'''''''''

import sys
import accountant_3_historia
from accountant_3_saldo import sal
from accountant_3_zakup import zak
from accountant_3_sprzedaz import sprz
from accountant_3_konto import kon
from accountant_3_magazyn import mag
from accountant_3_przeglad import prze



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




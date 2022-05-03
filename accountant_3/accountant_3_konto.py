import sys
import accountant_3_historia

from accountant_3_historia import saldo

def kon():
    if sys.argv[2] == "konto":
        print()
        print("Konto:", saldo)
        print()

import accountant_3_Manager
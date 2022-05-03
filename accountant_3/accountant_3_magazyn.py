

import sys
import accountant_3_historia
from accountant_3_historia import magazyn

def mag():
    if sys.argv[2] == "magazyn":
        print()
        print("Magazyn: ", end="")
        for produkt in sys.argv[3:]:
            print(f"{produkt} {magazyn.get(produkt, 0)} szt., ", end="", )

    if sys.argv[2] == "stan":
        for k, v in magazyn.items():
            print(k, v)


import accountant_3_Manager
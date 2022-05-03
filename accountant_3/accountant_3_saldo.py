import sys

import acc3
from acc3 import hist_tmp, historia, dodawanie_historii




def sal():
    from acc3 import saldo, hist_tmp
    kwota = int(sys.argv[3])
    komentarz = sys.argv[4]
    hist_tmp.append(sys.argv[2])
    dodawanie_historii(sys.argv[2])
    hist_tmp.append(kwota)
    dodawanie_historii(kwota)
    hist_tmp.append(komentarz)
    dodawanie_historii(komentarz)

    historia.append(hist_tmp)
    hist_tmp = []

    saldo = saldo + kwota



import man












# print()
# print()
# for element in historia:
#     print(element)
#
# print()
# print("Saldo:", saldo)
# print()
# print("Magazyn:", magazyn)
#

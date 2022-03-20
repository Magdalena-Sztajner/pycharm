import sys
import accountant_2_historia

from accountant_2_historia import saldo, dozwolone_komendy

dozwolone_komendy()

if sys.argv[2] == "konto":
    print()
    print("Konto:", saldo)
    print()
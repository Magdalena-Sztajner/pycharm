import sys
import accountant_2_historia

from accountant_2_historia import historia, dozwolone_komendy

dozwolone_komendy()

if sys.argv[2] == "historia":
    for element in historia:
        print(element)

if sys.argv[2] == "przeglad":
    przeglad_od = int(sys.argv[3])
    try:
        przeglad_do = int(sys.argv[4])
        print()
        print(F"Przeglad historii [od: {przeglad_od} do: {przeglad_do}]:")
        for element in historia[przeglad_od:przeglad_do]:
            print(element)
        print()

    except:
        print()
        print("Przeglad historii:", historia[przeglad_od])
        print()





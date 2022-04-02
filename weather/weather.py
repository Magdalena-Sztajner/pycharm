'''''''''
OPEN WEATHER (for 7 days):
https://openweathermap.org/api/one-call-api

'''''''''

import requests
from datetime import datetime, timedelta
import json
import sys
import os


try:
    API_ARGV = sys.argv[1]
    data_argv = sys.argv[2]

except:
    API_ARGV = sys.argv[1]
    date = datetime.today().date()
    data_argv = str(date + timedelta(days=1))
    # print(date + timedelta(days=1))

wwa_lat = 52.2319581
wwa_lon = 21.0067249
API_url = F"https://api.openweathermap.org/data/2.5/onecall?lat={wwa_lat}&lon={wwa_lon}&exclude=hourly,minutely,alerts&appid={API_ARGV}"

pogoda = {}

if os.stat("historia_pogody.json").st_size > 0:
    print("Sprawdzam historię...")
    with open("historia_pogody.json", "r") as plik:
        sprawdzenie_historii = json.load(plik)
        wyszukiwanie = sprawdzenie_historii.get(data_argv)
        if wyszukiwanie:
            print(F"{data_argv}: {wyszukiwanie}")
            exit()
        else:
            print("Wysyłam zapytanie...")

else:
    print("Wysyłam zapytanie...")

odpowiedz = requests.get(API_url)
# pprint.pprint(odpowiedz.json())             # pprint.pprint(odpowiedz.json()["list"][3]["weather"])
zapytanie = odpowiedz.json()  # zapytanie = odpowiedz.json()["list"][1]["weather"]

for dane in zapytanie["daily"]:
    data_format = datetime.fromtimestamp(dane["dt"]).date()  # przeszukiwanie po dacie
    dzien = str(data_format)  # zmiana formatu
    if dzien == data_argv:
        rain = dane.get("rain")
        if rain:
            print(F"{data_argv}: pada")
            pogoda[dzien] = ["pada"]
        else:
            pogoda[dzien] = ["nie pada"]
            print(F"{data_argv}: nie pada")

if data_argv not in pogoda:
    print("Brak informacji")
    exit()
try:
    with open("historia_pogody.json", "r") as plik:
        aktualizacja_slownika = json.load(plik) # wypakowaywanie słownika z pliku i aktualizowanie o dane ze słownika "pogoda"
        aktualizacja_slownika.update(pogoda)

    with open("historia_pogody.json", "w") as plik:  # zapisywanie uaktualniownego słownika do pliku
        json.dump(aktualizacja_slownika, plik, sort_keys=True, indent=4, separators=(',', ': '))

except:
    with open("historia_pogody.json", "w") as plik:
        json.dump(pogoda, plik, sort_keys=True, indent=4, separators=(',', ': '))

# OPEN WEATHER:

import pprint
import requests
from datetime import datetime, timedelta
import json
import csv
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

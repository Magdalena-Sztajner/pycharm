'''''''''
    wf[date] da odpowiedź na temat pogody dla podanej daty (według specyfikacji z poprzedniego zadania)
    wf.items() zwróci generator tupli w formacie (data, pogoda) dla już zcache’owanych rezultatów przy wywołaniu
    wf to iterator zwracający wszystkie daty, dla których znana jest pogoda

'''''''''


import os
import json
import requests
from datetime import datetime



class WeatherForecast():

    def __init__(self, klucz_API):
        self.klucz_API =  klucz_API
        self.pogoda = {}

        wwa_lat = 52.2319581
        wwa_lon = 21.0067249
        API_URL = F"https://api.openweathermap.org/data/2.5/onecall?lat={wwa_lat}&lon={wwa_lon}&exclude=hourly,minutely,alerts&appid={klucz_API}"
        odpowiedz = requests.get(API_URL)
        self.zapytanie = odpowiedz.json()

    def historia_zapis(self):
        pogoda_ = wf.pogoda

        try:
            with open("historia_pogody.json", "r") as plik:
                aktualizacja_historii_pogody = json.load(plik)
                aktualizacja_historii_pogody.update(pogoda_)

            with open("historia_pogody.json", "w") as plik:
                json.dump(aktualizacja_historii_pogody, plik, sort_keys=True, indent=4, separators=(',', ': '))

        except:
            with open("historia_pogody.json", "w") as plik:
                json.dump(pogoda_, plik, sort_keys=True, indent=4, separators=(',', ': '))
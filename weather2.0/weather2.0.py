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
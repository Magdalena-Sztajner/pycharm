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


    def __iter__(self):
            for x in self.zapytanie["daily"]:
             data_format = datetime.fromtimestamp(x["dt"]).date()
             dzien = str(data_format)
             if not dzien:
              break
             else:
              yield dzien

    def __getitem__(self, podany_dzien):

        if os.stat("historia_pogody.json").st_size > 0:
            print("Sprawdzam historię...")
            with open("historia_pogody.json", "r") as plik:
                sprawdzenie_historii = json.load(plik)
                wyszukiwanie = sprawdzenie_historii.get(podany_dzien)
                if wyszukiwanie:
                    print(F"{podany_dzien}: {wyszukiwanie}")
                    exit()
                else:
                    print("Wysyłam zapytanie...")
        else:
            print("Wysyłam zapytanie...")

        for x in self.zapytanie["daily"]:
            data_format = datetime.fromtimestamp(x["dt"]).date()
            dzien = str(data_format)

            if podany_dzien == dzien:
                rain = x.get("rain")
                if rain:
                    self.pogoda[dzien] = ["pada"]
                    self.historia_zapis()
                    return (F"{podany_dzien}: pada")

                else:
                    self.pogoda[dzien] = ["nie pada"]
                    self.historia_zapis()
                    return (F"{podany_dzien}: nie pada")

        if podany_dzien not in dzien:
            print("Brak informacji dla podanej daty")
            exit()

    def items(self):
        with open("historia_pogody.json", "r") as plik:
            pogoda_historia = json.load(plik)
            for x,y in pogoda_historia.items():
                yield x,y



wf = WeatherForecast()



# # 1:
# for dane in wf:
#     print(dane)

# # 2:
# print(wf["2022-04-17"])

# # 3:
# for data in wf.items():
#     print(data)
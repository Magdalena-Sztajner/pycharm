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


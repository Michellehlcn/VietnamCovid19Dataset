import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import ssl
import urllib3
import html5lib
from lxml import html
import pandas as pd
import json
from pandas.io.json import json_normalize

import csv
import urllib.request 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = "https://tiemchungcovid19.gov.vn/api/public/dashboard/vaccination-statistics/all"
page = requests.get(url , verify=False)
soup = BeautifulSoup(page.text, 'html.parser')

result = json.loads(soup.text)
df = pd.json_normalize(result)
df.to_csv(r'/Users/michelle/Desktop/vaxx.csv', encoding='UTF-16')


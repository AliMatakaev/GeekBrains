import requests
import pprint
import json

def currency_rates(a):
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(URL)
    dict_json = json.loads(response.text)
    print(dict_json['Valute'][a]['Value'])

currency_rates('EUR')
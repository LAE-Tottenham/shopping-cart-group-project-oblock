import math

exchange_rates = {
    'USD': 1.31,
    'EUR': 1.20,
    'CAD': 1.81,
    'CHF': 1.12,
    'CNY': 9.31
}

def check_currency_exists(currency):
    while currency not in exchange_rates: # Checks if the currency is in the dictionary
        currency = input("Please input an accepted currency - ") # Will make the user enter a currency that exists in the 
    return currency

def currency_convert(new_c, amount):
    ConvertAmount = exchange_rates[new_c] # Takes the conversion rate from dictionary of currencies
    NewAmount = amount * ConvertAmount # Converts the original amount to the new amount
    return round(NewAmount, 2)

import requests

def get_currency_conversion(code):
    url = f"https://v6.exchangerate-api.com/v6/a4dcacb3910c8ea780b67438/pair/GBP/{code}"
    response = requests.get(url)
    data = response.json()
    return(data['conversion_rate'])
    

code = input("Enter code please ")
niner = get_currency_conversion(code)
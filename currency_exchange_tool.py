import requests

def get_currency_conversion(code):
    code = code.upper()
    try:
        url = f"https://v6.exchangerate-api.com/v6/a4dcacb3910c8ea780b67438/pair/GBP/{code}"
        response = requests.get(url)
        data = response.json()
        return(data['conversion_rate'])
    except KeyError:
        code = input("invalid currency code, type in again. ")
        return get_currency_conversion(code)


def currency_convert(rate, amount):
    NewAmount = amount * rate # Converts the original amount to the new amount
    return round(NewAmount, 2)



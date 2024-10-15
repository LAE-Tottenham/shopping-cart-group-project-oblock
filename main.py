from currency_exchange_tool import currency_convert
from shop_functions import start_shop
from pyfiglet import Figlet

font = Figlet(font='alligator')

while True:
    print(font.renderText('Please select what you would like to buy'))
    items_to_buy = start_shop()

    # blah

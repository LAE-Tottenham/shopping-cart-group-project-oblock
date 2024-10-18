
from currency_exchange_tool import currency_convert
from shop_functions import *
from pyfiglet import Figlet
from currency_exchange_tool import *

font = Figlet(font='alligator')


print(font.renderText('Welcome to my shop'))
main()

# cc = input("Enter currency code please - ")
# ccr = get_currency_conversion(cc)
# print(ccr)

# actual_cost = currency_convert(ccr, total_cost)
# print(actual_cost)
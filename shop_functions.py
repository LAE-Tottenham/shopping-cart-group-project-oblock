from InquirerPy import inquirer
import pickle
import os
from Deliverys import runDelivery
from currency_exchange_tool import *

def make_account():
    username = inquirer.text(message="Enter your username: ").execute()
    password = inquirer.text(message="Enter your password: ").execute()
    if os.path.getsize("logins.pkl") > 0:
        with open('logins.pkl', 'rb') as f:
                login_list = pickle.load(f)
        login_list.append([username, password])
    else:
        login_list = [[username,password]]
    with open('logins.pkl', 'wb') as f:
        pickle.dump(login_list, f)
    return username, password

def log_in():
    if os.path.getsize("logins.pkl") == 0:
        print("No accounts currently")
        print("If you would like to continue, make an account with us.")
        return make_account()
    else:
        with open('logins.pkl', 'rb') as f:
                login_list = pickle.load(f)
        username_input = inquirer.text(message="Enter your username: ").execute()
        password_input = inquirer.text(message="Enter your password: ").execute()
        for login in login_list:
            if login[0] == username_input and login[1] == password_input:
                username = login[0]
                password = login[1]
                print("Account found!!!!!!")
                print(username, password)
                return username, password
        login_or_make = inquirer.select(
            message = "Try logging in again or make a new account",
            choices = ["Try logging in again", "Make account"] ,
        ).execute()
        
        if login_or_make == "Try logging in again":
            return log_in()
        else:
            return make_account()



def make_order(username, password):
    inventory = {
        'Bread': 1.20,
        'Milk': 1.15,
        'Chocolate': 0.5,
        'Water' : 1,
        'Oil' : 1.50,
        'Bacon': 1.50,
        'Cheese': 0.99,
        'Onion': 40,
        'Rice' : 1.50,
        'Egg' : 1.20,
    }

    item_choices = {}
    for i in inventory: # creates a dictionary that links the product and description with the product name
        item_choices[f"{i} for £{inventory[i]}"] = i
        
    total_cost = 0
    items = []
    while True:
        item_choice = inquirer.select(
            message = "What would you like to buy?",
            choices = item_choices.keys(),
        ).execute() # allows user to input which item they would like to choose
        
        items.append(item_choices[item_choice]) # adds the chosen item to list of items bought
        total_cost += inventory[item_choices[item_choice]] # Adds price of item to total
        
        buy_again = inquirer.select(
            message = "Would you like to buy anything else",
            choices = ["Yes", "No"],
        ).execute()

        if buy_again == "No":
            print(items, total_cost)
            break
    if os.path.getsize("past_orders.pkl") > 0:
        with open('past_orders.pkl', 'rb') as f:                
            order_list = pickle.load(f)
        order_list.append([username, password, items])
    else:
        order_list = [[username,password, items]]
    with open('past_orders.pkl', 'wb') as f:
        pickle.dump(order_list, f)
    
    # return basket_cost
    


def start_shop():
    make_or_access = inquirer.select(
        message = "Make a new account or use a current one?",
        choices = ["Make a new account", "Use current account"]
    ).execute()

    if make_or_access == "Make a new account":
        username, password = make_account()
        return make_order(username, password)
    else:
        username, password = log_in()
        return make_order(username, password)

def access_order_history():
    if os.path.getsize("past_orders.pkl") == 0:
        print("No previous orders.")
        main()
    else:
        with open('past_orders.pkl', 'rb') as f:
                login_list = pickle.load(f)
        username_input = inquirer.text(message="Enter your username: ").execute()
        password_input = inquirer.text(message="Enter your password: ").execute()
        prev_orders = []
        for i in range(len(login_list)):
            if login_list[i][0] == username_input and login_list[i][1] == password_input:
                prev_orders.append(login_list[i][2])
        print(f"Your precious orders are: {prev_orders}")


def main():
    menu_choice = inquirer.select(
        message = "Choose what you want to do",
        choices = ["Make order", "Access shopping history"],
    ).execute()
    if menu_choice == "Make order":
        basket_cost = start_shop()
        
        delivery_cost = runDelivery()

        total_cost = basket_cost + delivery_cost
        
        cc = input("Enter currency code please - ")
        ccr = get_currency_conversion(cc)
        actual_cost = currency_convert(ccr, total_cost)
        print(actual_cost)
    else:
        access_order_history()
     
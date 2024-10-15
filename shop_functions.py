from InquirerPy import inquirer

inventory = {
    'Bread': 1.20,
    'Milk': 1.15,
    'Chocoloate': 0.5,
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

def start_shop():
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

    return {
        'items': items,
        'total_cost': total_cost
    }
        
        

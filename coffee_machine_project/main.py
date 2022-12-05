
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



# TODO: check resources sufficient?
def are_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True

# TODO: proccess Coins 
def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please insert coins.')
    total = int(input(f'How many quarters?: ')) * 0.25
    total += int(input(f'How many dimes?: ')) * 0.1
    total += int(input(f'How many nickles?: ')) * 0.05
    total += int(input(f'How many pennies?: ')) * 0.01
    return total



# TODO: check transaction successful

def check_transaction(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry thats not enough money. Money refunded.')
        return False


# TODO: make coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕. Pain and suffering was endured for you to enjoy this shit...')




# TODO: print program again


programm_is_running = True
while programm_is_running:

    # TODO: ask user what he would like

    user_input = input('What would you like? (espresso/latte/cappuccino): ')

    if user_input == 'off':
        programm_is_running = False
        
# TODO: print report
    elif user_input == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[user_input]
        if are_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                make_coffee(user_input, drink['ingredients'])

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def is_resources_sufficient(drink_ingredients):
    """
    Return True when the order can be made, return False when the ingredients are insufficient
    """
    for key in drink_ingredients:
        if drink_ingredients[key] >= resources[key]:
            print(f"Sorry!there is no enough {key}")
            return False
    return True


def process_coins():
    """
    returns the total amount of the coins that were inserted
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Return True when the payment is accepted, or False if money is insufficient
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry!that's not enough money.")
        return False


def make_coffee(drink_name, order_ingredient):
    """
    Deduct the required ingredients from the resources.
    """
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
        print(f"Here is your {drink_name}")



is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        show_report()
    # It has to be any drinks from the menue
    else:
        # Get the entire dictionary value of the particular drink
        drink = MENU[order]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])




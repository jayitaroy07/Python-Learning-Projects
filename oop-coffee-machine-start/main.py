from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    coffee_menu = Menu()
    coffee_make = CoffeeMaker()
    money_processing = MoneyMachine()
    print(coffee_menu.get_items())
    order = input("What would you like? Please select something from the menu: ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_make.report()
    # It has to be any drinks from the menue
    else:
        # Get the ingredients associated with the drink
        drink = coffee_menu.find_drink(order)
        if coffee_make.is_resource_sufficient(drink):
            if money_processing.make_payment(drink.cost):
                coffee_make.make_coffee(drink)
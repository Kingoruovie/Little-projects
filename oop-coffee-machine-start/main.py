from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_resources = CoffeeMaker()
money_on_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    option = input(f"What would you like?:({menu.get_items()}): ").lower()
    if option == "report":
        machine_resources.report()
        money_on_machine.report()
    elif option == "off":
        print("Ready for Maintenance")
        is_on = False
    elif option == "latte" or option == "espresso" or option == "cappuccino":
        if machine_resources.is_resource_sufficient(menu.find_drink(option)) and \
                money_on_machine.make_payment(menu.find_drink(option).cost):
            machine_resources.make_coffee(menu.find_drink(option))
    else:
        print("Wrong choice of words")

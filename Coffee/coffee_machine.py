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


def water(diction):
    quantity_of_water = MENU[diction]['ingredients']['water']
    return quantity_of_water


def coffee(diction):
    quantity_of_coffee = MENU[diction]['ingredients']['coffee']
    return quantity_of_coffee


def cost(diction):
    cost_of_coffee = MENU[diction]['cost']
    return cost_of_coffee


def milk(diction):
    if "milk" in MENU[diction]['ingredients']:
        quantity_of_milk = MENU[diction]['ingredients']['milk']
    else:
        quantity_of_milk = 0
    return quantity_of_milk


def resource_check(machine_resource, option):
    water_true = False
    coffee_true = False
    milk_true = False
    check_true = True
    if machine_resource['water'] > water(option):
        water_true = True
    if machine_resource['coffee'] > coffee(option):
        coffee_true = True
    if machine_resource['milk'] > milk(option):
        milk_true = True
    if water_true and coffee_true and milk_true:
        return check_true
    else:
        return not check_true


def money_calc(penn, nick, dim, quart):
    total = 0.01 * penn + 0.05 * nick + 0.1 * dim + 0.25 * quart
    return total


def money_check(customer_cash, actual_cost):
    if customer_cash < actual_cost:
        print('Money is not enough. Money refunded')
    if customer_cash > actual_cost:
        extra_cash = customer_cash - actual_cost
        print(f"You have got a change of ${round(extra_cash, 2)}")


def bol_money_check(customer_cash, actual_cost):
    money_true = True
    if customer_cash < actual_cost:
        money_true = False
    return money_true


money_in_machine = 0
is_true = True
while is_true:
    decision = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if decision == "report":
        print(f"We have the following \nWater:{resources['water']}ml \nMilk:{resources['milk']}ml "
              f"\nCoffee:{resources['coffee']}g \nMoney:${money_in_machine}")

    elif decision == "off":
        is_true = False

    elif decision == "espresso" or decision == "latte" or decision == "cappuccino":
        if resource_check(resources, decision):
            print("Your coin, please")
            penny = int(input("How many penny: "))
            nickel = int(input("How many nickel: "))
            dime = int(input("How many dime: "))
            quarter = int(input("How many quarter: "))
            customers_money = money_calc(penny, nickel, dime, quarter)
            cost_of_var = cost(decision)
            if bol_money_check(customers_money, cost_of_var):
                money_check(customers_money, cost_of_var)
                resources['water'] -= water(decision)
                resources['milk'] -= milk(decision)
                resources['coffee'] -= coffee(decision)
                money_in_machine += cost(decision)
                print(f"Here is your {decision} ☕... Please enjoy")
            elif not bol_money_check(customers_money, cost_of_var):
                money_check(customers_money, cost_of_var)

        elif not resource_check(resources, decision):
            print('Please, sorry for the disappointment, not enough ingredient')

    else:
        print("WRONG CHOICE")

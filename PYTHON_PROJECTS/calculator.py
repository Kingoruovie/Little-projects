from calcu_art import logo


import os
#creating functions for calculation
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

def root(n1, n2):
    return n1 ** (1/n2)

operations = {
    "+":add,
    "*":multiply,
    "-":subtract,
    "/":divide,
    "**":exponent,
    "/**":root
}
def calculator():
    print(logo)
    print("WELCOME TO MINI CALCULATOR")
    first_number = float(input("\nWhat is your first number? "))


    should_continue = True
    while should_continue:
        for operation in operations:
            print(operation)
        choosen_operation = input("Select an operation from above? ")
        second_number = float(input("\nWhat is the next number? "))
        calculation_function = operations[choosen_operation]
        answer = calculation_function(first_number, second_number)

        print(f"{first_number} {choosen_operation} {second_number} = {answer}\n")

        options = input("Type yes to contnue with previous answer and no not to continue with it: ")

        if options == "yes":
            first_number = answer
        else:
            os.system('cls')
            calculator()

calculator()
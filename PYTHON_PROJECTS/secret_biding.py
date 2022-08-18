import os
import biding_logo

print(biding_logo.logo)

biders_dictionary = {}

def add_new_bider(name_of_bider, amount_bidded):
    biders_dictionary[name_of_bider] = amount_bidded



is_true = True
while is_true:
    name = input("What is your name? ")
    amount = int(input("What is your bidding amount? $"))
    add_new_bider(name, amount)
    biders = input("Are there any other biders? type 'yes' or 'no': ")
    os.system('cls')
    if biders == "no":
        is_true = False
        highest = 0
        for highest_bidder  in biders_dictionary:
            bid = biders_dictionary[highest_bidder]
            if bid > highest:
                highest = bid
                winner = highest_bidder
        print(f"The winner is {winner} with a bid of ${highest}")


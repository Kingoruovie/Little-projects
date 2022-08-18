#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_letters = ''
random_numbers = ''
random_symbols = ''

for x in range(1, nr_letters + 1):
  random_choice_of_letters = random.choice(letters)
  random_letters += random_choice_of_letters

for y in range(1, nr_numbers + 1):
  random_choice_of_numbers = random.choice(numbers)
  random_numbers += random_choice_of_numbers

for z in range(1, nr_symbols + 1):
  random_choice_of_symbols = random.choice(symbols)
  random_symbols += random_choice_of_symbols

password = random_letters + random_numbers + random_symbols

#shuffling password
list_password = list(password)
random.shuffle(list_password)

#ths can be done using a for loop, joining characters in a list to form a string
password = ''.join(list_password)


print(f'Your password is: {password}')
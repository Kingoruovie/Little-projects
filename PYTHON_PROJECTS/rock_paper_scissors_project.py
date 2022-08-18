rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

number = input('"What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors" ')

#code blocks determining error in inputing wrong number
if int(number) not in range(0, 3):
    print('you type and invalid number')
    print()

#code blocks giving the randomization procedure
import random

game_choice = [rock, paper, scissors]
random_guess = random.choice(game_choice)

#logic determining image for any value in our range taken
my_choice = 0
if number == '0':
  my_choice = rock
elif number == '1':
  my_choice = paper
elif number == '2':
  my_choice = scissors
else:
    my_choice = 'invalid and no image to display'

#image of choice's made by human and computer
print(f'YOUR CHOICE\n{my_choice}\n')
print(f"COMPUTER'S CHOICE\n{random_guess}\n")

#logic behind the winning and losing in the game
if my_choice == random_guess:
    print("It is a draw!")
elif my_choice == rock and random_guess == scissors:
    print("You won!")
elif my_choice == scissors and random_guess == paper:
    print("You won!")
elif my_choice == paper and random_guess == rock:
    print("You won!")
elif my_choice == rock and random_guess == paper:
    print("Oh No! You loss")
elif my_choice == scissors and random_guess == rock:
    print("Oh No! You loss")
elif my_choice == paper and random_guess == scissors:
    print("Oh No! You loss")
else:
    print("Oh No! You loss for inputing an invalid number")

print()

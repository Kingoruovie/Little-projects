#Importing all the libraries and modules used in the the game project
import os
import random
from hangman_art import *
from hangman_words import word_list

#Logo of the game outputted in the terminal by the print() function
print(logo)

#Generation of random word by the choice() function
random_word = random.choice(word_list)


print(f"The random word is {random_word}")

#Created variable for number of chances given in the game
lives = 6

#Created list of underscores for the display of the result of the word we are guessing
word_in_list = []
for n in range(len(random_word)):
    word_in_list.append("_")

#A bolean value for our while loop
#Note that this is one reasonable way to make a while loop, i.e., using bolean and if together
end_of_game = False

#THE MECHANICS OF THE GAME
#While loop for continous process until word is gotten or chances are exhausted
while not end_of_game:
    #guess made by user
    guess = input("Guess a letter: ")
    #to clear screen of prompt
    os.system('cls')
    #checking if letter was already guessed
    if guess in word_in_list:
        print(f"The letter '{guess}' is already found")
    #now when it is not
    elif guess not in random_word:
        print(f"The letter {guess} is not in word")
        lives = lives - 1
    else:
        #A for loop to go through word and checking if letter is in word
        for position in range(len(random_word)):
            if guess == random_word[position]:
                word_in_list[position] = random_word[position]
        #If staement for live reduction
        if guess not in random_word:
            lives = lives - 1
        print(stages[lives])
        print(f"{' '.join(word_in_list)}")
        #If statement to end game when life is finished
        if lives == 0:
            end_of_game = True
            print("You loss")
        #If statement to end game if no more display of underscore in word
        if "_" not in word_in_list:
            end_of_game = True
            print("You win")

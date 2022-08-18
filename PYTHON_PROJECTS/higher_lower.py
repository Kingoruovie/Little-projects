import random
import os
import higher_and_lower_art
import game_data

compare_A = random.choice(game_data.data)
compare_B = random.choice(game_data.data)

def compare():
    if compare_A['follower_count'] > compare_B['follower_count']:
        return compare_A      
    else:
        return compare_B

condition_satisfied = True
score = 0
    
while condition_satisfied:
    print(higher_and_lower_art.logo)
    print(f"Your score is: {score}")
    print(f"\nCOMPARE A: {compare_A['name']}, a {compare_A['description']} from {compare_A['country']}\n")
    print(higher_and_lower_art.vs + "\n")
    print(f"COMPARE B: {compare_B['name']}, a {compare_B['description']} from {compare_B['country']}\n")


    highest_count = input("Which of the above has more followers count? A or B: ").upper()
    
    
    winner = compare()
    if winner == compare_A:
        winner_option = 'A'
    else:
        winner_option = 'B'

    if highest_count == winner_option:
        score = score + 1
        compare_A = winner
        compare_B = random.choice(game_data.data)
        os.system('cls')
      
    else:
        condition_satisfied = False
        print("You loss")
        print("GAME OVER")


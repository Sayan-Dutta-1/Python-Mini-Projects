from game_data import data
from game_art import logo, vs
import random
import os
#use this if you are using vs code to clear previous inputs in the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

def random_choice():
    return random.choice(data)

def check_answer (guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a" # It is same as if guess == "a"   return True  (so return guess == "a" returns a boolean value)
    else:
        return guess == "b"      
account_b = random_choice()
continue_game = True  
score = 0                                       
while continue_game:
    def format_data(account):
        name = account["name"]
        description = account["description"]
        country = account["country"]
        return f"{name} a {description} from {country}."
    account_a = account_b
    account_b = random_choice()
    if account_a == account_b:
        account_b = random_choice()
    print(f"Compare------\nOption A :- {format_data(account_a)}")
    print(vs)
    print(f"Option B :- {format_data(account_b)}")
    guess_option = input("Who has more followers: Option A or Option B\n").lower()
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    correct_guess = check_answer(guess_option,follower_count_a,follower_count_b)

    clear()
    print(logo)

    if correct_guess:
        score += 1
        print(f"Thats Correct! your score is {score}")    
    else:
        continue_game = False
        print(f"Sorry! Thats a Wrong. your final score is {score}")
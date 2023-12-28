import os
def clear():
  os.system('clear')

import random
from art import logo

def game():
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    end_of_game = False
    difficulty = input("Choose a difficulty. Type 'easy oyr 'hard'. ").lower()
    
    if difficulty == "easy":
        lives = 10
        print(f"You have {lives} attempts to win.")
    elif difficulty == "hard":
        lives = 5
        print(f"You have {lives} attempts to win.")
    
    user_guess = input("Make a guess: ")
    int_user_guess = int(user_guess)
    
    def chosen_number():
        number = list(range(0,101))
        choice = random.choice(number)
        return choice 
    
    chosen_num = chosen_number()
    
    def compare(chosen_num, int_user_guess):
        if chosen_num < int_user_guess:
            print ("Too high")
        elif chosen_num > int_user_guess:
            print ("Too low")
    
    compare(chosen_num, int_user_guess)
    
    while not end_of_game:
        
        if int_user_guess != chosen_num:
            lives -= 1
            print (f"You have {lives} lives left.")
            user_guess = input("Guess again: ")
            int_user_guess = int(user_guess)
            compare(chosen_num, int_user_guess)
            
        if lives == 0:
            end_of_game = True
            print("You lose")
        
        elif int_user_guess == chosen_num:
            print("You win!")
            end_of_game = True

    if end_of_game == True:
        new_game = input("Do you want to play again? 'y' or 'n'")
        if new_game == "y":
            clear()
            game()
        else:
            print("Goodbye!")
            clear()

game()

import random

from click import option
from requests import options

user_score = 0
computer_score = 0

options = ['r', 'p', 's']

while True:
    user_input = input("Rock (r), paper (p), scissors (s) or quit (q)?: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Invalid input")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_input = options[random_number]
    print("Computer picked: ", computer_input + ".")

    if user_input == "rock" and computer_input == "scissors":
        print("You win!")
        user_score += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You win!")
        user_score += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("You win!")
        user_score += 1
    elif user_input == computer_input:
        print("It's a tie!")
    else:
        print("You lose!")
        computer_score += 1
print("Your score: ", user_score)
print("Computer score: ", computer_score)
print("Thanks for playing!")
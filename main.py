import random

from click import option
from requests import options

user_score = 0
computer_score = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Rock (r), paper (p), scissors (s) or quit (q)?: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Invalid input")
        continue
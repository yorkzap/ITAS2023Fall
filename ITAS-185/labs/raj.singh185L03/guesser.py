"""
Course: ITAS 185 - Introduction to Programming
Lab 3: Conditional Flow in Python
Description: This program generates a random number and takes a guess input from the user
"""

import random

guessing_number = random.randint(1, 100)

while True:
    my_guess = int(input("I am thinking of a number from 1 to 100 "))
    
    if my_guess == guessing_number:
        print(f"Congratulations! That is correct! The number I was thinking of was {guessing_number}.")
        break
    elif my_guess > guessing_number:
        print(f"{my_guess} is too high.")
    else:
        print(f"{my_guess} is too low.")
"""
Course: ITAS 185 - Introduction to Programming
Lab 3: Conditional Flow in Python
Description: This program generates a random number and takes a guess input from the user
"""

import random

guessing_number = random.randint(1, 100)

while True:
    my_guess = int(input("Take a guess from 1 - 100: "))
    if my_guess == guessing_number:
        break
    elif my_guess > guessing_number:
        print(f"Your number is too high. Try a lower number.")
    else:
        print(f"Your number is too low. Try a higher number.")
    
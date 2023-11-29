"""
    Course: ITAS 185 - Introduction to Programming
    Lab 9: Exceptions
    Description: Runs the number guessing game in a loop until the user exits with Ctrl+C. It handles user
    guesses, validates input, and responds to Ctrl+Z by preventing suspension of the program.
"""

import random

class TooBigError(Exception):
    pass

class TooLessError(Exception):
    pass

def get_integer_guess():
    """Prompt the user for a validated guess."""
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > 100:
            raise TooBigError("Your guess should not be greater than 100.")
        if guess < 1:
            raise TooLessError("Your guess should not be less than 1.")
        return guess
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def play_guessing_game():
    """Heart of the play the number guessing game."""
    while True:
        try:
            secret_number = random.randint(1, 100)
            guess = None
            while guess != secret_number:
                guess = get_integer_guess()
                if guess is None:
                    continue
                print(f'{secret_number} - Secret number for testing purposes.') # Debugging statement
                if guess < secret_number:
                    print("Number too low, try again with something higher...")
                elif guess > secret_number:
                    print("Number too high, try again with something lower...")
                else:
                    print("Yay! You guessed it. Now, let's play again!")
        except KeyboardInterrupt:
            print("\nCancelled by keyboard. Goodbye!")
            break
        except (TooBigError, TooLessError) as err:
            print(err)

if __name__ == "__main__":
    play_guessing_game()

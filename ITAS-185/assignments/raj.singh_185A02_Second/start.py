"""
Course: ITAS 185 - Introduction to Programming
Assignment 02: Wordle Game
Description:
    This WordleGame class simulates the popular word guessing game 'Wordle'. The 
    game selects a secret five-letter word which the player must guess within a 
    limited number of attempts. Each guess provides feedback to the player in the 
    form of colored letters: green for correct letters in the correct position, 
    yellow for correct letters in the wrong position, and uncolored for incorrect 
    letters. The game continues until the player either guesses the word correctly 
    or runs out of attempts, at which point the game can be restarted.

Requirements:
    This code requires the `colorama` module to be installed in the Python 
    environment. Additionally, a file named 'wordlewords.txt' must exist in the 
    same directory as this script, containing potential secret words (one per 
    line, all uppercase). Adjustments may be necessary based on your specific 
    environment or requirements.
"""

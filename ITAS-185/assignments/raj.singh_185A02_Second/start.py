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
    environment. Additionally, a file named 'wordle.txt' must exist in the 
    same directory as this script, containing potential secret words (one per 
    line, all uppercase). Adjustments may be necessary based on your specific 
    environment or requirements.
"""

import random
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

class WordleGame:
    def __init__(self):
        self.__wordList = self.read_file()
        self.__targetWord = self.select_word().upper()
        self._maxAttempts = 6
        self.__currentAttempt = 0
        self._isGameOver = False
        self._isGameWon = False
        self.__attempts = []

    def read_file(self, filename='wordle.txt'):
        with open(filename, 'r') as file:
            return [word.strip().upper() for word in file.readlines()]

    def select_word(self):
        return random.choice(self.__wordList)

    def _validateInput(self, word):
        return len(word) == 5 and word.isalpha()

    def _checkWord(self, word):
        feedback = []

        # Loop through each letter in the guessed word.
        for i, char in enumerate(word):
            # If the letter is correct and in the correct position, add green color.
            if char == self.__targetWord[i]:
                feedback.append(Fore.GREEN + char + Fore.RESET)
            # If the letter is correct but in the wrong position, add yellow color.
            elif char in self.__targetWord:
                feedback.append(Fore.YELLOW + char + Fore.RESET)
            # If the letter is not in the secret word at all, add it without color.
            else:
                feedback.append(char)

        # Combine the feedback into a single string and return it.
        return ''.join(feedback)


    def _displayBoard(self):
        for attempt in self.__attempts:
            print(self._checkWord(attempt))

    def play(self):
        print("Welcome to Wordle. Let's see if you can guess the five letter word that I have in my mind.")
        while not self._isGameOver and not self._isGameWon:
            guess = input("What is your guess: ").upper()
            if not self._validateInput(guess):
                print("Error: Input must be a 5-letter English word.")
                continue
            self.__attempts.append(guess)
            self.__currentAttempt += 1
            self._displayBoard()
            if guess == self.__targetWord:
                self._isGameWon = True
                print(f"Good job! You guessed it in {self.__currentAttempt} guesses")
            if self.__currentAttempt == self._maxAttempts:
                self._isGameOver = True
                if not self._isGameWon:
                    print(f"You lose: The correct word was {self.__targetWord}.")
            if self._isGameWon or self._isGameOver:
                if input("Would you like to play again (Y/N)? ").upper() == 'Y':
                    self.__init__()
                else:
                    break

# The game can be started with the following line:
if __name__ == "__main__":
    game = WordleGame()
    game.play()

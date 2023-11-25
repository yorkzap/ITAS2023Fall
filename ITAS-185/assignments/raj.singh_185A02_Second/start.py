"""
Course: ITAS 185 - Introduction to Programming
Assignment 02: Wordle Game

Description:
    The WordleGame class emulates 'Wordle', a word guessing game where players try to
    deduce a secret five-letter word within limited attempts. Feedback is given after
    each guess with colored indicators: green for correct placement, yellow for correct
    letters in the wrong spot, and no color for incorrect guesses. The game ends when
    the word is guessed or attempts are exhausted, with an option to restart.

Requirements:
    This code requires the `colorama` module to be installed in the Python environment. To install 
    the necessary requirements, set up a virtual environment and run the following commands:
        python -m venv venv
        source venv/bin/activate  # On Windows use 'venv\\Scripts\\activate'
        pip install -r requirements.txt

Additionally, a file named 'wordle.txt' must exist in the same directory as this script, 
containing potential secret words (one per line, all uppercase). Adjustments may be necessary 
based on your specific environment or requirements.
"""

import random
from colorama import Fore, init

# Initialize Colorama to enable terminal color formatting.
init(autoreset=True)

class WordleGame:
    """A simple terminal-based version of the Wordle game."""
    
    def __init__(self):
        """Initialize the game by resetting it."""
        self.reset_game()

    def reset_game(self):
        """Reset the game by initializing all game parameters."""
        self.__word_list = self.read_file()
        self.__target_word = self.select_word().upper()
        self.max_attempts = 6
        self.__current_attempt = 0
        self.is_game_over = False
        self.is_game_won = False
        self.__attempts = []

    def read_file(self, filename='wordle.txt'):
        """Read words from a file to add into."""
        with open(filename, 'r') as file:
            return [word.strip().upper() for word in file.readlines()]

    def select_word(self):
        """Select a random word from the word list as the secret word."""
        return random.choice(self.__word_list)

    def _validate_input(self, word):
        """Check if the user's guess is a valid 5-letter word."""
        return len(word) == 5 and word.isalpha()

    def _generate_feedback(self, word):
        """Generate feedback for the user's guess."""
        return [self._evaluate_char(i, char) for i, char in enumerate(word)]

    def _evaluate_char(self, index, char):
        """Evaluate a single character against the target word."""
        if char == self.__target_word[index]:
            return (char, 'correct')
        elif char in self.__target_word:
            return (char, 'present')
        else:
            return (char, 'absent')

    def _color_feedback(self, feedback):
        """Apply color formatting to the feedback based on character correctness."""
        colored_feedback = ''
        for char, status in feedback:
            if status == 'correct':
                colored_feedback += Fore.GREEN + char + Fore.RESET
            elif status == 'present':
                colored_feedback += Fore.YELLOW + char + Fore.RESET
            else:
                colored_feedback += char
        return colored_feedback

    def _display_board(self):
        """Display number of attempts with feedback to the user."""
        print("\n" + "-" * 40)  # Start with a horizontal line for separation.
        for attempt in self.__attempts:
            feedback = self._generate_feedback(attempt)
            print("| " + self._color_feedback(feedback))
        print("-" * 40 + "\n")  # End with a horizontal line for separation.

    def _display_summary(self):
        """Display a summary of the game after it ends."""
        if self.is_game_won:
            print(Fore.GREEN + f"Congratulations, you've won in {self.__current_attempt}/{self.max_attempts} attempts!")
            print(Fore.GREEN + "The word was: " + self.__target_word + "\n")
        else:
            print(Fore.RED + "Game over. You've used all attempts.")
            print(Fore.RED + "The correct word was: " + self.__target_word + "\n")
    
    def play(self):
        """Start the game loop, accepting user input until the game ends."""
        print("Welcome to Wordle. Guess the five-letter word.")
        while not self.is_game_over and not self.is_game_won:
            guess = input(f"Attempt {self.__current_attempt + 1}/{self.max_attempts}. Your guess: ").upper()
            if not self._validate_input(guess):
                print(Fore.RED + "Error: Input must be a 5-letter English word.\n" + Fore.RESET)
                continue
            self.__attempts.append(guess)
            self.__current_attempt += 1
            self._display_board()
            if guess == self.__target_word:
                self.is_game_won = True
            if self.__current_attempt == self.max_attempts or self.is_game_won:
                self.is_game_over = True
                self._display_summary()
            if self.is_game_over:
                play_again = input("Would you like to play again (Y/N)? ").upper()
                if play_again == 'Y':
                    self.reset_game()
                else:
                    print("Thank you for playing Wordle!")
                    break

if __name__ == "__main__":
    game = WordleGame()
    game.play()

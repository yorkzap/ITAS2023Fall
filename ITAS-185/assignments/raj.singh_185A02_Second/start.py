import random
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

class WordleGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.__word_list = self.read_file()
        self.__target_word = self.select_word().upper()
        self.max_attempts = 6
        self.__current_attempt = 0
        self.is_game_over = False
        self.is_game_won = False
        self.__attempts = []

    def read_file(self, filename='wordle.txt'):
        with open(filename, 'r') as file:
            return [word.strip().upper() for word in file.readlines()]

    def select_word(self):
        return random.choice(self.__word_list)

    def _validate_input(self, word):
        return len(word) == 5 and word.isalpha()

    def _generate_feedback(self, word):
        return [self._evaluate_char(i, char) for i, char in enumerate(word)]

    def _evaluate_char(self, index, char):
        if char == self.__target_word[index]:
            return (char, 'correct')
        elif char in self.__target_word:
            return (char, 'present')
        else:
            return (char, 'absent')

    def _color_feedback(self, feedback):
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
        print("\n" + "-" * 40)  # Horizontal line for separation
        for attempt in self.__attempts:
            feedback = self._generate_feedback(attempt)
            print("| " + self._color_feedback(feedback))
        print("-" * 40 + "\n")  # Horizontal line for separation

    def _display_summary(self):
        if self.is_game_won:
            print(Fore.GREEN + f"Congratulations, you've won in {self.__current_attempt}/{self.max_attempts} attempts!")
            print(Fore.GREEN + "The word was: " + self.__target_word + "\n")
        else:
            print(Fore.RED + "Game over. You've used all attempts.")
            print(Fore.RED + "The correct word was: " + self.__target_word + "\n")
    
    def play(self):
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

import os
from termcolor import colored

# Define custom exception classes
class NotSingleLetterError(Exception):
    pass

class NotALetterError(Exception):
    pass

class FourOFour(Exception):
    pass

def welcome_message():
    print("Welcome to the Letter Frequency Checker!")

def get_user_letter():
    not_a_letter = None
    while True:
        try:
            letter = input("Enter a letter: ").lower()
            if len(letter) > 1:
                raise NotSingleLetterError
            if not letter.isalpha():
                not_a_letter = letter
                raise NotALetterError
            break
        except NotALetterError:
            print(colored(f"Please enter a letter and not '{not_a_letter}'.", 'red'))
        except NotSingleLetterError:
            print(colored("Please enter a single letter.", 'red'))
        except Exception:
            print(colored("Make sure you enter a single alphabet letter only.", 'red'))
    return letter

def list_text_files(path):
    file_list = []
    for file in os.scandir(path):
        try:
            if file.is_file() and file.name.endswith(".txt"):
                file_list.append(file.name)
        except Exception:
            pass
    return file_list

def check_text_files(path):
    print(colored(f"Checking for all text files in {path}...", 'blue'))
    file_list = list_text_files(path)
    if not file_list:
        print(colored("No text files found.", 'yellow'))
    else:
        for file in file_list:
            print(colored(f" - {file} found", 'green'))
    return file_list

def get_user_file(file_list):
    while True:
        try:
            file = input(f"Enter the name of the file you want to check for '{letter}': ")
            if file not in file_list:
                raise FourOFour
            break
        except FourOFour:
            print(colored(f"File '{file}' not found in {files_path}. Please enter a valid file name.", 'red'))
    return file

def count_letter_frequency(letter, file_path):
    try:
        with open(file_path, "r") as file:
            letter_list = file.readlines()
        repeated_letters = len([char for line in letter_list for char in line if char.lower() == letter])
        return repeated_letters
    except Exception:
        return -1

def display_result(letter, file, frequency):
    if frequency >= 0:
        print(colored(f"The letter '{letter}' appears {frequency} times in the file '{file}'.", 'blue'))
    else:
        print(colored(f"Error reading file: {file}", 'red'))

if __name__ == "__main__":
    while True:
        welcome_message()
        letter = get_user_letter()
        files_path = "./files/part_b"
        file_list = check_text_files(files_path)
        selected_file = get_user_file(file_list)
        frequency = count_letter_frequency(letter, os.path.join(files_path, selected_file))
        display_result(letter, selected_file, frequency)

        another = input("Do you want to check another letter and file? (yes/no): ")
        if another.lower() != 'yes':
            break

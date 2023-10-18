"""
Course: ITAS 185 - Introduction to Programming
Lab05: Part B - Users Choice
Description:
    This program prompts the user for a letter and then reads the contents of count_letters.txt, 
    and finds its frequency in the file. It then prints the frequency of the letter in the file.
"""

# Prompt the user for a letter and convert it to lowercase
letter = input("Enter a letter: ").lower()

# Open, read, and close the file
file = open("count_letters.txt", "r")
file_list = file.readlines()
file.close()

# Initialize count for the letter
count_letter = 0

# Count the number of times the letter appears
repeated_letters = len([char for line in file_list for char in line if char.lower() == letter])

# Print the frequency of the letter in the file
print(f"The letter {letter} appears {repeated_letters} times in the file.")

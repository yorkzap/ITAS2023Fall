"""
Course: ITAS 185 - Introduction to Programming
Lab05: Part B - Count Letters
Description:
    This program reads a text file, counts the number of vowels and consonants in it, 
    and then prints the counts.
"""

# Open, read and close the file
file = open("count_letters.txt", "r")
file_list = file.readlines()
file.close()

# Define vowels and consonants
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# Initialize counts for vowels and consonants
count_vowels = 0
count_consonants = 0

# Count the number of vowels in the file
count_vowels = len([char for letter in range(len(file_list)) for char in file_list[letter] for vowel in vowels if char == vowel])

# Count the number of consonants in the file
count_consonants = len([char for letter in range(len(file_list)) for char in file_list[letter] for consonant in consonants if char == consonant])

# Print the counts of vowels and consonants
print(f"Total number of vowels: {count_vowels}")
print(f"Total number of consonants: {count_consonants}")


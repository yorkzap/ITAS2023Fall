"""
Course: ITAS 185 - Introduction to Programming
Lab04: A function called string_along.py
Description: The functions process a mixed list of integers and floats, returning specific results.
"""


def string_to_int(integer_string_list):
    int_list = []
    for item in integer_string_list:
        if type(item) == str:
            int_list.append(int(item.strip()))
    return int_list


def count_same(string_list):
    string_over_2_and_same = 0
    for item in string_list:
        if len(item) >= 2 and item[0] == item[-1]:
            string_over_2_and_same += 1
    return string_over_2_and_same


def count_vowels(string_with_vowels):
    return sum(1 for letter in string_with_vowels if letter in "aeiouAEIOU")


# Testing string_to_int function
integer_string_list = ['1', '2 ', '3']
expected_string_to_int = [1, 2, 3]

print(" ")
if string_to_int(integer_string_list) == expected_string_to_int:
    print("string_to_int function worked properly!")
else:
    print("string_to_int function did not work as expected.")
    print(f"Expected: {expected_string_to_int}, Got: {string_to_int(integer_string_list)}")
print(f"These are the integers taken out from the string list: {string_to_int(integer_string_list)}")
print(" - " * 50)
print(" ")

# Testing count_same function
string_list = ['121', 'abba', '45.4']
expected_count_same = 3

if count_same(string_list) == expected_count_same:
    print("count_same function worked properly!")
else:
    print("count_same function did not work as expected.")
    print(f"Expected: {expected_count_same}, Got: {count_same(string_list)}")
print(f"Number of strings over two letters with the same first and last letters: {count_same(string_list)}")
print(" - " * 50)
print(" ")

# Testing count_vowels function
string_with_vowels = "bcdfghijkiilmn"
expected_count_vowels = 3

if count_vowels(string_with_vowels) == expected_count_vowels:
    print("count_vowels function worked properly!")
else:
    print("count_vowels function did not work as expected.")
    print(f"Expected: {expected_count_vowels}, Got: {count_vowels(string_with_vowels)}")
print(f"Total number of vowels in this string would be: {count_vowels(string_with_vowels)}")
print(" - " * 50)
print(" ")

"""
Course: ITAS 185 - Introduction to Programming
Assignment: A function called string_along.py
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

string_list = ['121', 'abba', '45.4']
integer_string_list = ['1', '2 ', '3']
string_with_vowels = "bcdfghijkiilmn"

print(count_same(string_list))
print(string_to_int(integer_string_list))
print(count_vowels(string_with_vowels))
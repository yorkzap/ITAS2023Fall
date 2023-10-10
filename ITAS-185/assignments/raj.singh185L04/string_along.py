"""
Course: ITAS 185 - Introduction to Programming
Assignment 1: A function called string_along.py
Description: The functions process a mixed list of integers and floats, returning specific results.
"""

def string_to_int(integer_string_list):
    int_list = []
    for item in integer_string_list:
        if type(item) == str:
            int_list.append(int(item.strip()))
    return int_list

integer_string_list = ['1', '2 ', '3']
print(string_to_int(integer_string_list))
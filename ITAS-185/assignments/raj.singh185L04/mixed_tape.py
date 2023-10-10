"""
Course: ITAS 185 - Introduction to Programming
Assignment 1: A function called mixed_tape.py
Description: The functions process a mixed list of integers and floats, returning specific results.
"""

def only_integers(*mixed_type_list):
    return [item for item in mixed_type_list if isinstance(item, int) and item is not True]

def max_integer(mixed_type_list):
    max_num = None
    for item in mixed_type_list:
        if isinstance(item, int) and item is not True:
            if max_num is None or (isinstance(item, int) and item > max_num):
                max_num = item
    return max_num

def sum_integer(mixed_type_list):
    return sum(item for item in mixed_type_list if isinstance(item, int) and item is not True)

def product_floats(mixed_type_list):
    floats = [item for item in mixed_type_list if isinstance(item, float) and item is not True]
    if floats:
        product = 1
        for item in floats:
            product *= item
    else:
        product = 0.0
    return product

mixed_type_list = [2, 5.0, "cat", 10, 43.2, True]
 
# Print the list of integers from the mixed_type_list
print("List of Integers:", only_integers(*mixed_type_list))

# Print the maximum integer (if any) from the list
print("Maximum Integer:", max_integer(mixed_type_list))

# Print the sum of integers from the list
print("Sum of integers: ", sum_integer(mixed_type_list))

# Print the product of floats from the list
print("Product of floats: ", product_floats(mixed_type_list))
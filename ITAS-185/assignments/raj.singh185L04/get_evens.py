"""
Course: ITAS 185 - Introduction to Programming
Lab04: A function called get_even_list. 
Description: The function is passed a list of integers and returns a list of all the even numbers in the list.
"""


def get_even_list(number_list):
    return [number for number in number_list if number % 2 == 0]


def get_even_count(even_list):
    return sum(even_list)

even_list = get_even_list([4, 7, 2, 5, 21, 1024, 56])
even_count = get_even_count(even_list)

# Expected values for the given input list
expected_even_list = [4, 2, 1024, 56]
expected_even_count = sum(expected_even_list)

# Print the list of even numbers
print(f"List of Even Numbers: {even_list}")

# Print the sum of even numbers
print(f"Sum of Even Numbers: {even_count}")

# Validate the even sum
if even_count == expected_even_count:
    print("The function get_even_count worked properly!")
else:
    print("The function get_even_count did not work as expected.")


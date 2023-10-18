"""
Course: ITAS 185 - Introduction to Programming
Lab05: Part A (Program to Create Sequence Datatypes using List Comprehension)
Description:
    The program declares various sequence datatypes using list comprehension and then displays the results using print statements.
"""


# List from the elements of a range from 1200 to 2000 with steps of 130
list_a = [i for i in range(1200, 2000, 130)]
print(f"List A: {list_a}\n")

# List of the values in the list check_list = [44, 54, 64, 74, 104] with 6 added to each list item
check_list = [44, 54, 64, 74, 104]
list_b = [i + 6 for i in check_list]
print(f"List B: {list_b}\n")

# Create a list of all the numbers from 1-1000 that are evenly divisible by 7 (use modulus)
list_c = [i for i in range(1, 1001) if i % 7 == 0]
print(f"List C: {list_c}\n")

#  List from the squares of each element in list if the square is greater than 50 
my_list = [2, 4, 6, 8, 10, 12, 5, 14]
list_d = [i ** 2 for i in my_list if i ** 2 < 50]
print(f"List D: {list_d}\n")

# List of numbers from 1-300 (inclusive) containing 3.
list_e = [i for i in range(1, 301) if '3' in str(i)]
print(f"List E: {list_e}\n")

# List of tuples containing only the matching numbers in two lists
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_b = [2, 7, 1, 12]
list_f = [(a, b) for a in list_a for b in list_b if a == b]
print(f"List F: {list_f}\n")

# List of words in the string that are less than or equal to 4 letters long.
string = "This is a long string with many words even with some that are less than five letters long"
list_g = [word for word in string.split(" ") if len(word) < 5]
print(f"List G: {list_g}\n")

# Nested list comprehension to find all of the numbers from 1-100 if divisible by any single digit besides 1 (2-9).
list_h = [i for i in range(1, 101) if i > 1 and not all(i % j != 0 for j in range(2, 10))]
print(f"List H: {list_h}\n")
"""
Course: ITAS 185 - Introduction to Programming
Lab05: Part B (Program to Create Sequence Datatypes using List Comprehension)
Description:
    The program declares various sequence datatypes using list comprehension and then displays the results using print statements.
"""

# Prompt the user for a filename
filename = input("Enter a filename: ")

def sum_column(filename):
    file = open(filename, "r")
    file_list = file.readlines()
    file.close()
    # Splitting lines to columns
    list_inside_list = [line.split() for line in file_list]
    # Create a list of the sum of the columns
    sum_list = [sum([int(line[i]) for line in list_inside_list]) for i in range(len(list_inside_list[0]))]
    # Return the list of sums
    return sum_list

print(sum_column(filename))


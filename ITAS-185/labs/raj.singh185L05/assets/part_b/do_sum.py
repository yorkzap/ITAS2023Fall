"""
Course: ITAS 185 - Introduction to Programming
Lab05: Part B - Do Sum
Description:
    This program calculates the sum of columns in a text file. It prompts the user for a filename, reads the file, 
    and then calculates the sum of each column, returning a list of the sums.
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

    # Return the list of the sum of the columns
    return sum_list

print(sum_column(filename))


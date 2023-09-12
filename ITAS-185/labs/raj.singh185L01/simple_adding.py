"""
    Course: ITAS 185 - Introduction to Programming
    Lab 1: Printing to the screen
    Name: Raj Singh
    Description: This program takes three inputs and then sums them up.
"""
number_one = input("Enter the first Number ")
number_two = input("Enter the second Number ")
number_three = input("Enter the third number ")

result = int(number_one) + int(number_two) + int(number_three) #Type casting the variables for treating numbers as such
print(f"The sum of {number_one}, {number_two} and {number_three} is {result}.")

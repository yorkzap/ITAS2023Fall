"""
Course: ITAS 185 - Introduction to Programming
Lab 2: Working with numbers and modules
Description: This program calculates mileage
"""

print("This program will calculate mileage")
#Prompt to user asking for the number of kilometres driven and assign the value to a variable.
kilometer_driven = float(input("Enter the number of kilometres driven "))
number_of_litres = float(input("Enter the litres of gas used "))
ltrs_per_100_km = (number_of_litres * 100) / kilometer_driven
ltrs_per_100_km = "{:.2f}".format(ltrs_per_100_km)
print(f"If {kilometer_driven} are driven using {number_of_litres}, then the vehicle uses {ltrs_per_100_km} for every 100 kilometers")
"""
    Course: ITAS 185 - Introduction to Programming
    Lab 1: Introduction to Python
    Name: Raj Singh
    Description: This program calculates the amount to be paid
"""

wage = input("Enter the wages per hour ")
hours = input("Enter the number of hours worked ")
gross_pay = float(wage) * float(hours)
after_tax = gross_pay * 0.77 #Take away 23% taxes from the gross pay
add_bonus = after_tax * 1.13 #Add 13% bonus to after_tax
print(f"Gross pay: $ {gross_pay:.2f}")
print(f"After tax: $ {after_tax:.2f}")
print(f"Total pay: $ {add_bonus:.2f}") #Print the final amount
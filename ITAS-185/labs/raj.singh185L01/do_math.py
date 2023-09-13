"""
    Course: ITAS 185 - Introduction to Programming
    Lab 1: Introduction to Python
    Name: Raj Singh
    Description: This program contains different Math calculations.
"""
#Input in float datatype in order to take in decimals
num1 = float(input("Enter number 1 "))
num2 = float(input("Enter number 2 "))

#Do calculations
diff = num1 - num2
product = num1 * num2
quotient = num1/num2
remainder = num1%num2
int_division = num1//num2

#Show results
print(f"The difference between {num1} and {num2} is {diff}")
print(f"The product of {num1} and {num2} is {product}")
print(f"The quotient of {num1} and {num2} is {quotient}")
print(f"The remainder of {num1} and {num2} is {remainder}")
print(f"The integer division of {num1} and {num2} is {int_division}")
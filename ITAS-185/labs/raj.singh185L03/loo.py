"""
Course: ITAS 185 - Introduction to Programming
Lab 3: Conditional Flow in Python
Description: This program calculates the sum of integers up to a given positive, non-zero value using both for and while loops.
"""

# Prompt the user to enter a positive, non-zero integer value
value = int(input("Enter a positive, non-zero integer value: "))

# Using for loop
the_sum = 0

for i in range(1, value + 1):
    the_sum += i

print(f"Sum of numbers up to {value} (using a for loop): {the_sum}")

# Using while loop
the_sum = 0

while value > 0:
    the_sum += value
    value -= 1

print(f"Sum of numbers up to {value} (using a while loop): {the_sum}")

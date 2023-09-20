"""
Course: ITAS 185 - Introduction to Programming
Lab 2: Working with numbers and modules
Description: This program does various calculations with operators
"""

import math

# Initialize the total variable
total = 0

# Display the initial total
print(f"Initial total: {total}")

# Add 96 to the total
total += 96
print(f"Total after adding 96: {total}")

# Subtract 8 from the total
total -= 8
print(f"Total after subtracting 8: {total}")

# Divide the total by 3 and convert it to an integer
total /= 3
total = int(total)
print(f"Total after dividing by 3 and converting to an integer: {total}")

# Calculate the remainder when dividing by 5
total %= 5
print(f"Total after taking the remainder when dividing by 5: {total}")

# Raise the total to the power of 3
total **= 3
print(f"Total after raising to the power of 3: {total}")

# Divide the total by 8
total /= 8
print(f"Total after dividing by 8: {total}")

# Multiply the total by 7
total *= 7
print(f"Total after multiplying by 7: {total}")
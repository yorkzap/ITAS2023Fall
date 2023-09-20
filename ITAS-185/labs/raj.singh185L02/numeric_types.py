"""
Course: ITAS 185 - Introduction to Programming
Lab 2: Working with numbers and modules
Description: This program does various arithmetic tasks
"""

# Add the import statements you need here
import random
import math

# TASK A
# identifier declarations
NUMBER = 3		# number of scores
SCORE1 = 100	# first test score
SCORE2 = 97 	# second test score
SCORE3 = 90   # third test score

# Find an arithmetic average
average = (SCORE1 + SCORE2 + SCORE3) / NUMBER
output = str(SCORE1) + " and " + str(SCORE2) + " and " + str(SCORE3) + " have an average of " + str(average)
print(output)
BOILING_IN_F = 212      # boiling temperature

# Convert Fahrenheit temperatures to Celsius
f_to_c = 5/9 * (BOILING_IN_F - 32)
print(f"{BOILING_IN_F} in Fahrenheit is {f_to_c} in Celsius.", end="\n\n")

# TASK B
# Prompt the user to enter their name and read it in to a variable called first_name
first_name = input('Enter your first name: ')
# Prompt the user to enter the lowest number that their lucky number could be and call the variable low
low = int(input('Enter the lowest number your lucky number can be: '))
# Prompt the user to enter the highest number that their lucky number could be and call the variable high
high = int(input('Enter the highest number your lucky number can be: '))
# Generate a random integer between low and high and call it lucky_number using the randint function
lucky_number = random.randint(low, high)
# Print out a message to the user including their name and lucky number 
print(f"Hello {first_name}. Your lucky number is {lucky_number}")

# TASK C
# Prompt the user for a diameter of a sphere
diameter = float(input("Enter the diameter "))
# Calculate the radius
radius = diameter / 2
# Calculate the volume 
approximate_volume = (4/3) * math.pi * radius ** 3
# Print out the volume
print(f"The approximate volume of the sphere with diameter {diameter} units is {approximate_volume:.2f} cubic units")co
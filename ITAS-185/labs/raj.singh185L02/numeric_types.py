"""
ITAS Lab #2, Parts #A-C
This program demonstrates how numeric types and operators behave in Python
##### ADD THE REST OF THE DOCSTRING HERE #####
"""
# Add the import statements you need here


# TASK A- Correct these forumulae
# Find an arithmetic average
# identifier declarations
NUMBER = 3		# number of scores
SCORE1 = 100	# first test score
SCORE2 = 97 	# second test score
SCORE3 = 90   # third test score


average = (SCORE1 + SCORE2 + SCORE3) / NUMBER

output = str(SCORE1) + " and " + str(SCORE2) + " and " + str(SCORE3) + " have an average of " + str(average)
print(output)

# Convert Fahrenheit temperatures to Celsius
BOILING_IN_F = 212      # boiling temperature

f_to_c = 5/9 * BOILING_IN_F - 32

print(f"{BOILING_IN_F} in Fahrenheit is {f_to_c} in Celsius.", end="\n\n")


# ADD LINES FOR TASK B HERE
# Note you also need to import the random module where indicated above
# Next:
#    prompt the user to enter their name and read it in to a variable called first_name
#    prompt the user to enter the lowest number that their lucky number could be and call the variable low
#    prompt the user to enter the highest number that their lucky number could be and call the variable high
#    generate a random integer between low and high and call it lucky_number using the randint function
#    print out a message to the user including their name and lucky number 

# ADD LINES FOR TASK C HERE
# prompt the user for a diameter of a sphere
# read the diameter
# calculate the radius
# calculate the volume 
# print out the volume

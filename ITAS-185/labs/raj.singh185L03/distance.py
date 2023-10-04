"""
Course: ITAS 185 - Introduction to Programming
Lab 3: Conditional Flow in Python
Description: This program calculates the distance traveled using speed and time entered by the user.
"""

while True:
    speed = float(input("Enter the speed travelled: "))
    if speed > 0:
        break
    else:
        print("Invalid speed.")

while True:
    time = float(input("Enter the time travelled: "))
    if 0 < time <= 24:
        break
    else:
        print("Invalid time.")

print("------------------------")

for hour in range(0, int(time) + 1):
    distance = speed * hour
    print(f"{hour}\t{distance}")


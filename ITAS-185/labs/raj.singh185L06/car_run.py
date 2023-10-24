"""
Course: ITAS 185 - Introduction to Programming
Lab06: Importing Classes with constructors
Description:
    This program imports the Employee class, calls it's methods and display car information
"""

import Car as car

# Create a Car object
my_car = car.Car(2023, "Ford", 0)

# Accelerate the car 5 times
for i in range(5):
    my_car.accelerate()
    print(my_car)

# Brake the car 6 times and display information after each brake
for i in range(6):
    if i > 0:
        my_car.brake()
        print(my_car)
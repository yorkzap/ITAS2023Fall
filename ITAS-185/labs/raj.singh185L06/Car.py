"""
Course: ITAS 185 - Introduction to Programming
Lab06: Car Class
Description:
    The Car class defines a representation of a car with attributes for its model year, make, and speed.
    It provides methods to accelerate and brake the car, and a string representation to display its information.
"""

class Car:
    def __init__(self, model_year, make, speed):
        self.model_year = model_year
        self.make = make
        self.speed = speed

    def __str__(self):
        return f"The {self.model_year} {self.make} is going {self.speed} kph"
    
    def accelerate(self):
        self.speed += 5
    
    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

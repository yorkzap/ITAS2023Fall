"""
Course: ITAS 185 - Introduction to Programming
Test03: 01 (Whale Class)
Description:
    This is the Whale class. It is an abstract class that is inherited by the Orca and Humpback classes.
"""

from abc import ABC as a, abstractmethod as abs

class Whale(a):
    # Initialize the variable count
    count = 0

    # Initialize the attributes in the constructor
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        Whale.count += 1

    # Return a string representation of the object
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight} tons"

    # Return boolean value if the two objects are equal
    def __eq__(self, second):
        return self.name == second.name and self.age == second.age and self.weight == second.weight

    # Abstract methods Below:
    @abs
    def sing(self):
        pass

    @abs
    def eat(self, food):
        pass

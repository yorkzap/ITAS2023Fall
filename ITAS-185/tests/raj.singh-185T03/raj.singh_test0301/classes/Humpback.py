"""
Course: ITAS 185 - Introduction to Programming
Test03: 01 (Humpback Class)
Description:
    This is the Humpback class. It is a subclass of the Whale class.
"""

from .Whale import Whale as wh

class Humpback(wh):
    def __init__(self, name, age, weight, fluke_width):
        super().__init__(name, age, weight)
        self.fluke_width = fluke_width

    # Return a string representation of the object with the fluke width
    def __str__(self):
        return super().__str__() + f", Fluke Width: {self.fluke_width}"

    # Return boolean if equal (like Orca class, but with fluke width)
    def __eq__(self, other):
        return super().__eq__(other) and self.fluke_width == other.fluke_width

    def sing(self):
        return "Midtones and coos"

    def eat(self, food):
        print(f"Humpbacks eat lots and lots of {food}")

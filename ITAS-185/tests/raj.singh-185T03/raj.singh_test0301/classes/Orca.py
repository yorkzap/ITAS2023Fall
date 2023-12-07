"""
Course: ITAS 185 - Introduction to Programming
Test03: 01 (Orca Class)
Description:
    This is the Orca class. It is a subclass of the Whale class.
"""

from .Whale import Whale as wh

class Orca(wh):
    def __init__(self, name, age, weight, pod):
        super().__init__(name, age, weight)
        self.pod = pod

    def __str__(self):
        return super().__str__() + f", Pod: {self.pod}"

    def __eq__(self, second):
        return super().__eq__(second) and self.pod == second.pod

    def sing(self):
        return "High chirps and trills"

    def eat(self, food):
        print(f"Orcas eat meat like {food}")


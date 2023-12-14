"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Truck.py class
    Description: Represents a sturdy truck in a race simulation, potentially diesel-powered.
"""

from classes.Vehicle import Vehicle

class Truck(Vehicle):
    """Class representing a truck, inheriting from Vehicle."""

    def __init__(self, model: str, colour: str, is_diesel: bool):
        """
        Initialize a new Truck object with model, colour, and is_diesel.
        The is_diesel parameter is a boolean indicating if the truck runs on diesel.
        """
        super().__init__(model, colour)  # Call the superclass constructor with model and colour
        self._is_diesel = is_diesel  # Private attribute indicating if the truck is diesel-powered

    def accelerate(self):
        """
        Accelerate the truck by increasing its speed.
        Speed increase depends on whether the truck is diesel-powered.
        """
        if self._is_diesel:
            self._speed += 0.4
        else:
            self._speed += 0.5

    def get_icon(self) -> str:
        """
        Return the icon representing the truck.
        """
        return "T"
    
    def __str__(self) -> str:
        """
        Return a string representation of the truck,
        nicely formatted using the parent's __str__ method.
        """
        return super().__str__() + f", Diesel: {self._is_diesel}, Icon: {self.get_icon()}"

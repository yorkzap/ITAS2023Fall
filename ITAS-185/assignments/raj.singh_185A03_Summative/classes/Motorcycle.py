"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Motorcycle.py class
    Description: A subclass of Vehicle class, motorcycle with burst speed.
"""

from classes.Vehicle import Vehicle

class Motorcycle(Vehicle):
    """Class representing a motorcycle, inheriting from Vehicle."""

    def __init__(self, model: str, colour: str):
        """
        Initialize a new Motorcycle object with model and colour.
        Passes model and colour to the parent Vehicle class.
        """
        super().__init__(model, colour)
    
    def accelerate(self):
        """
        Accelerate the motorcycle by increasing its speed by a fixed amount.
        """
        accel = 0.6
        self._speed += accel
    
    def get_icon(self) -> str:
        """
        Return the icon representing the motorcycle.
        """
        return "M"
    
    def __str__(self) -> str:
        """
        Return a string representation of the motorcycle,
        nicely formatted using the parent's __str__ method.
        """
        return super().__str__() + ", Icon: " + self.get_icon()

"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Truck.py class
    Description: XXXXXXXXX
"""

from classes.Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, model: str, colour: str, is_diesel: bool):
        super().__init__(model, colour)
        self._is_diesel = is_diesel

    def accelerate(self):
        """Accelerate the truck based on its type."""
        accel = 0.4 if self._is_diesel else 0.5
        self._speed += accel

    def get_icon(self) -> str:
        """Return the icon representing the truck."""
        return "T"

    def __str__(self) -> str:
        """String representation of the Truck, using parent's __str__."""
        return super().__str__() + f", Diesel: {self._is_diesel}, Icon: {self.get_icon()}"

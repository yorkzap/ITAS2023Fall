"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Motorcycle.py class
    Description: XXXXXXXXX
"""

from classes.Vehicle import Vehicle

class Motorcycle(Vehicle):
    def accelerate(self):
        """Accelerate the motorcycle by increasing speed."""
        accel = 0.6
        self._speed += accel

    def get_icon(self) -> str:
        """Return the icon representing the motorcycle."""
        return "M"

    def __str__(self) -> str:
        """String representation of the Motorcycle, using parent's __str__."""
        return super().__str__() + f", Icon: {self.get_icon()}"

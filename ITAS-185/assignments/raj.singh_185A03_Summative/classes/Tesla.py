"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Tesla.py class
    Description: XXXXXXXXX
"""

from classes.Vehicle import Vehicle

class Tesla(Vehicle):
    def __init__(self, model: str, colour: str, is_two_motor: bool):
        super().__init__(model, colour)
        self._is_two_motor = is_two_motor

    def accelerate(self):
        """Accelerate the Tesla based on its motor configuration."""
        accel = 0.7 if self._is_two_motor else 0.6
        self._speed += accel

    def get_icon(self) -> str:
        """Return the icon representing the Tesla."""
        return "E"

    def __str__(self) -> str:
        """String representation of the Tesla, using parent's __str__."""
        return super().__str__() + f", Two Motor: {self._is_two_motor}, Icon: {self.get_icon()}"

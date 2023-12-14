"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Tesla.py class
    Description: Represents a Tesla car with potential for two motors in a race simulation.
"""

from classes.Vehicle import Vehicle

class Tesla(Vehicle):
    """Class representing a Tesla car, inheriting from Vehicle."""

    def __init__(self, model: str, colour: str, is_two_motor: bool):
        """
        Initialize a new Tesla object with model, colour, and is_two_motor.
        The is_two_motor parameter indicates if the Tesla has two motors.
        """
        super().__init__(model, colour)  # Call the superclass constructor with model and colour
        self._is_two_motor = is_two_motor  # Private attribute indicating if the Tesla has two motors

    def accelerate(self):
        """
        Accelerate the Tesla by increasing its speed.
        Speed increase depends on whether the Tesla has two motors.
        """
        if self._is_two_motor:
            self._speed += 0.7
        else:
            self._speed += 0.6

    def get_icon(self) -> str:
        """
        Return the icon representing the Tesla.
        """
        return "E"
    
    def __str__(self) -> str:
        """
        Return a string representation of the Tesla,
        nicely formatted using the parent's __str__ method.
        """
        return super().__str__() + f", Two Motor: {self._is_two_motor}, Icon: {self.get_icon()}"

"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Vehicle.py class
    Description:
    This is an abstract base class for a vehicle. It class has various methods.
    It cannot be instantiated directly, but must be subclassed first.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for a vehicle."""

    def __init__(self, model: str, colour: str):
        """
        Initialize a new Vehicle object with model and colour. 
        Speed and position are set to zero by default.
        """
        self._model = model
        self._colour = colour
        self._speed = 0.0  # Initial speed is zero
        self._position = 0.0  # Initial position is at the start line

    def get_model(self) -> str:
        """Return the model of the vehicle."""
        return self._model

    def get_colour(self) -> str:
        """Return the colour of the vehicle."""
        return self._colour

    def get_speed(self) -> float:
        """Return the current speed of the vehicle."""
        return self._speed

    def get_position(self) -> float:
        """Return the current position of the vehicle."""
        return self._position

    def set_speed(self, value: float):
        """
        Set the speed of the vehicle.
        :param value: A float representing the new speed of the vehicle.
        """
        self._speed = value

    def set_position(self, value: float):
        """
        Set the position of the vehicle.
        :param value: A float representing the new position of the vehicle.
        """
        self._position = value

    def move(self):
        """Update the vehicle's position by adding the current speed."""
        self._position += self._speed

    @abstractmethod
    def accelerate(self):
        """Abstract method to accelerate the vehicle."""
        pass

    @abstractmethod
    def get_icon(self) -> str:
        """Abstract method to get the icon representing the vehicle."""
        pass

    def get_position_int(self) -> int:
        """Return the vehicle's position as an integer."""
        return int(self._position)

    def __repr__(self) -> str:
        """Return a string representation of the vehicle for debugging."""
        return (f"Vehicle(Model: {self._model}, Colour: {self._colour}, "
                f"Speed: {self._speed}, Position: {self._position})")

    def __str__(self) -> str:
        """Return a human-readable string representation of the vehicle."""
        return (f"Model: {self._model}, Colour: {self._colour}, "
                f"Speed: {self._speed}, Position: {self._position}")

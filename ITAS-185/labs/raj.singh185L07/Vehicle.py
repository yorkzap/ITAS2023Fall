"""
Course: ITAS 185 - Introduction to Programming
Lab06: Vehicle Class
Description:
    This module defines a hierarchy of classes that model different types of vehicles.
    It includes a base Vehicle class along with derived classes Car, Transport,
    Pickup, and SportsCar, each with specific attributes and methods.
"""

class Vehicle:
    """
    A class representing a generic vehicle.
    """

    def __init__(self, color, manufacturer, speed, top_speed, year):
        self.color = color
        self.manufacturer = manufacturer
        self.speed = 0.0  # Speed is initialized to 0.0
        self.top_speed = float(top_speed)
        self.year = int(year)
        
    def accelerate(self, amount=3):
        """
        Increase the vehicle's speed by a specified amount, up to the top_speed.
        """
        self.speed += amount
        if self.speed > self.top_speed:
            self.speed = self.top_speed
    
    def brake(self, amount=2):
        """
        Decrease the vehicle's speed by a specified amount, not going below 0.
        """
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        
    def __str__(self):
        return f"{self.year} {self.color} {self.manufacturer} is travelling at {self.speed} kph with a top speed of {self.top_speed} kph."
    
    def __eq__(self, other):
        return self.top_speed == other.top_speed
    
class Car(Vehicle):
    """
    A class representing a car, which is a type of vehicle.
    """

    def __init__(self, color, manufacturer, speed, top_speed, year, number_of_doors, is_electric):
        super().__init__(color, manufacturer, speed, top_speed, year)
        self.number_of_doors = int(number_of_doors)
        self.is_electric = bool(is_electric)
        
    def accelerate(self, amount=2):
        """
        Accelerate the car by a fixed amount of 2.
        """
        super().accelerate(amount)
        
    def __str__(self):
        electric_status = 'is electric' if self.is_electric else 'is not electric'
        return f"{super().__str__()}, It has {self.number_of_doors} doors and {electric_status}."
        
class Transport(Vehicle):
    """
    A class representing a transport vehicle, capable of carrying a payload.
    """

    def __init__(self, color, manufacturer, speed, top_speed, year, payload):
        super().__init__(color, manufacturer, speed, top_speed, year)
        self.payload = float(payload)
        
    def accelerate(self):
        """
        Accelerate the transport by a fixed amount of 1.
        """
        super().accelerate(1)
        
    def __str__(self):
        return f"{super().__str__()}, It can carry a payload of {self.payload} tons."
    
class Pickup(Car):
    """
    A class representing a pickup truck, which is a specialized type of car.
    """

    def __init__(self, color, manufacturer, speed, top_speed, year, number_of_doors, is_electric):
        super().__init__(color, manufacturer, speed, top_speed, year, number_of_doors, is_electric)
        
    def accelerate(self):
        """
        Accelerate the pickup by a fixed amount of 1.5.
        """
        super().accelerate(1.5)

class SportsCar(Car):
    """
    A class representing a sports car, which is a specialized type of car.
    """

    def __init__(self, color, manufacturer, speed, top_speed, year, number_of_doors, is_electric):
        super().__init__(color, manufacturer, speed, top_speed, year, number_of_doors, is_electric)
        
    def accelerate(self):
        """
        Accelerate the sports car by a fixed amount of 4.
        """
        super().accelerate(4)

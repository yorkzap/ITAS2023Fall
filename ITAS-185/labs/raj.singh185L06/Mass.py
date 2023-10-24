"""
Course: ITAS 185 - Introduction to Programming
Lab06: Mass Class
Description:
    The Mass class provides functionalities to represent and manipulate 
    objects with different mass units. It allows conversion of these units 
    into kilograms (kg) and supports representation in a string and formal format. 
    The class utilizes a predefined dictionary for conversion rates relative to the kilogram.
"""

class Mass:
    # Dictionary of conversion rates relative to the kilogram
    _conversion = {
        'mg': 0.000001,
        'g': 0.001,
        'kg': 1,
        'lb': 0.453592,
        'oz': 0.02835,
        'stone': 6.35029
        }
    
    def __init__(self, value, unit = 'kg'):
        self.value = value
        self.unit = unit

    def convert_to_kg(self):
        return self.value * self._conversion[self.unit]
    
    def __str__(self):
        return f"{self.convert_to_kg():.2f} kg"
    
    def __repr__(self):
        return f"Mass({self.value:.2f}, '{self.unit}')"

    

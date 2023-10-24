"""
Course: ITAS 185 - Introduction to Programming
Lab06: Mass class test
Description:
    This program imports class and runs it's methods
"""

import Mass as mass

# Create a Mass object for conversion in kg
mass_kg = mass.Mass(2400, 'g')

# Create a mass object for conversion in stone
mass_stone = mass.Mass(14.30, 'stone')
 
# Test the convert_to_kg method
print(mass_kg.convert_to_kg())
print(mass_kg.__str__())
print(mass_stone.__repr__())
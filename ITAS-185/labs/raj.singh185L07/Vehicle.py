"""
Course: ITAS 185 - Introduction to Programming
Lab06: Vehicle Class
Description:
    EDITTHIS_EDITTHIS_EDITTHIS_EDITTHIS_EDITTHIS_EDITTHIS_
"""

class Vehicle:
    def __init__(self, color, manufacturer, speed, top_speed, year):
        self.color = color
        self.manufacturer = manufacturer
        self.speed = float(0.0)
        self.top_speed = float(top_speed)
        self.year = int(year)
        
    def accelerate(self, amount=3):
         """
         Increases the speed by the amount passed default 3
         """
         self.speed = self.speed + amount
         self.speed = self.top_speed if self.speed > self.top_speed else self.speed
    
    def brake(self, amount=2):
        """
        Decreases the speed by the amount passed or default 2
        """
        self.speed = self.speed - amount
        self.speed = 0 if self.speed < 0 else self.speed
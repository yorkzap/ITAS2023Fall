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
        
    def __str__(self):
        return f"{self.year} {self.color} {self.manufacturer} is travelling {self.speed} kph with a maximum speed of {self.top_speed} kph"
    
    def __eq__(self, other):
        return True if self.top_speed == other.top_speed else False
    
class Car(Vehicle):
    def __init__(self, color, manufacturer, speed, top_speed, year, number_of_doors, is_electric):
        super().__init__(color, manufacturer, speed, top_speed, year) # Referring to the constructor of the Vehicle class
        self.number_of_doors = int(number_of_doors)
        self.is_electric = bool(is_electric)
        
    def accelerate(self):
        super().accelerate(2)
        
    def __str__(self):
        initial_string = super().__str__()
        if self.is_electric:
            return f"{initial_string}, It has {self.number_of_doors} doors and is electric"
        else:
            return f"{initial_string}, It has {self.number_of_doors} doors and is not electric"
        
"""
9.	Create a class called Transport which extends Vehicle. It has the extra attribute of: 
payload: float
Method	Purpose
Constructor	A constructor that accepts all attributes and set the values accordingly by first calling the super method and then assigning the extra attribute
accelerate	Has NO parameters. Overrides the accelerate method of the Vehicle class and calls the Vehicle class accelerate method with the value 1
toString()	Calls the super method to get the initial string and adds: 
It can carry a payload of payload tons to end of the string. For example,
1999 brown Mac is travelling 100 kph with a maximum speed of 160 kph. It can carry a payload of 300 tons.
"""

class Transport(Vehicle):
    def __init__(self, color, manufacturer, speed, top_speed, year, payload):
        super().__init__(color, manufacturer, speed, top_speed, year)
        self.payload = float(payload)
        
    def accelerate(self):
        super().accelerate(1)
        
    def __str__(self):
        initial_string = super().__str__()
        return f"{initial_string}. It can carry a payload of {self.payload} tons"
    
"""10.	Create a class called Pickup which extends Car. 
Method	Purpose
Constructors	One constructor that accepts all attributes and set the values accordingly by calling the super method.
accelerate	Has no parameters and calls the accelerate method of the Car class with the value 1.5
"""

class Pickup(Car):
    def __init__(self, color, manufacturer, speed, top_speed, year, number_of_doors, is_electric):
        super().__init__(color, manufacturer, speed, top_speed, year, number_of_doors, is_electric)
        
    def accelerate(self):
        super().accelerate(1.5)

"""11.	Create a class called SportsCar which extends Car.
Method	Purpose
Constructor	One constructor that accepts all attributes and set the values accordingly by calling the super method.
accelerate	Has no parameters and calls the accelerate method of the Car class with the value 4
"""

class SportsCar(Car):
    def __init__(self, color, manufacturer, speed, top_speed, year, number_of_doors, is_electric):
        super().__init__(color, manufacturer, speed, top_speed, year, number_of_doors, is_electric)
        
    def accelerate(self):
        super().accelerate(4)

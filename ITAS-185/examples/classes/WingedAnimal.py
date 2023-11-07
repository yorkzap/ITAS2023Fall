class WingedAnimal:
    def __init__(self, wing_colour):
        self.wing_colour = wing_colour

    def fly(self):
        print("I can fly!")

    def __str__(self):
        return f"{self.__class__.__name__} with {self.wing_colour} wings"
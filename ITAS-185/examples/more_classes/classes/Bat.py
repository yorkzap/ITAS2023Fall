import classes.Animal as a
import classes.WingedAnimal as wa

class Bat(a.Animal, wa.WingedAnimal):
    def __init__(self, name="", yob=0, is_vegetarian=False, wing_colour='black', eyesight='poor'):
        a.Animal__init__(self, name, yob, is_vegetarian)
        wa.WingedAnimal__init__(self, wing_colour, eyesigh)
        self.eysight = eyesight


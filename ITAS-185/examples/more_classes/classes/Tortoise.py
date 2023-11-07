import classes.Animal as a

class Tortoise(a.Animal):
    def __init__(self, name="", yob=0, is_vegetarian=False, shell_thickness = 0):
        super().__init__(name, yob, is_vegetarian)
        self.__shell_thickness = shell_thickness
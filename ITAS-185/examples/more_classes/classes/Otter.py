import classes.Animal as a

class Otter(a.Animal):
    def __init__(self, name="", yob=0, is_vegetarian=False, whisker_length = 0):
        super().__init__(name, yob, is_vegetarian)
        self.__is_playful = False
        
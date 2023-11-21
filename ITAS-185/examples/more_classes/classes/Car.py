import classes.Vehicle as v

class Car(v.Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    
    def start_engine(self):
        print('Starting engine of {self.make} {self.model} car')
        
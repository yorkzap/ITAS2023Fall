class MyClass:
    def __init__(self) -> None:
        self.public_var = 10
        self._protected_var = 20
        self.__private_var = 30
        
    def public_method(self):
        print("Public Method")
        
    def _protect_method(self):
        print("Protected Method")
        
    def __private_method(self):
        print("Private Method")
    
'''
    TODO: Single Inheritance in Python | Python Tutorial - Day #78 
'''


class Animal:
    def __init__(self, *args) -> None:
        self.name, self.species = args
        pass

    def make_sound(self):
        print("sound made by animal")
    pass


class Dog(Animal):
    def __init__(self, *args) -> None:
        super().__init__( args[0], "Dog")
        self.breed = args[1]

    def make_sound(self):
        print("Bark!")
    pass


obj = Dog("131", "sdfa")
print(obj.__dict__)

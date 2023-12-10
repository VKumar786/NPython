'''
    TODO: Multiple Inheritance in Python | Python Tutorial - Day #79 
    ? mro will tell order of method that would be find inside a class
'''


class Person:
    def __init__(self, name) -> None:
        self.name = name
        pass

    def show(self):
        print(f"Name is {self.name}")


class Sport:
    def __init__(self, sport_name) -> None:
        self.sport_name = sport_name
        pass

    def show(self):
        print(f"Name is {self.dance}")


class SuperHuman(Person, Sport):
    def __init__(self, name, sport_name) -> None:
        self.name = name
        self.sport_name = sport_name


obj = SuperHuman("Vishal", "Badminton")

obj.show()  # first class in MultiInheritance will get first change

print(SuperHuman.mro())

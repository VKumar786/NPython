'''
    TODO: Inheritance in Python | Python Tutorial - Day #61 
    ? Types of inheritance:
        * Single inheritance
        * Multiple inheritance
        * Multilevel inheritance
        * Hierarchical Inheritance
        * Hybrid Inheritance
'''


class Employee:
    def __init__(self, *args) -> None:
        self.name = args[0]
        self.id = args[1]
        pass

    def showDetails(self):
        print(f"{self.id}. {self.name}")
        pass


obj = Employee("Vishal", 45)
obj.showDetails()


class Programmer(Employee):
    def showLang(self):
        print("Python")


obj1 = Programmer("viky", 52)
obj1.showLang()

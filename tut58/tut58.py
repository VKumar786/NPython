'''
    TODO: Access Modifiers in Python | Python Tutorial - Day #62 
    ? there is no such access modifier in python
    ? Types of access specifiers
        * Public access modifier
        * Private access modifier - it is accessed only within class
        * Protected access modifier - it is accessed only within class & subclass

    ? protected -> _var -> it just a naming convention
'''


class Business:
    def __init__(self, *args):
        self.name = args[0]  # public
        self.age = args[1]
        self.__net_worth = args[2]  # private
        self._occupation = args[3]  # protected
        pass

    def _printName(self):
        print("My name is khan")
    pass


class Franchise(Business):
    pass


obj = Business("Vishal", 21, 2100, "Frontend Developer")
print(obj.name)

try:
    print(obj.__net_worth)  # cannot access directly
except Exception as e:
    print(e)
    pass

print(obj._Business__net_worth)  # can be access indirectly | Name mangling
print(obj.__dir__())  # all method which are available
print(dir(obj))

obj1 = Franchise("Viky", 21, 500, "SDE")

print(obj._occupation)
obj._printName()

print(obj1._occupation)
obj1._printName()

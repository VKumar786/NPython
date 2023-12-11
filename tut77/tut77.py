'''
    TODO: Hybrid and Hierarchical Inheritance in Python | Python Tutorial - Day #81 
'''

# Hybrid Inheritance


class BaseClass:
    pass


class Derived1(BaseClass):
    pass


class Derived2(BaseClass):
    pass


class Derived3(Derived1, Derived2):
    pass

# Hierarchical Inheritance


class BaseClass:
    pass


class Derived1(BaseClass):
    pass


class Derived2(BaseClass):
    pass


class Derived3(Derived1):
    pass

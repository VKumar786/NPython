'''
    TODO: Operator Overloading in Python | Python Tutorial - Day #77 
'''


class Vector:
    def __init__(self, *args) -> None:
        self.i, self.j, self.k = args
        pass

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, obj):
        # return f"{self.i + obj.i}i + {self.j + obj.j}j + {self.k + obj.k}k"
        return Vector(self.i + obj.i, self.j + obj.j, self.k + obj.k)
    pass


obj = Vector(1, 2, 3)
print(obj)

obj1 = Vector(2, 4, 2)
print(obj1)

print(obj + obj1)
print(type(obj + obj1))

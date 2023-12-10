'''
    TODO: Method Overriding in Python | Python Tutorial - Day #74 
'''


class Square:
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]

    def area(self):
        return self.x * self.y


class Circle(Square):
    def __init__(self, *args):
        self.radius = args[0]
        super().__init__(args[0], args[0])

    def area(self):
        return 31.4 * super().area()


obj = Circle(5)
print(obj.area())
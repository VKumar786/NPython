class MyClass:
    NumberOfEmployee = 0  # class variable

    def __init__(self, *args):
        MyClass.NumberOfEmployee += 1
        pass

    def print_class_var(self):
        print(MyClass.NumberOfEmployee)

    pass


obj1 = MyClass()
obj1.print_class_var()
obj2 = MyClass()

obj1.print_class_var()
obj2.print_class_var()

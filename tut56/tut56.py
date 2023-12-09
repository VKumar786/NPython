'''
    TODO: Getters and Setters in Python | Python Tutorial - Day #60 
    ? by using @property we can use function name as variable
'''


class MyClass:
    def __init__(self, value):
        self._value = value

    def value1(self):
        return self._value

    # Getter
    @property
    def value(self):
        return self._value

    @property
    def Ten_value(self):
        return self._value*10

    # Setter
    @value.setter
    def value(self, *args):
        self._value = args[0]

    @Ten_value.setter
    def Ten_value(self, *args):
        self._value = args[0]//10


obj = MyClass(786)
print(obj.value)
print(obj.Ten_value)
print(obj.value1)

obj.value = 100
print(obj.value)

obj.Ten_value = 450
print(obj.Ten_value)

'''
    TODO: Instance variables vs Class variables in Python | Python Tutorial - Day #66 
    ? Employee.showDetails(obj)
'''


class Employee:
    def __init__(self, *args):
        self.name = args[0]
        pass

    def showDetails(self):
        print(f"Name is {self.name}")


obj = Employee("vishal")

obj.showDetails()
Employee.showDetails(obj)

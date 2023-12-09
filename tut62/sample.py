class Employee:
    # Class Variable | variable which i want to put as global for each instance
    Company_Name = "Tax Refund"

    def __init__(self, *args):
        self.name = args[0]
        self.Raise_Amount = 0.2  # Instance Variable
        pass

    def showDetails(self):
        print(
            f"Name is {self.name}, raise {self.Raise_Amount}, company {self.Company_Name}")


obj = Employee("vishal")

obj.Raise_Amount = 0.8

obj1 = Employee("vivek")

obj1.Company_Name = "Tax Refund India"

obj.showDetails()
obj1.showDetails()

Employee.Company_Name = "Tax Refund India"

obj.showDetails()
obj1.showDetails()

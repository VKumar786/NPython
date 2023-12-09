'''
    TODO: Class Methods in Python | Python Tutorial - Day #69 
    ? unless we use @staticmethod, function will take first args as self
    ? @classmethod, function will take first args as Class
'''


class Employee:
    Company = "Tax Refund"

    def show(self):
        print(f"Company Name is {self.Company}")

    def changeCompanyName(cls, newCompanyName): # cls is acting as self, first args is treated as self
        cls.Company = newCompanyName

    @staticmethod
    def changeCompanyName1(cls, newCompanyName):
        cls.Company = newCompanyName
        
    @classmethod
    def changeCompanyName2(cls, newCompanyName):
        cls.Company = newCompanyName
        
    pass

obj = Employee()

obj.changeCompanyName( "Tax Refund India")

obj.show()

print(Employee.Company)

Employee.changeCompanyName1(Employee, "Tax Refund India")

print(Employee.Company)

Employee.changeCompanyName2("Tax Refund")

print(Employee.Company)
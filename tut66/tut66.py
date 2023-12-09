'''
    TODO: Class Methods as Alternative Constructors in Python | Python Tutorial - Day #70 
'''


class Business:
    def __init__(self, name, location, industry, revenue):
        self.name = name
        self.location = location
        self.industry = industry
        self.revenue = revenue
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees

    def show(self):
        print(f"Business Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Industry: {self.industry}")
        print("Employees:")
        for employee in self.employees:
            print(f"- {employee}")

    @classmethod
    def fromStr(cls, data):
        data = list(map(lambda x: int(x) if x.isnumeric()
                    else x, data.split("-")))
        obj = cls(*data)
        return obj


my_business = Business("Tax Refund", "India", "Technology", 0)

data = "Tax Refund India-India-Technology-100"

my_business = Business.fromStr(data)

my_business.show()

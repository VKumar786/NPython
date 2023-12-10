'''
    TODO: dir, __dict__ and help method in Python | Python Tutorial - Day #71 
    ? __dict__ - return all variable inside a class
    ? dir - return all builtin method inside it & dander methods [__x__] also
    ? help - give a brief context
'''

arr = [1, 2, 3, 4]
tup = (1, 2, 3, 4)

print(dir(arr))
print(dir(tup))


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

print(my_business.__dict__)

help(str)
help(Business)

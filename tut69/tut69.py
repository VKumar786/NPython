'''
    TODO: Magic/Dunder Methods in Python | Python Tutorial - Day #73 
    ? __repr__ -> how can i recreate this, work as fallback if __str__ method was not found | repr(E)
    ? __str__ -> print what inside class | str(E) | print(E)
    ? __call__ -> my_business()
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

    def __str__(self):
        return f'''Business Name: {self.name}
Location: {self.location}
Industry: {self.industry}'''

    def __repr__(self):
        return f'''Business("{self.name}", "{self.location}", "{self.industry}", {self.revenue})'''

    def __len__(self):
        return len(self.employees)

    def __call__(self, *args, **kwds) -> None:
        print("My name is khan")
        pass


my_business = Business("Tax Refund", "India", "Technology", 0)
my_business.add_employee("Vishal")

print(len(my_business))
print(my_business)

print(str(my_business))
print(repr(my_business))

my_business()

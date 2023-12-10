'''
    TODO: super keyword in Python | Python Tutorial - Day #72 
    ! DRY - Don't Repeat YourSelf
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
    pass


class SubsidiaryBusiness(Business):
    def __init__(self, name, location, industry, revenue, parent_company):
        super().__init__(name, location, industry, revenue)
        self.parent_company = parent_company
        
    def show(self):
        super().show()
        print(f"Parent Company : {self.parent_company}")
    pass


# my_business = Business("Tax Refund", "India", "Technology", 0)
my_business = SubsidiaryBusiness("ITR", "India", "Technology", 0, "Tax Refund")

my_business.show()

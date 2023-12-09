'''
    TODO: Constructors in Python | Python Tutorial - Day #58 
    ? Default Constructor
        * When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
'''


class Person:
    name, occupation, net_worth = "", "", 0

    def __init__(self, *args):
        self.name, self.occupation, self.net_worth = args
        pass

    def info(self):
        print(
            f"I'm {self.name}, an {self.occupation} professional with a net worth of {self.net_worth}.")

        pass


Vishal = Person("Vishal", "Developer", -10)

Vishal.info()

Preeti = Person("Preeti Anand", "HR",  10)

Preeti.info()

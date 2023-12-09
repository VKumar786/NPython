'''
    TODO: Classes and Objects in Python | Python Tutorial - Day #57 
    ? self - jis obj ke liya ye call kiya ja rha ha
'''


class Person:
    name, occupation, net_worth = "", "", 0

    def __init__(self, *args):
        self.name, self.occupation, self.net_worth = args
        pass

    def info(self):
        print(
            f"My name is {self.name}, occupation is {self.occupation}, net worth is {self.net_worth}")

        pass


Vishal = Person("Vishal", "FrontEnd Developer", 0)

Vishal.info()

Vishal.name = "Viky"

Vishal.info()

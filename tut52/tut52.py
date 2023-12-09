'''
    TODO: Introduction to OOPs in Python | Python Tutorial - Day #56 
    ? Polymorphism - ek chiz but multiple form
'''


class Business:  # BluePrint
    sale, profit, ad = 0, 0, 0

    def __init__(self, *args):
        self.sale = args[0]
        self.profit = args[1]
        self.ad = args[2]
        pass


Vikram = Business(6000, 2000, 1000)  # Object
Vishal = Business(300000, 100000, 200000)  # Entity

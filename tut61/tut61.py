'''
    TODO: Static Methods in Python | Python Tutorial - Day #65 
'''


class Business:
    def __init__(self) -> None:
        pass

    @staticmethod
    def Add(a, b) -> None:
        print(f"sum is {a+b}")


Business.Add(52, 1)

vishal = Business()
vishal.Add(2, 1)

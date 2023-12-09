'''
    TODO: Raising custom errors in Python | Python Tutorial - Day #38 
    ? https://docs.python.org/3/library/exceptions.html
'''

age = int(input("Enter you age"))

if (age < 0):
    raise ValueError("Age can't be negative")

# Custom class exception


class CustomErr(Exception):
    pass


try:
    name = input("Enter your name : ")
    if(name == "king"):
        raise CustomErr("I want something just like this")
    pass
except CustomErr as e:
    print(e)
    pass

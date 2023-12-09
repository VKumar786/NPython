'''
    TODO: Decorators in Python | Python Tutorial - Day #59 
    ? decorators is used to modify function
    ? *args -> arguments as list
    ? **kwargs -> arguments as dictionary
'''


def Greet(fx):
    def mfx():  # modified function
        print("Good Morning")  # before actual function implementation
        fx()
        print("Have a good one")  # after actual function implementation
    return mfx


@Greet
def work():
    print("I am working")


def gym():
    print("I am in GYM")


work()

Greet(gym)()

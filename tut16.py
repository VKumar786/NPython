'''
    TODO: Functions in Python | Python Tutorial - Day #20 
'''


def gmean(a, b):
    return (a*b)/(a+b)


def greater(a, b):
    if (a == b):
        return "Both are equal"
    elif (a < b):
        return "Second is greater"
    else:
        return "First is greater"


def lesser(a, b):
    pass


print(gmean(4, 2))
print(gmean(4, 20))

print(greater(21, 12))

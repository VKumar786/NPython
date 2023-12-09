'''
    TODO: Function Arguments in Python | Python Tutorial - Day #21 
'''


def avgV1(a=0, b=0):
    print("a :", a, ", b :", b)
    print("Avg is ::", (a+b)/2)


avgV1(21, 232)
avgV1(21)
avgV1(b=58)
avgV1(b=5112, a=21312)


def avgV2(*arr):
    print(type(arr), arr)  # tuple
    el = 0
    for i in arr:
        el += i
    print(el/len(arr))


avgV2(234, 452)


def Intro(**arr):
    print(type(arr), arr)  # dict
    print(f'My name is {arr["name"]}, age is {arr["age"]}')


Intro(
    name="vishal",
    age=21,
)


def avgV3(*arr):
    return sum(arr)/len(arr)


print(avgV2(234, 452)) # return type is None
print(avgV3(12, 123, 123, 12, 123, 4, 45, 32, 63))

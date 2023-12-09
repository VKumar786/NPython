'''
    TODO: Map, Filter and Reduce in Python | Python Tutorial - Day #53 
    ? from functools import reduce
'''

from functools import reduce
# MAP


def fun(x):
    return x + 5


arr = [2, 5, 1, 6, 7, 4]

print([x * x for x in arr])

arr = list(map(lambda x: x*x*x, arr))

print(arr)

arr = list(map(fun, arr))

print(arr)

# FILTER

arr = [2, 5, 1, 6, 7, 4]

arr = list(filter(lambda x: x % 2 == 0, arr))
print(arr)

# Reduce
arr = [2, 5, 1, 6, 7, 4]

val = reduce(lambda x, y: x+y, arr)
print(val)

'''
    TODO: Function Caching in Python | Python Tutorial - Day #92 
    ? memorization
'''

# import functools
from functools import lru_cache
import time


# @functools.lru_cache(maxsize=None)
@lru_cache(maxsize=None)
def fun(i):
    time.sleep(2)
    return i


print(fun(100))
print(fun(101))
print(fun(102))
print(fun(103))
print(fun(100))
print(fun(100))
print(fun(100))
print(fun(100))

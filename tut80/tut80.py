'''
    TODO: Time Module in Python | Python Tutorial - Day #84 
    ? For loop === while loop both are equal
'''

import time


def usingWhile():
    i = 0
    while i < 50000:
        i += 2
    pass


def usingFor():
    for i in range(50000, 2):
        pass


start = time.time()
usingWhile()
print(time.time() - start)

start = time.time()
usingFor()
print(time.time() - start)

'''
    TODO: 'is' vs '==' in Python | Python Tutorial - Day #54 
'''

a = [2, 4, 1]
b = [2, 4, 1]

print(a == b)  # value
print(a is b)  # exact location of object in memory

a = 55
b = "55"

print(a == b)  # value
print(a is b)  # exact location of object in memory

a = 55
b = 55

print(a == b)  # value
print(a is b)  # exact location of object in memory

a = "55"
b = "55"

print(a == b)  # value
print(a is b)  # exact location of object in memory

a = (2, 4)
b = (2, 4)

print(a == b)  # value
print(a is b)  # exact location of object in memory

a = None
b = None

print(a == b)  # value
print(a is b)  # exact location of object in memory

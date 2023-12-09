'''
    TODO: Tuples in Python | Python Tutorial - Day #24 
    ? tuple are unchangeable
'''

tup = (12, 32, 34, 23, 4324)
print(tup, type(tup))

tup = (1)
print(tup, type(tup))
# Single element tuple
tup = (1,)
print(tup, type(tup))

# tup[0] = 2121 Err

tup = (1, "vishal", "vivek", True)
print(tup)

print(tup[-1])
print(tup[len(tup)-1])

if ("vivek" in tup):
    print("vivek found in tuple")
else:
    print("vivek not found in tuple")

print(tup[::2])
print(tup[0:len(tup):2])
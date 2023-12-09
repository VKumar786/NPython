'''
    TODO: Operations on Tuples in Python | Python Tutorial - Day #25 
    ? tuple are immutable
    ? if we want to manipulate tuple
        * tuple -> list -> tuple
    ? we can directly concatenate two tuples without converting them to list
'''

tup = (12, 23, 421, 2364, 34, 756, 2346)

tup1 = list(tup)
tup1.append(-1)
tup1[0] = 1e9 + 7

tup = tuple(tup1)

print(tup)


t1 = (213, 123122, 13)
t2 = (35, 3, 1)

tup = t1 + t2
print(tup)


print(tup.count(1))
print(tup.index(3, 0, len(tup)))

'''
    TODO: List Methods in Python | Python Tutorial - Day #23 
'''

l1 = [3, 6, 9, 12, 15, 1, 2, 1]
l2 = ["Alice", "Bob", "Claire", "David", "Emma"]

l1.append(2)
print(l1)

l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

l2.reverse()
print(l2)

print("Index :", l2.index("Emma"))

print(l1.count(1))

l2_1 = l2.copy()
l2_1[0] = "vishal"

print(l2, l2_1)

l1.insert(1, 1000)
print(l1)

arr = [2, 232, 3232, 332323]
print(l1)
l1.extend(arr)
print(l1)

l1 = l1 + arr
print(l1)

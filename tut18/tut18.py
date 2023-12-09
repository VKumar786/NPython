'''
    TODO: Introduction to Lists in Python | Python Tutorial - Day #22 
    ? order is maintain inside list
    ? list comprehension
'''

arr = [1, 2, 3, 4, 5, "vishal", "vivek"]

print(arr)

for i in range(len(arr)):
    print(arr[i], end=", ")

if 3 in arr:
    print("found 3")
else:
    print("not found 3")

if "vivek" in arr:
    print("vivek is in list")
else:
    print("vivek not found")

el = "vishal kumar, vivek kumar"

if ("hal kum" in el):
    print("find string")

# Jump Index concept used
print(el[2:20:3])

el = [i*i for i in range(10)]
print(el)

el = [i*i for i in range(10) if i % 2 == 0]
print(el)

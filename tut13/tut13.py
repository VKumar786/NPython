'''
    TODO: For Loops in Python | Python Tutorial - Day #17 
'''

name = "vishal kumar"
for ch in name:
    print(ch, end=" ")
print()

colors = ["red", "yellow", "green"]
for color in colors:
    for ch in color:
        print(ch, end=":")
    print()

for i in range(20):
    print(i)

for i in range(1, 21, 2):
    print(i)

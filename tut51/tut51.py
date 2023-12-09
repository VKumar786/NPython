'''
    TODO: Exercise 5 - Snake Water Gun | Python Tutorial - Day #55 
'''

import random

arr = ["Snake", "Water", "Gun"]

print("Option are")

for el, idx in enumerate(arr):
    print(f"{idx+1}. {el}")

x = int(input("Select One Option (1-3) :: ")) - 1
_x = random.randint(0, 2)

if (x == _x):
    print("Draw")
    pass
elif (x == 0 and _x == 1) or (x == 1 and _x == 2) or (x == 2 and _x == 0):
    print("User Win 😊")
    pass
else:
    print("Computer Win 😊")
    pass

'''
             S W G
Computer =   0 1 2
Player = S 0 D W L
         W 1 L D W
         G 2 W L D
         
D = Draw
W = Win
L = Loose
'''

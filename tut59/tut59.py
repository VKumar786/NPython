'''
    TODO: Snake Water Gun Game in Python - Exercise 5 - Solution | Python Tutorial - Day #63 
'''

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


import random
computer = random.randint(0, 1)

res = [["Draw", "Win", "Loose"],
       ["Loose", "Draw", "Win"],
       ["Win", "Loose", "Draw"]]

content = ["Snake", "Water", "Gun"]

print("Option are")
for idx, el in enumerate(content):
    print(f"{idx+1}. {el}")

human = int(input("Select One Option (1-3) :: ")) - 1

print(f"you {res[human][computer]}")

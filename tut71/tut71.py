'''
    TODO: Exercise 7 Solution + Shutouts | Python Tutorial - Day #75 
'''

import os

for i in os.listdir("tut64"):
    if i.endswith(".txt"):
        os.rename(f"tut64/{i}", f"tut64/{i[:-4]}.py")
        # print(i[:-4])
    pass

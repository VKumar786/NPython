'''
    TODO: Enumerate Function in Python | Python Tutorial - Day #42 
'''

arr = [12,2,23,534,2,556,454,5]

for idx, el in enumerate(arr):
    print(idx, el)
    
    
fruits = ['apple', 'banana', 'mango']
for idx, el in enumerate(fruits, start=1):
    print(f"{idx} :: {el}")
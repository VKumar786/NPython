'''
    TODO: Walrus Operator in Python | Python Tutorial - Day #86 
'''

a = True
print(a := False)

arr = [1,2,4,2,1,2]

while n := len(arr) > 0:
    print(arr.pop())
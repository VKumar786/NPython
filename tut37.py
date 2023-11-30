'''
    TODO: Short hand if else statements | Python Tutorial - Day #41 
    ? result = value_if_true if condition else value_if_false
'''

a, b = 10, 20

print("A") if a > b else print("==") if a == b else print("B")

c = 999 if a < b else -1
print(c)
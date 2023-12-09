'''
    TODO: Exercise 4: Secret Code Language | Python Tutorial - Day #40 
'''

data = input("Enter Data : ")
data = data.split()

print("Options are")
print("A. Encrypt".center(20))
print("B. Decode".center(20))

reply = input()

if (reply.lower() == "a"):
    for idx, el in enumerate(data):
        if (len(el) <= 3):
            data[idx] = el[::-1]
        else:
            data[idx] = el[1:] + el[0]
    pass
elif (reply.lower() == "b"):
    for idx, el in enumerate(data):
        if (len(el) <= 3):
            data[idx] = el[::-1]
        else:
            data[idx] = el[-1] + el[:len(el)-1] 
    pass

print(" ".join(data))

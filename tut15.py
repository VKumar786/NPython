'''
    TODO: break and continue in Python | Python Tutorial - Day #19 
'''

for i in range(10):
    if(i == 2):
        print("[]",end="")
        continue
    elif(i >= 8):
        break;
    print(i, end="$")
    
    
# Do while syntax
i = 0
while True:
    print(i)
    i += 1
    if(i%100 == 0):
        break
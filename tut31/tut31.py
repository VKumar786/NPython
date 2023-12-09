'''
    TODO: for Loop with else in Python | Python Tutorial - Day #35 
    ! else part will not be executed when break is applied
    ? else means loop have ended.
'''

for i in range(5):
    print(i, end=":")
else:
    print("hi 😈")
print()

for i in range(5):
    print(i, end=":")
    if (i == 3):
        break
else:
    print("hi 😈")
print()

i = 0
while i < 5:
    print(i)
    i += 1
    if(i == 3):
        break;
else:
    print("hi 😈")
print()

'''
    TODO: Local vs Global Variables in Python| Python Tutorial - Day #48 
'''

x = 4
print(x) # Global Variable

def Hello():
    global x
    x = 5
    print(x) # Local Variable

Hello()
print(x)

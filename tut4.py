'''
    TODO: Exercise 1: Calculator using Python | Python Tutorial - Day #7
    TODO: Exercise 1: Calculator using Python (Solution) | Python Tutorial - Day #8
'''

# Athematic Operation => +, -, *, /, //, %, **

a, b = [int(x) for x in input().split()]

print("Press Key For Operation \n1. Add\n2. Sub\n3. Multi\n4. Division")
c = int(input())

if(c == 1):
    print("Value of", a, "+", b, "is:",a+b)
elif (c == 2):
    print("Value of", a, "-", b, "is:",a-b)
elif (c == 3):
    print("Value of", a, "*", b, "is:",a*b)
elif (c == 4):
    print("Value of", a, "//", b, "is:",a//b)


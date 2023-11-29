'''
    TODO: Recursion in Python | Python Tutorial - Day #30 
'''


def Factorial(n):
    if n == 1:
        return n
    else:
        return n * Factorial(n-1)


print(Factorial(5))


def Fib(n):
    if (n <= 1):
        return n

    return Fib(n-1) + Fib(n-2)

print(Fib(5))
print(Fib(6))

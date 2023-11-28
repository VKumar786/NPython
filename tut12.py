'''
    TODO: Match Case Statements in Python | Python Tutorial - Day #16 
    ? break statement is not important
    ? case _ is default case
'''

n = int(input())

match n:
    case 0:
        print("value is 0")
    case 4:
        print("value is 4")
    case _ if n % 2 == 0:
        print("n is even")
    case _:
        print("default case is hit")

'''
    TODO: Exception Handling in Python | Python Tutorial - Day #36 
'''

try:
    n = int(input("Enter a number : "))
    print(n*121)
except Exception as e:
    print(e)
print("End of program")


try:
    n = int(input("Enter a number : "))
    print(n*121)
except:
    print("Invalid Input")
print("End of program")


try:
    n = int(input("Enter a number : "))
    arr = [34, 25]
    print(arr[n])
except ValueError:
    print("Value Error")
except IndexError:
    print("Index Error")
except:
    print("Some Error")
print("End of program")

'''
    TODO: Finally keyword in Python | Python Tutorial - Day #37 
    ! main use of finally when we use return statement inside your try except
'''

# Sample 2


def func():
    try:
        n = int(input("Enter a number : "))
        arr = [34, 25]
        print(arr[n])
        return 1
    except:
        print("Some Error")
        return 0
    finally:
        print("It will be executed weather exception occur or not || it is always executed")


print(func())

# Sample 1
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
finally:
    print("It will be executed weather exception occur or not || it is always executed")
print("End of program")

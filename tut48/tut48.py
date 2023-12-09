'''
    TODO: Lambda functions in Python | Python Tutorial - Day #52 
    ? lambda function is used when we are using function as argument
'''

double = lambda x : (x*(x+1))/2
# def double(x): return (x*(x+1))/2
cube = lambda x : x*x*x

avg2 = lambda x,y : (x+y)/2

avg = lambda arr : sum(arr)/len(arr)

print(double(5))
print(cube(5))
print(avg2(3,5))
print(avg([2,31,4,53,6,5,3,8]))

def sample(fx, val):
    return 50 + fx(val)

print(sample(cube, 5))
print(sample(lambda x: (x*(x+1))/2, 5))

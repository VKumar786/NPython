'''
    TODO: Generators in Python | Python Tutorial - Day #91 
    ? If we want to minimize memory consumption 
'''


def my_generator():
    for i in range(10):
        yield i


el = my_generator()

print(next(el))
print(next(el))
print(next(el))
print(next(el))
print(next(el))

for i in el:
    print(f"--{i}")
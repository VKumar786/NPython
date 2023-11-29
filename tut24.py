'''
    TODO: f-strings in Python | Python Tutorial - Day #28 
    ? use index while placing in this string
        * "My name is {1}, and I am from {0}"
'''

print(f"My name is {{name}}, I am from {{country}}")

price = 45.02451

print("Price is {price:.2f}".format(price = price))
print(f"Price is {price:.2f}")
print(f"Price is {2*3}")

name = "Vishal"
country = "India"

print("My name is {}, and I am from {}".format(name, country))
print("My name is {1}, and I am from {0}".format(country, name))


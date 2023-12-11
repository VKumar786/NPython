# foods = []

# while True:
#     food = input("what food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# print(foods)

foods = []

while (food := input("what food do you like?")) != "quit":
    foods.append(food)
    
print(foods)
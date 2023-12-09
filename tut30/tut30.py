'''
    TODO: Dictionary Methods in Python | Python Tutorial - Day #34 
'''

new_word_dict = {
    "name": "vishal",
    "python": "A high-level programming language known for its readability and versatility.",
    "algorithm": "A step-by-step procedure or formula for solving problems.",
    "database": "A structured collection of data, typically stored and accessed electronically.",
    "machine_learning": "A field of artificial intelligence that enables systems to learn and improve from experience.",
    "cloud_computing": "A technology that allows access to computing resources over the internet on a pay-as-you-go basis."
}

word_dict = {
    "python": "Programming language",
    "algorithm": "Problem-solving procedure",
    "database": "Data storage",
    "machine_learning": "AI learning",
    "cloud_computing": "Internet-based computing"
}

word_dict["name"] = "vivek"
print(word_dict["name"])

word_dict.update(new_word_dict)
print(word_dict)

word_dict.clear()
print(word_dict)

word_dict = {}
print(word_dict)

new_word_dict.pop("name")
print(new_word_dict)

# The popitem() method removes the last key-value pair from the dictionary.
new_word_dict.popitem()
print(new_word_dict)

# we can also use the del keyword to remove a dictionary item.
new_word_dict["name"] = "vishal"
del new_word_dict["name"]

for key, val in new_word_dict.items():
    print(f"[{key}] {val}")

del word_dict
    
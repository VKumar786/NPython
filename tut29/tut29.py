'''
    TODO: Dictionaries in Python | Python Tutorial - Day #33 
    ? Before py v3.7 Diconaries are unordered but after that Diconaries are ordered
    ! Ordered Data Structure
'''

dict1 = {
    1: "vishal",
    2: "vivek",
    3: "jadu"
}

print(dict1[2])

word_dict = {
    "python": "A high-level programming language known for its readability and versatility.",
    "algorithm": "A step-by-step procedure or formula for solving problems.",
    "database": "A structured collection of data, typically stored and accessed electronically.",
    "machine_learning": "A field of artificial intelligence that enables systems to learn and improve from experience.",
    "cloud_computing": "A technology that allows access to computing resources over the internet on a pay-as-you-go basis."
}

print(word_dict["algorithm"])  # raise exception
print(word_dict.get("database"))

for key in word_dict.keys():
    print(f"key : {key}, value = {word_dict[key]}")
print()

for item in word_dict.items():
    (k, v) = item
    print(f"key : {k}, value : {v}")
print()

for value in word_dict.values():
    print(f"value :  {value}")
print()

for key, value in word_dict.items():
    print(f"key : {key}, value : {value}")
    

'''
    TODO: Strings Slicing and Operations on Strings in Python | Python Tutorial - Day #12 
'''

name = "My name is khan"

print(len(name))

# [start_index, end_index], if start_index > end_index then return blank string
# return string will be from start_index to end_index - 1
print(name[0:5])
print(name[:5])
print(name[1:])

# Negative index name[:-3] === name[:len(name)-3]
print(name[:-3])
print(name[:len(name)-3])

# Negative index name[:-3] > name[:len(name)-3]
print(name[-3:-1])
print(name[len(name)-3:len(name)-1])

for ch in name:
    print(ch)
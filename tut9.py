'''
    TODO: String Methods in Python | Python Tutorial - Day #13 
    ? on applying method of string, new string is generated
    ? string are immutable => can't be changed
'''

name = "King"

print(len(name))

# The upper() method converts a string to upper case.
print(name.upper())

# The lower() method converts a string to lower case.
print(name.lower())

# rstrip - only trim trailing char or string
name = "!!!King!!!!!!"
print(name.rstrip("!"))

# The replace() method replaces all occurences of a string with another string. Example:
print(name.replace("King", "BadGuy😈"))

# The split() method splits the given string at the specified instance and returns the separated strings as list items.
name = "vishal vivek yash suraj vineet"
print(name.split(" "))

# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
name = "king reMaiN a King"
print(name.capitalize())

# The center() method aligns the string to the center as per the parameters given by the user.
# it will add X char to front of string
print(name.center(50))
print(name.center(50, "."))

# The count() method returns the number of times the given value has occurred within the given string.
print(name.count("King"))

# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
print(name.endswith("King"))
# endWith(str, start, end)
print(name.endswith("King", 2, 20))

# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
print(name.find("a"))
print(name.find("a1"))

# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
print(name.index("a"))  # if string not found return exception

# The strip() method removes any white spaces before and after the string.
name = " King   King "
print(name.strip())

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
name = "KingKing"
print(name.isalnum())

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(name.isalpha())

# The islower() method returns True if all the characters in the string are lower case, else it returns False.
print(name.islower())

# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
print(name.isprintable())
name = name + "\n"
print(name.isprintable())

# The isspace() method returns True only and only if the string contains white spaces, else returns False.
print(name.isspace())
name = "        "
print(name.isspace())

# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
name = "World Health Organization"
print(name.istitle())

# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
print(name.isupper())

# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
print(name.startswith("World"))

# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
print(name.swapcase())

# The title() method capitalizes each letter of the word within the string.
name = name.lower()
print(name)
print(name.title())
'''
    TODO: Regular Expressions in Python | Python Tutorial - Day #95 
    ? Metacharacters in regular expressions
        []  Represent a character class
        ^   Matches the beginning
        $   Matches the end
        .   Matches any character except newline
        ?   Matches zero or one occurrence.
        |   Means OR (Matches with any of the characters
            separated by it.
        *   Any number of occurrences (including 0 occurrences)
        +   One or more occurrences
        {}  Indicate number of occurrences of a preceding RE 
            to match.
        ()  Enclose a group of REs
    ? search -- for first match in text
    ? finditer -- for all match in text
    ! regexr.com
'''

import re

pattern = f"[A-Z]+han"
text = "My Name is Khan Than"

print(re.search(pattern, text))

print([match for match in re.finditer(pattern, text)])

print([text[match.span()[0]:match.span()[1]]
      for match in re.finditer(pattern, text)])

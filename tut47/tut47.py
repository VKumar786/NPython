'''
    TODO: seek(), tell() and other functions | Python Tutorial - Day #51 
'''

with open("tut47/text.txt", "r") as f:
    print(type(f))

    f.seek(10)  # move to 10th byte in file

    print(f.tell())  # retrieves the current position within a file.

    data = f.read(5)  # read next 5 byte

    print(data)

with open("tut47/sample.txt", "w") as f:
    f.write("vishal kumar")

    # resize a file to a specified size or truncate it to a specified number of bytes.
    f.truncate(6)

with open("tut47/sample.txt", "r") as f:
    print(f.read())

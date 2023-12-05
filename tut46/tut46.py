'''
    TODO: read(), readlines() and other methods | Python Tutorial - Day #50 
'''

with open("tut46/k.txt") as f:
    while True:
        line = f.readline()
        if not line:
            print(line, type(line))
            break
        print(line)

with open("tut46/marks.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        m1 = line.split(",")[0]
        m2 = line.split(",")[1]
        m3 = line.split(",")[2]
        print(f"Marks in Python {m1}, C++ {m2}, Java {m3}")

content = [
    "From Wikipedia, the free encyclopedia\n",
    "HackingTeamHacking Team logo: Hacking Team\n",
    "Industry	Information technology\n",
]

with open("tut46/write.txt", "w") as f:
    f.writelines(content)
    
with open("tut46/write.txt", "+a") as f:
    for line in content:
        f.write(line)
        
'''
    TODO: os Module in Python | Python Tutorial - Day #46 
'''

import shutil
import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(1, 101):
    if not os.path.exists(f"data/day{i}"):
        os.mkdir(f"data/day{i}")

    if not os.path.exists(f"data/day{i}/main.py"):
        with open(f"data/day{i}/main.py", "w") as file:
            file.write("print('ji')")

    if os.path.exists(f"data/day{i}/main.py"):
        os.rename(f"data/day{i}/main.py", f"data/day{i}/main1.py")

    if not os.path.exists(f"data/Tutorial {i}"):
        os.rename(f"data/day{i}", f"data/Tutorial {i}")

# find how many folder are there
folders = os.listdir(f"data")

for folder in folders:
    # print(folder)
    print(os.listdir(f"data/{folder}"))


# command run using system

os.system("date")

# change dir

print(os.getcwd())

os.chdir("/home/vkumar/VsCodeProjects/NPython/data")

print(os.getcwd())

os.chdir("/home/vkumar/VsCodeProjects/NPython")

# remove dir

# os.rmdir("data")

# Delete directory 'data' and all its contents
shutil.rmtree("data")

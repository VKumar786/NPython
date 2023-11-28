'''
    TODO: Exercise 2: Good Morning Sir | Python Tutorial - Day #15 
    ? strftime("%H:%M:%S") === strftime("%H:%M:%S", localtime(time()))
'''

from time import strftime, localtime, time

date = strftime("%H:%M:%S", localtime(time()))
[hr, mn, sc] = [int(x) for x in date.split(":")]

print(hr, mn, sc)

if (0 <= hr < 12):
    print("Good Morning BadGuy😈")
elif (12 <= hr < 6):
    print("Good Afternoon BadGuy😈")
else:
    print("Good Evening BadGuy😈")

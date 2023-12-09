'''
    TODO: Exercise 2: Solution | Python Tutorial - Day #26 
'''

from time import strftime, localtime, time

date = strftime("%H:%M:%S", localtime(time()))
[hr, mn, sc] = [int(x) for x in date.split(":")]

if (0 <= hr < 12):
    print("Good Morning BadGuy😈")
elif (12 <= hr < 18):
    print("Good Afternoon BadGuy😈")
else:
    print("Good Evening BadGuy😈")

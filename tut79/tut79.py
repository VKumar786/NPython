'''
    TODO: Exercise 9 - Shutouts to Everyone | Python Tutorial - Day #83 
'''

import pyttsx3
engine = pyttsx3.init()

names = ["vishal", "viky", "arjun"]

for name in names:
    engine.say(f"Shutouts to {name}")

engine.runAndWait()
engine.stop()

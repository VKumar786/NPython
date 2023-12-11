'''
    TODO: Exercise 9 - Shutouts to Everyone | Python Tutorial - Day #83 
'''

import pyttsx3
engine = pyttsx3.init()

arr = ["vishal", "viky", "arjun"]

engine.say("Hello World!")
engine.runAndWait()
engine.stop()

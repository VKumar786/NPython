'''
    TODO: Exercise 11 - Drink Water Reminder | Python Tutorial - Day #94 
'''

from plyer import notification
import time
import pygame

pygame.init()

# Load the music
pygame.mixer.music.load(
    '/home/bakru_k78/VsCodeProject/NPython/tut89/audio_bf0304c79f.mp3')

while True:
    notification.notify(title="hello", message="BOII", timeout=2)
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.mixer.music.stop()
    time.sleep(8)

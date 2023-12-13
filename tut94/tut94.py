'''
    TODO: Exercise 11: Solution + Shutouts - Desktop Notification System | Python Tutorial - Day #99 
'''


from plyer import notification
import time
import pygame

pygame.init()

# Load the music
pygame.mixer.music.load(
    '/home/bakru_k78/VsCodeProject/NPython/tut89/audio_bf0304c79f.mp3')

while True:
    notification.notify(title="hello", message="BOII", timeout=4)
    pygame.mixer.music.play()
    time.sleep(4)
    pygame.mixer.music.stop()
    time.sleep(8)

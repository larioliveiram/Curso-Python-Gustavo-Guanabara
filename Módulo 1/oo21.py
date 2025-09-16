# Write a Python program that opens and plays the audio from an MP3 file.

import pygame
pygame.init()
pygame.mixer.music.load('oo21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()







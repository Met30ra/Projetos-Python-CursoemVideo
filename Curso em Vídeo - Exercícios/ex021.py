import pygame
pygame.mixer.init()
pygame.mixer.music.load('Apex Theme.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():pass

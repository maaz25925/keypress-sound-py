import pygame
from pygame import mixer
import sys

pygame.init()

mixer.init()
mixer.music.load(
    "Mechanical-Keyboard-single-button-presses-1-www.FesliyanStudios.com.mp3"
)


display = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Keypress Sound")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            mixer.music.play()

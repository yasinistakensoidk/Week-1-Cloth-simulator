from classes import *
from tkinter import *
import pygame

Particles = []

Win = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

run = True

while run:
    for event in pygame.event.get():
        if EventType == pygame.QUIT:
            run = False
    
    pygame.display.update()


pygame.quit()
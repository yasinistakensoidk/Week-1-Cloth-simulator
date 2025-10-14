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
        elif EventType == pygame.MOUSEBUTTONDOWN: # checking if the left mouse button was clicked to determine if a connection was cut
            #lets define a vector for the mousepath:
            mousePath = () # start_x, start_y, end_x, end_y
            # we need to update every node so we need to determine which connection we severed.
            for n in Particles:
                print(n.position, n.parents, n.siblings, n.children)
    
    pygame.display.update()


pygame.quit()
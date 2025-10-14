from classes import *
from tkinter import *
import pygame

Particles = []

Win = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

run = True

def create_Fabric(x=10, y=10, l=10):
    for i in range(x):
        for j in range(y):
            Particles.append(particle(i*l, j*l, (y*i)+(j), depth=j, parents=[y*(i-1)+j]), children=[y*(i+1)+j], siblings=[y*i+j-1, y*i+j+1])

Win.fill("White")

while run: 
    
    for p in Particles:
        pygame.draw.circle(Win, center=(p.position[0], -p.position[1]), colour="BLACK", radius=5)
    
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
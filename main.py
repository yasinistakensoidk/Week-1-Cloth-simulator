from classes import *
from tkinter import *
import pygame

Particles = []

Win = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

run = True

def create_Fabric(x=10, y=100, l=50):
    global Particles
    
    for i in range(x):
        for j in range(y):
            #Particles.append(particle(i*l, j*l, (y*i)+(j), depth=j, parents=[y*(i-1)+j], children=[y*(i+1)+j], siblings=[y*i+j-1, y*i+j+1]))
            Particles.append(particle(j*l, i*l, (y*j)+(i), depth=j, children = [], siblings = [], parents = []))
            if (y*(i+1)+j) < x*y:
                Particles[(y*i)+(j)].children.append(y*(i+1)+j)
            if 0<j:
                Particles[(y*i)+(j)].siblings.append(y*i+j-1)
            if j < y-1:
                Particles[(y*i)+(j)].siblings.append(y*i+j+1)
            
            print(y*i+j, Particles[y*i+j].children, Particles[y*i+j].siblings)


Win.fill("White")

create_Fabric()

while run: 
    for p in Particles: # drawing
        #if p.index%10 == 0:
        pygame.draw.circle(Win, center=(p.position[0]+100, p.position[1]+100), color="black", radius=5) # we draw all our nodes
            
        #drawing our fibres
        for child in p.children: # {ADD FEATURE} we will only draw fibres if it connects a node with a node of smaller index      
            pygame.draw.line(Win, start_pos=(p.position[0]+100, p.position[1]+100), end_pos=(Particles[child].position[0]+100, Particles[child].position[1]+100), color="red")
        for sibling in p.siblings:
            pygame.draw.line(Win, start_pos=(p.position[0]+100, p.position[1]+100), end_pos=(Particles[sibling].position[0]+100, Particles[sibling].position[1]+100), color="red")
        for parent in p.siblings:
            pygame.draw.line(Win, start_pos=(p.position[0]+100, p.position[1]+100), end_pos=(Particles[parent].position[0]+100, Particles[parent].position[1]+100), color="red")

    
    for event in pygame.event.get():
        if EventType == pygame.QUIT:
            run = False
        elif EventType == pygame.MOUSEBUTTONDOWN: # checking if the left mouse button was clicked to determine if a fibre was cut
            #lets define a vector for the mousepath:
            mousePath = () # start_x, start_y, end_x, end_y
            # we need to update every node so we need to determine which fibre we severed.
            for n in Particles:
                print(n.position, n.parents, n.siblings, n.children)
        pygame.display.update()
    #run = False

pygame.quit()
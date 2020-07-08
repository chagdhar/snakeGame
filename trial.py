import pygame
import time
import numpy as np
pygame.init()
gd = pygame.display.set_mode((600,600))
gd.fill([255,255,255])
pygame.display.set_caption("Snake")
clk = pygame.time.Clock()
pygame.draw.circle(gd,[205,0,205],(300,300),3)
crush = True
def grid(a,b):
    return(a*6,b*6)
while crush:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crush = False
        
    pygame.display.update()
    clk.tick(60)
pygame.quit()

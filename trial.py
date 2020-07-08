import pygame
import time
import numpy as np
pygame.init()
gd = pygame.display.set_mode((600,600))
gd.fill([255,255,255])
pygame.display.set_caption("Snake")
clk = pygame.time.Clock()
crush = True
while crush:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crush = False
        
    pygame.display.update()
    clk.tick(60)
pygame.quit()

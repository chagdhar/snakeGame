import pygame
import time
import random as rn
import numpy as np
pygame.init()
gd = pygame.display.set_mode((600,600))
gd.fill([255,255,255])
pygame.display.set_caption("Snake")
clk = pygame.time.Clock()
lis =[(x,y) for x in range(100) for y in range(100)]
crush = True
dot = False
dot_loc = ()
len_snake = 3
head_img = pygame.image.load("head.png")
body_img = pygame.image.load("point.png")
dot_img = pygame.image.load("dot.png")
head = (1,1)
vel = ""
snake = [head]
def grid(a,b):
    return((a*6,b*6))

while crush:
    gd.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crush = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if vel == "":
                if event.key == pygame.K_LEFT:
                    vel = "Left"
                if event.key == pygame.K_RIGHT:
                    vel = "Right"
                if event.key == pygame.K_UP:
                    vel = "Up"
                if event.key == pygame.K_DOWN:
                    vel = "Down"
            if vel =="Up":
                if event.key == pygame.K_LEFT:
                    vel = "Left"
                if event.key == pygame.K_RIGHT:
                    vel = "Right"
            if vel == "Down":
                if event.key == pygame.K_LEFT:
                    vel = "Left"
                if event.key == pygame.K_RIGHT:
                    vel = "Right"
            if vel == "Right":
                if event.key == pygame.K_DOWN:
                    vel = "Down"
                if event.key == pygame.K_UP:
                    vel = "Up"
            if vel == "Left":
                if event.key == pygame.K_UP:
                    vel = "Up"
                if event.key == pygame.K_DOWN:
                    vel = "Down"
    a,b = head
    if vel == "Down":
        b+=1
    if vel == "Up":
        b-=1
    if vel == "Right":
        a+=1
    if vel == "Left":
        a-=1
    head = (a%100,b%100)
    snake.append(head)
    if len(snake)>len_snake:
        snake = snake[1:]
    if not dot:
        difflis = [i for i in lis + snake if i not in lis or i not in snake]
        ndin = rn.randint(0,len(difflis))
        dot_loc = difflis[ndin]
        dot = True
    else:
        x,y = dot_loc
        gd.blit(dot_img,grid(x,y))
        if head == dot_loc:
            len_snake+=1
            dot = False
    for a in snake:
        x,y = a
        if head == a:
            gd.blit(head_img,grid(x,y))
        else:
            gd.blit(body_img,grid(x,y))
    pygame.display.update()
    clk.tick(10)
pygame.quit()
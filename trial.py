import pygame
import time
import random as rn
import numpy as np
pygame.init()
gd = pygame.display.set_mode((600,600))
gd.fill([255,255,255])
pygame.display.set_caption("Snake")
clk = pygame.time.Clock()
crush = True
dot = False
len_snake = 5
head_img = pygame.image.load("head.png")
body_img = pygame.image.load("point.png")
head = (1,1)
vel = ""
snake = [head]
def grid(a,b):
    return((a*6,b*6))
def snake_update():
    global snake, head
    snake.append(head)
    if len(snake)>len_snake:
        snake = snake[1:]
def play():
    global crush, clk, snake, head, vel
    while crush:
        gd.fill([255,255,255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crush = False
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if vel =="Up" or vel == "":
                    if event.key == pygame.K_LEFT:
                        vel = "Left"
                    if event.key == pygame.K_RIGHT:
                        vel = "Right"
                if vel == "Down" or vel == "":
                    if event.key == pygame.K_LEFT:
                        vel = "Left"
                    if event.key == pygame.K_RIGHT:
                        vel = "Right"
                if vel == "Right" or vel == "":
                    if event.key == pygame.K_DOWN:
                        vel = "Down"
                    if event.key == pygame.K_UP:
                        vel = "Up"
                if vel == "Left" or vel == "":
                    if event.key == pygame.K_UP:
                        vel = "Up"
                    if event.key == pygame.K_DOWN:
                        vel = "Down"
        snake_mov()
        snake_update()
        for a in snake:
            x,y = a
            if head == a:
                gd.blit(head_img,grid(x,y))
            else:
                gd.blit(body_img,grid(x,y))
        pygame.display.update()
        clk.tick(5)
def snake_mov():
    global head, vel
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

play()
pygame.quit()
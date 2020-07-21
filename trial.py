import random as rn
import time

import pygame

pygame.init()
gd = pygame.display.set_mode((600,600))
gd.fill([255,255,255])
pygame.display.set_caption("Snake")
clk = pygame.time.Clock()
lis =[(x,y) for x in range(100) for y in range(100)]
crush = True
head_img = pygame.image.load("head.png")
body_img = pygame.image.load("body.png")
dot_img = pygame.image.load("dot.png")
font = pygame.font.Font('freesansbold.ttf', 10)
check = 2
x_speed = 0
y_speed = 0
def grid(a):
	return tuple(t*6 for t in a)
while crush:
	if check>1:
		dot = False
		dot_loc = ()
		len_snake = 3
		x_speed = 0
		y_speed = 0
		head=(1,1)
		snake = [head]
	check =0
	typ = False
	gd.fill([255,255,255])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crush = False
		if event.type == pygame.KEYDOWN:
			typ = True
			event_key = event.key
	if typ:
		if x_speed+y_speed==0:
			if event_key == pygame.K_LEFT:
				x_speed = -1
				y_speed = 0
			if event_key == pygame.K_RIGHT:
				x_speed = 1
				y_speed = 0
			if event_key == pygame.K_UP:
				y_speed = -1
				x_speed = 0
			if event_key == pygame.K_DOWN:
				y_speed = 1
				x_speed = 0
		if y_speed == -1:
			if event_key == pygame.K_LEFT:
				x_speed = -1
				y_speed = 0
			if event_key == pygame.K_RIGHT:
				x_speed = 1
				y_speed = 0
		if y_speed == 1:
			if event_key == pygame.K_LEFT:
				x_speed = -1
				y_speed = 0 
			if event_key == pygame.K_RIGHT:
				x_speed = 1
				y_speed = 0
		if x_speed ==1:
			if event_key == pygame.K_DOWN:
				x_speed = 0
				y_speed = 1
			if event_key == pygame.K_UP:
				x_speed = 0
				y_speed = -1
		if x_speed == -1:
			if event_key == pygame.K_UP:
				x_speed = 0
				y_speed = -1
			if event_key == pygame.K_DOWN:
				x_speed = 0
				y_speed = 1
	head_x,head_y = head
	head_x += x_speed
	head_y += y_speed
	head = (head_x%100,head_y%100)
	snake.append(head)
	while len(snake)>len_snake:
		snake = snake[1:]
	if not dot:
		difflis = [i for i in lis if i not in snake]
		ndin = rn.randint(0,len(difflis))
		dot_loc = difflis[ndin]
		dot = True
	else:
		gd.blit(dot_img,grid(dot_loc))
		if head == dot_loc:
			len_snake+=1
			dot = False
	for a in snake:
		if head == a:
			gd.blit(head_img,grid(a))
		else:
			gd.blit(body_img,grid(a))
	for a in snake:
		if a == head:
			check+=1
	text = font.render("score = "+str(len_snake-3),True,(0,0,0),(255,255,255))
	textrec = text.get_rect()
	textrec.center = (570,10)
	gd.blit(text,textrec)
	pygame.display.update()
	clk.tick(10)
pygame.quit()

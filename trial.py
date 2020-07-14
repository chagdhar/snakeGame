import random as rn
import pygame
pygame.init()
gd = pygame.display.set_mode((600,600))
gd.fill([255,255,255])
pygame.display.set_caption("Snake")
clk = pygame.time.Clock()
lis =[(x,y) for x in range(100) for y in range(100)]
crush = True
head_img = pygame.image.load("head.png")
body_img = pygame.image.load("point.png")
dot_img = pygame.image.load("dot.png")
font = pygame.font.Font('freesansbold.ttf', 10)
len_snake = 0
def grid(a):
	return tuple(t*6 for t in a)
def reset():
	global dot, dot_loc,head,vel,snake,check,len_snake
	dot = False
	dot_loc = ()
	len_snake = 3
	vel = ""
	head=(1,1)
	snake = [head]
	check = 0
reset()
while crush:
	typ = False
	gd.fill([255,255,255])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crush = False
		if event.type == pygame.KEYDOWN:
			typ = True
			event_key = event.key
	if typ:
		if vel == "":
			if event_key == pygame.K_LEFT:
				vel = "Left"
			if event_key == pygame.K_RIGHT:
				vel = "Right"
			if event_key == pygame.K_UP:
				vel = "Up"
			if event_key == pygame.K_DOWN:
				vel = "Down"
		if vel =="Up":
			if event_key == pygame.K_LEFT:
				vel = "Left"
			if event_key == pygame.K_RIGHT:
				vel = "Right"
		if vel == "Down":
			if event_key == pygame.K_LEFT:
				vel = "Left"
			if event_key == pygame.K_RIGHT:
				vel = "Right"
		if vel == "Right":
			if event_key == pygame.K_DOWN:
				vel = "Down"
			if event_key == pygame.K_UP:
				vel = "Up"
		if vel == "Left":
			if event_key == pygame.K_UP:
				vel = "Up"
			if event_key == pygame.K_DOWN:
				vel = "Down"
	head_x,head_y = head
	if vel == "Down":
		head_y+=1
	if vel == "Up":
		head_y -=1
	if vel == "Right":
		head_x+=1
	if vel == "Left":
		head_x-=1
	head = (head_x%100,head_y%100)
	snake.append(head)
	if len(snake)>len_snake:
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
	if check>1:
		reset()
		clk.tick(15000)
	check =0
	text = font.render("score = "+str(len_snake-3),True,(0,0,0),(255,255,255))
	textrec = text.get_rect()
	textrec.center = (570,10)
	gd.blit(text,textrec)
	pygame.display.update()
	clk.tick(10)
pygame.quit()
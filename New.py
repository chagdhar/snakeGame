import random,pygame
lis =[(x,y) for x in range(100) for y in range(100)]
crush = True
head_img = pygame.image.load("head.png")
body_img = pygame.image.load("body.png")
dot_img = pygame.image.load("dot.png")
font = pygame.font.Font('freesansbold.ttf', 10)
segments_at_head_loc = 2
def grid(a):
    return tuple(t*6 for t in a)
while crush:
    if segments_at_head_loc>1:
        dot = False
        dot_loc = ()
        len_snake = 3
        x_speed = 0
        y_speed = 0
        head=(1,1)
        snake = [head]
    segments_at_head_loc =0
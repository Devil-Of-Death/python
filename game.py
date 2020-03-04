#! /usr/bin/python3
import random
import math
import pygame
pygame.init()
w=800
h=600
score=0
a=0
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("space invader")
icon=pygame.image.load("superpower(1).png")
pygame.display.set_icon(icon)

#player
player_=pygame.image.load("player.png")
x=360
y=480
temp=0

#enemy
enemy_=pygame.image.load("spaceship.png")
e_x=random.randint(0,800)
e_y=random.randint(50,150)
e_s=0.3
temp=0

#bullet
bullet_=pygame.image.load("bullet.png")
b_x=0
b_y=480
b_tf=False
b_state="ready"

def player(x1,y1):
    screen.blit(player_,(x1,y1))


def enemy(x1,y1):
    screen.blit(enemy_,(x1,y1))

def bullet(x1,y1):
    global b_state
    b_state="fire"
    screen.blit(bullet_,(x1,y1))

def iscol(ex,ey,bx,by):
    a=ex-bx
    d=math.sqrt(math.pow(ex-bx,2)+math.pow(ey-by,2))
    if d < 27:
        return True
    else:
        return False

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True,(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


#game loop
run=True
while run:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                temp=1.3

            if event.key == pygame.K_LEFT:
                temp=-1.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                temp=0

            if event.key == pygame.K_z:
                if b_state is "ready":
                    bullet(x,y)
                    b_x=x


    if x<=0:
        x=0

    elif x>=736:
        x=736



    x+=temp
    player(x,y)


    enemy(e_x,e_y)

    e_x+=e_s
    if e_x>=786:
        e_y+=20
        e_x=0

    if b_y == 0:
        b_state="ready"
        b_y=480
        b_x=0

    if b_state is "fire":
        bullet(b_x,b_y)
        b_y-=1

    if score%10==0 and score!=a:
        e_s+=0.1
        a=score

    col=iscol(e_x,e_y,b_x,b_y);
    if col:
        b_y=480
        b_state="ready"
        e_x=random.randint(0,800)
        e_y=random.randint(50,150)
        score+=1
    s="result: "+str(score)
    draw_text(screen,s,12,750,15)

    pygame.display.update()

import pygame
import random
import math
from pygame import mixer
#initializing the pygame:
pygame.init()

#creating a screen:
screen=pygame.display.set_mode((800,600))#width,height

#Creating title and icon:
pygame.display.set_caption("SPACE_INVADERS")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Creating background
background=pygame.image.load('background.jpg')

#sound and music:
mixer.music.load('background.wav')
mixer.music.play(-1)

#for the player:
playerimg=pygame.image.load('player.png')
player_x=370
player_y=480
player_x_change=0
player_y_change=0
def player(x,y):
    screen.blit(playerimg,(x,y))

#for the enemy:
enemyimg=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
no_of_enemy=10
for j in range(no_of_enemy):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(50,150))
    enemy_x_change.append(0.3)
    enemy_y_change.append(40)
def enemy(x,y,i):
    screen.blit(enemyimg[j],(x,y))

#for the attack:
bulletimg=pygame.image.load('bullet.png')
bullet_x=0
bullet_y=480
bullet_x_change=0
bullet_y_change=0.9
bullet_state="ready"
def fire(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))

#collition
def collition(enemy_x,enemy_y,bullet_x,bullet_y):
    distance=math.sqrt((math.pow(enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y,2)))#Distance bw two midpoint formula:D=sqrt((x2-x1)^2+(y2-y1)^2)
    if distance<27:
        return True
    else:
        return False

#score:
score=0
font=pygame.font.Font('freesansbold.ttf',32)
text_x=10
text_y=10
def show_score(x,y):
    score_n=font.render("Score:"+ str(score),True,(255,255,255))
    screen.blit(score_n,(x,y))

#gameover:
over_font=pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over_text=over_font.render("GAMEOVER",True, (255,255,255))
    screen.blit(over_text,(200,225))

#Game loop
runs=True
while runs:
    #setting background colour:
    screen.fill((0,0,0))# we have declared a variable screen in the above

    #Background image:
    screen.blit(background,(0,0))

    #Event loop:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            runs=False
    
    #KEYDOWN is for key press in your keyboard:
        if i.type==pygame.KEYDOWN:
            #for x direction:
            if i.key==pygame.K_LEFT:
                player_x_change = -0.6
            if i.key==pygame.K_RIGHT:
                player_x_change = 0.6
            if i.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
                    #getting coordinate from player
                    bullet_x=player_x
                    fire(bullet_x,bullet_y)


    #KEYUP is for key release in your keyboard:
        if i.type==pygame.KEYUP:
            #for x deirction:
            if i.key==pygame.K_LEFT or i.key==pygame.K_RIGHT:
                player_x_change=0
            
#for player-----------------------------
    #Adjusting x coordinates:
    player_x+=player_x_change

    #Setting boundary for x axis:
    if player_x<=0:
        player_x=0
    elif player_x>=736:#width-object pixel size-->800-64=736
        player_x=736

#for enemy-------------------------------  
    #Adjusting x coordinates:
    for j in range(no_of_enemy):
        enemy_x[j]+=enemy_x_change[j]
        if enemy_y[j]>440:
            for k in range(no_of_enemy):
                enemy_y[k]=2000
            game_over_text()
            break

    #Setting boundary for x axis:
        if enemy_x[j]<=0:
            enemy_x_change[j]=0.3
            enemy_y[j]+=enemy_y_change[j]
        elif enemy_x[j]>=736:#width-object pixel size-->800-64=736
            enemy_x_change[j]=-0.3
            enemy_y[j]+=enemy_y_change[j]

        #for collition----------------------------
        colloid=collition(enemy_x[j], enemy_y[j], bullet_x, bullet_y)
        if colloid:
            collition_sound=mixer.Sound('explosion.wav')
            collition_sound.play()
            bullet_y=480
            bullet_state="ready"
            score+=1
            enemy_x[j]=random.randint(0,735)
            enemy_y[j]=random.randint(50,150)
        enemy(enemy_x[j],enemy_y[j],j)
    
#for bullet----------------------------------
    if bullet_y<=0:
        bullet_y=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire(bullet_x,bullet_y)
        bullet_y-=bullet_y_change



    player(player_x,player_y)
    show_score(text_x,text_y)
    pygame.display.update()
    

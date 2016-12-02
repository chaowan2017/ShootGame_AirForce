# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:05:00 2016

@author: Chao Wan
"""

import pygame
from sys import exit
from pygame.locals import *
from gameRole import *
from menu import *
from Buttons import *
from Level import *
import pygame, Buttons
import random
from Characters import *
import os
import ctypes
from GamePlayer import *

class scorestruct:
   def __init__(self, name, score):
        self.name = name
        self.score = score

if __name__ == "__main__":
    # Creating the screen



    item=[]

    if os.path.exists(r'score.txt')==False:
        f=open('score.txt','w')
        for i in range(0,5):
            f.write(str(0)+':'+'\n')
        f.close()
    f = open("score.txt", "r")
    for i in range(0,5):
        line = f.readline()
        if line:
            line=line.strip()
            p=line.rfind(':')
            len=line.__len__()
            aa= scorestruct(line[p+1:len],int(line[0:p]))
            item.append(aa)
    f.close()





    win=GraphWin("AirCraft 2016",340, 300)
    win.setBackground(color_rgb(255,0,0))
    operate=GameMenu(win).operate
    if operate==1:
      win=GraphWin("Choose level",340, 300)
      win.setBackground(color_rgb(255,0,0))
      g_speed=GameLevel(win).speed
      win=GraphWin("Choose characters",360,320)
      win.setBackground(color_rgb(255,0,0))
      g_speed=GameCharacters(win).speed
      screen = pygame.display.set_mode((480, 800), 0, 32)
      pygame.display.set_caption('AirCraft 2016 by Chao Wan')



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AirCraft 2016 by Chao Wan')


bullet_sound = pygame.mixer.Sound('resources/sound/bullet.wav')
enemy1_down_sound = pygame.mixer.Sound('resources/sound/enemy1_down.wav')
game_over_sound = pygame.mixer.Sound('resources/sound/game_over.wav')
bullet_sound.set_volume(0.3)
enemy1_down_sound.set_volume(0.3)
game_over_sound.set_volume(0.3)
pygame.mixer.music.load('resources/sound/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# background Image
background = pygame.image.load('resources/image/background.png').convert()
game_over = pygame.image.load('resources/image/gameover.png')

filename = 'resources/image/shoot.png'
plane_img = pygame.image.load(filename)

# setting player index
player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos,g_speed)

# bullets' surface index
bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

# surface index
enemy1_rect = pygame.Rect(534, 612, 57, 43)
enemy1_img = plane_img.subsurface(enemy1_rect)
enemy1_down_imgs = []
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

enemies1 = pygame.sprite.Group()

# plane crushed
enemies_down = pygame.sprite.Group()

shoot_frequency = 0
enemy_frequency = 0
enemy_movespeed=0

player_down_index = 16

score = 0

clock = pygame.time.Clock()

running = True

while running:
    # REFRESHRATE
    clock.tick(60)

    # CONTROL BULLETS
    if not player.is_hit:
        if shoot_frequency % 95 == 0:
            bullet_sound.play()
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    # MAKE ENEMIES
    if enemy_frequency % 75 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos,g_speed,enemy_movespeed)
        enemies1.add(enemy1)
    enemy_frequency += 1
    enemy_movespeed+=1
    if score >= 5000:
        enemy_frequency += 5
        enemy_movespeed += 50
    if enemy_frequency >= 100:
        enemy_frequency = 0


    # MOVE BULLETS
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    # MOVE ENEMIES
    for enemy in enemies1:
        enemy.move()
        #JUDGE IF PLAYER IS SHOT
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            game_over_sound.play()
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies1.remove(enemy)




    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)


    screen.fill(0)
    screen.blit(background, (0, 0))

    # players' plane
    if not player.is_hit:
        screen.blit(player.image[player.img_index], player.rect)
        # animate
        player.img_index = shoot_frequency // 12
    else:
        player.img_index = player_down_index // 12
        screen.blit(player.image[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index > 47:
            running = False


    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            enemy1_down_sound.play()
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            score += 1000
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)
        enemy_down.down_index += 1

    # bullets and enemies
    player.bullets.draw(screen)
    enemies1.draw(screen)
    # score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)
    # refresh
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Controlling Keyboard
    key_pressed = pygame.key.get_pressed()
    # Lose
    if not player.is_hit:
        if key_pressed[K_w] or key_pressed[K_UP]:
            player.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            player.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveRight()


font = pygame.font.Font(None, 38)
text = font.render('YOU LOSE.PLAY AGAIN '+ str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(game_over, (0, 0))
screen.blit(text, text_rect)
lastscore= item[4]
if score>lastscore.score:
   ctypes.windll.user32.MessageBoxW(0, u'You are on the list, please input your name', u'caption',0)
   winname=GraphWin("Name",300, 230)
   winname.setBackground(color_rgb(255,0,0))
   namestr=GamePlayer(winname).namestr
   aa= scorestruct(namestr,score)
   if score>=item[0].score:
        item.insert(0,aa)
   else:
       for i in range(1,5):
           if score<item[i-1].score and score>=item[i].score:
                item.insert(i,aa)

   f=open('score.txt','w')
   for i in range(0,5):
        f.write(str(item[i].score)+':'+item[i].name+'\n')
   f.close()






while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

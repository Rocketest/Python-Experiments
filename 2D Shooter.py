'''
Assets:-
  bullet.png
  player.png

You will have to install these modules to get this to run. Ask permission first from the computer owner (or your parents if you're under-18):-
  pgzero
  pygame
  numpy
Command for installation (for Command Prompt/Terminal):-
It will look something like this:-
  C:\Users\yourusername\AppData\Local\Programs\Python\Python39\python.exe -m pip install pgzero pygame numpy
'''
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
import pgzrun
from time import time
import numpy as np

TITLE = "2D Shooter"
HEIGHT = 600
WIDTH = 600

delta_time = 1
last_time = time()
player = Actor("player")
player.pos = (300, 300)
bullets = []
bullet_data = []
enemies = []
enemy_data = []
fire_rate = 10

def update():
    global player, delta_time, last_time, bullets, bullet_data, fire_rate, enemies, enemy_data
    #calculate delta time
    delta_time = (time() * 30) - last_time
    last_time = time() * 30
    #clear screen
    screen.fill("gray")
    #move player
    if keyboard.left:
        player.angle += 2 * delta_time
    if keyboard.right:
        player.angle -= 2 * delta_time
    angle_trig = [np.sin(np.radians(0 - player.angle)), np.cos(np.radians(0 - player.angle))]
    if keyboard.up:
        player.x += (2 * angle_trig[0])* delta_time
        player.y += (-2 * angle_trig[1])* delta_time
    if keyboard.down:
        player.x += (-2 * angle_trig[0])* delta_time
        player.y += (2 * angle_trig[1])* delta_time
    #shoot bullets
    if keyboard.space:
        if fire_rate == 10:
            fire_rate = 0
            bullets.append(Actor("bullet"))
            bullet_data.append([player.x + (10 * angle_trig[0]), player.y + (-10 * angle_trig[1]), 5 * angle_trig[0], -5 * angle_trig[1]])
            bullets[len(bullets) - 1].angle = player.angle
        else:
            fire_rate += 1
    else:
        fire_rate = 10
    #add enemies
    '''----------------------------------'''
    #draw actors and update bullets and enemies
    i = len(bullets) - 1
    while i > (-1):
        bullet_data[i][0] += bullet_data[i][2] * delta_time
        bullet_data[i][1] += bullet_data[i][3] * delta_time
        
        bullets[i].pos = (bullet_data[i][0], bullet_data[i][1])
        bullets[i].draw()
        if (bullet_data[i][0] < -20 or bullet_data[i][0] > 620) or (bullet_data[i][1] < -20 or bullet_data[i][1] > 620):
            bullets.pop(i)
            bullet_data.pop(i)
        i -= 1
    player.draw()
pgzrun.go()

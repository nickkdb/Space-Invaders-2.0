import pygame
import sys
from setup import load_img, SCREENRECT
from player import Player
from alien import Alien
from bullet import Bullet
from level import Level

#GAME VARIABLES 
screen = pygame.display.set_mode(SCREENRECT.size)
clock = pygame.time.Clock()
bgtile = pygame.transform.smoothscale(load_img("spacebg.png"), SCREENRECT.size)
background = pygame.Surface(SCREENRECT.size)
level = Level(screen)

#move= [UP,RIGHT,DOWN,LEFT]
playerMoves = [False,False,False,False]


# GAME LOOP

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerMoves[3] = True
            if event.key == pygame.K_RIGHT:
                playerMoves[1] = True
            if event.key == pygame.K_UP:
                playerMoves[0] = True
            if event.key == pygame.K_DOWN:
                playerMoves[2] = True
            if event.key == pygame.K_SPACE:
                level.pushBullet()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerMoves[3] = False
            if event.key == pygame.K_RIGHT:
                playerMoves[1] = False
            if event.key == pygame.K_UP:
                playerMoves[0] = False
            if event.key == pygame.K_DOWN:
                playerMoves[2] = False


    screen.blit(bgtile, (0,0))
    level.runGame(playerMoves) 

    pygame.display.flip()
    clock.tick(60)
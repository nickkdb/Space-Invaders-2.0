import pygame
import sys
from setup import load_img
from player import Player, SCREENRECT

#GAME VARIABLES 
screen = pygame.display.set_mode(SCREENRECT.size) # set game window
clock = pygame.time.Clock()

#PLAYER VARIABLES
#move= [UP,RIGHT,DOWN,LEFT]
move = [False,False,False,False]

#ENEMY VARIABLES
alienList = []

#ITEMS TO DISPLAY
bgtile = pygame.transform.smoothscale(load_img("spacebg.png"), SCREENRECT.size)
background = pygame.Surface(SCREENRECT.size)
ship = Player()

# GAME LOOP

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move[3] = True
            if event.key == pygame.K_RIGHT:
                move[1] = True
            if event.key == pygame.K_UP:
                move[0] = True
            if event.key == pygame.K_DOWN:
                move[2] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move[3] = False
            if event.key == pygame.K_RIGHT:
                move[1] = False
            if event.key == pygame.K_UP:
                move[0] = False
            if event.key == pygame.K_DOWN:
                move[2] = False


    screen.blit(bgtile, (0,0))

    ship.update(move)
    screen.blit(ship.image, ship.rect)
    pygame.display.flip()
    clock.tick(60)
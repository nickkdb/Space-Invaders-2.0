from json.tool import main
import pygame
import sys
from setup import load_img

#GAME VARIABLES 
SCREENRECT = pygame.Rect(0,0,800,600) #set up a rectangle for the screen to reference later
screen = pygame.display.set_mode(SCREENRECT.size) # set game window
clock = pygame.time.Clock()

#PLAYER VARIABLES
move_left = False
move_right= False
move_up = False
move_down = False

#ENEMY VARIABLES
alienList = []


#GAME LOOP

while True:
    bgtile = pygame.transform.smoothscale(load_img("spacebg.png"), SCREENRECT.size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bgtile, (0,0))
    pygame.display.flip()
    clock.tick(60)
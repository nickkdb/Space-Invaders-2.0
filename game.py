from json.tool import main
import pygame
import os
import sys

#GAME VARIABLES
main_dir = os.path.split(os.path.abspath(__file__))[0] #game path
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
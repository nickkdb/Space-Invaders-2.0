import pygame
from setup import load_img

ALIENSIZE = (64,36)

class Alien:
    speed = 4
    
    def __init__(self,x,y):
        self.image = pygame.transform.smoothscale(load_img('alien.png'), ALIENSIZE)
        self.rect = self.image.get_rect(center=(x,y))
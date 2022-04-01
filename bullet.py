import pygame
from setup import load_img

class Bullet:

    def __init__(self,x,y):
        self.image = pygame.transform.rotate(load_img('bullet.png'), 90)
        self.rect = self.setBullet(x,y)
        self.speed = 5

    def setBullet(self,x,y):
        return self.image.get_rect(topleft=(x,y))
        
    def update(self):
        # self.rect.centerx - 16, self.rect.y - 12
        self.rect.y -= self.speed
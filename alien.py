import pygame
from setup import load_img, SCREENRECT

ALIENSIZE = (64,36)

class Alien(pygame.sprite.Sprite):
    speed = 1
    direction = 1
    movingRight = True
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.transform.smoothscale(load_img('alien.png'), ALIENSIZE)
        self.rect = self.image.get_rect(topleft= (x,y))

    def shift(self):
        if Alien.switching:
            self.rect.x += Alien.speed * Alien.direction           
        if self.rect.left > 2 and self.rect.right < SCREENRECT.right:
            self.rect.x += Alien.speed * Alien.direction
        else:
            Alien.direction *= -1
            Alien.switching = True
    def update(self):
        if self.rect.right > 795 and Alien.movingRight:
            Alien.speed *= -1
            self.rect.x += Alien.speed
            Alien.movingRight = False
        elif self.rect.left < 5 and not Alien.movingRight:
            Alien.speed *= -1
            self.rect.x += Alien.speed
            Alien.movingRight = True
        else:
            self.rect.x += Alien.speed
    
    def checkForHit(self, bullet):
        if self.rect.colliderect(bullet):
            return True
        else:
            return False



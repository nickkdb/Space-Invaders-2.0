from setup import load_img
import pygame

SCREENRECT = pygame.Rect(0,0,800,600) #set up a rectangle for the screen to reference later
PLAYERSIZE = (64,64)
startingY = SCREENRECT.bottom - 50
startingX = SCREENRECT.centerx

class Player:

    def __init__(self):
        self.image = pygame.transform.smoothscale(load_img('player.png'), PLAYERSIZE)
        self.rect = self.image.get_rect(center=(startingX, startingY)) 
        self.speed = 4

    #Update IF within allowed area
    def update(self, move):
        if move[3] and self.rect.left > 0:
            self.rect.x -= self.speed
        if move[1] and self.rect.right < SCREENRECT.right:
            self.rect.x += self.speed
        if move[0] and self.rect.y >= SCREENRECT.bottom - 214: #arbitrary amount of space I decided ship can move
            self.rect.y -= self.speed
        if move[2] and self.rect.centery <= startingY: #ship can't go lower than where it starts
            self.rect.y = min(self.rect.y + self.speed, startingY) #Makes sure we never exceed starting value
import pygame
from bullet import Bullet
from player import Player
from alien import Alien
from explosion import Explosion

class Level:

    def __init__(self, screen):
        self.display = screen
        self.alienList = pygame.sprite.Group()
        self.player = Player()
        self.bulletList = []
        self.explosionList = []
        self.setAliens()

    def runGame(self, move):
        self.updateAliens()
        self.player.update(move)
        self.display.blit(self.player.image, self.player.rect)
        self.moveBullet()
        self.checkForExplosion()

    def pushBullet(self):
        bullet = Bullet(self.player.rect.centerx - 16, self.player.rect.y - 12)
        self.bulletList.append(bullet)

    def moveBullet(self):
        for shot in self.bulletList:
            self.display.blit(shot.image, shot.rect)
            shot.update() 

    def checkForExplosion(self):
        if len(self.explosionList) > 0:
            for explosion in self.explosionList:
                explosion.animate()
                complete = explosion.update()
                if complete: 
                    self.explosionList.remove(explosion)
                else:
                    self.display.blit(explosion.image, explosion.rect)

        


    def setAliens(self):
        alienMinX = 68
        alienMinY = 32
        alienPos = [alienMinX, alienMinY]
   
        for i in range(0,4):
            alienRow = []
            for j in range(0,9):
                alien = Alien(alienPos[0], alienPos[1])
                self.alienList.add(alien)
                alienPos[0] += 75     
            self.alienList.add(alienRow)
            alienPos[0] = alienMinX
            alienPos[1] += 50          

    def updateAliens(self): 
        for alienShip in self.alienList:
            alienShip.update()
            self.display.blit(pygame.transform.flip(alienShip.image, False, True), alienShip.rect)
            if len(self.bulletList) > 0:
                for bullet in self.bulletList:
                    if alienShip.rect.colliderect(bullet.rect):
                        self.explosionList.append(Explosion(alienShip.rect.center))
                        self.alienList.remove(alienShip)
                        self.bulletList.remove(bullet)
                        break
        
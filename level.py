import pygame
from bullet import Bullet
from player import Player
from alien import Alien

class Level:

    def __init__(self, screen):
        self.display = screen
        self.alienList = pygame.sprite.Group()
        self.player = Player()
        self.bulletList = []
        self.setAliens()

    def runGame(self, move):
        self.updateAliens()
        self.player.update(move)
        self.display.blit(self.player.image, self.player.rect)
        self.moveBullet()

    def pushBullet(self):
        bullet = Bullet(self.player.rect.centerx - 16, self.player.rect.y - 12)
        self.bulletList.append(bullet)

    def moveBullet(self):
        for shot in self.bulletList:
            self.display.blit(shot.image, shot.rect)
            shot.update() 

        


    def setAliens(self):
        alienMinX = 68
        alienMinY = 32
        alienPos = [alienMinX, alienMinY]
        # while len(alienList) < 4:
        #     alienRow = []
        #     while len(alienRow) < 9:
        #         alien = Alien(alienPos[0], alienPos[1])
        #         alienRow.append(alien)
        #         alienPos[0] += 75

        #     alienList.append(alienRow)
        #     alienPos[0] = alienMinX
        #     alienPos[1] += 50
        for i in range(0,4):
            alienRow = []
            for j in range(0,9):
                alien = Alien(alienPos[0], alienPos[1])
                # alienRow.append(alien)
                self.alienList.add(alien)
                alienPos[0] += 75     
            self.alienList.add(alienRow)
            alienPos[0] = alienMinX
            alienPos[1] += 50          
        # return alienList

    def updateAliens(self): 
        for alienShip in self.alienList:
            alienShip.update()
            self.display.blit(pygame.transform.flip(alienShip.image, False, True), alienShip.rect)
            if len(self.bulletList) > 0:
                for bullet in self.bulletList:
                    if alienShip.rect.colliderect(bullet.rect):
                        self.alienList.remove(alienShip)
                        self.bulletList.remove(bullet)
                        break
        
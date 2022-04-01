import pygame
import sys
from setup import load_img, SCREENRECT
from player import Player
from alien import Alien
from bullet import Bullet

#GAME VARIABLES 
screen = pygame.display.set_mode(SCREENRECT.size)
clock = pygame.time.Clock()
bgtile = pygame.transform.smoothscale(load_img("spacebg.png"), SCREENRECT.size)
background = pygame.Surface(SCREENRECT.size)

#PLAYER VARIABLES
#move= [UP,RIGHT,DOWN,LEFT]
move = [False,False,False,False]
ship = Player()
bulletList = []
playerFire = []
enemyHit = []


#ENEMY VARIABLES
alienList = []
# aliensList = pygame.sprite.Group()
alienMinX = 68
alienMinY = 32
alienPos = [alienMinX, alienMinY]

while len(alienList) < 4:
    alienRow = []
    while len(alienRow) < 9:
        alien = Alien(alienPos[0], alienPos[1])
        alienRow.append(alien)
        alienPos[0] += 75

    alienList.append(alienRow)
    alienPos[0] = alienMinX
    alienPos[1] += 50

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
            if event.key == pygame.K_SPACE:
                bullet = Bullet(ship.rect.centerx - 16, ship.rect.y - 12)
                bulletList.append(bullet)
                playerFire.append(True)
                enemyHit.append(False)
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

    for idx, shot in enumerate(bulletList):
        if playerFire[idx] and not enemyHit[idx]:
            screen.blit(shot.image, shot.rect)
            shot.update()            

    for row in alienList:
        for alienShip in row:
            for idx, shot in enumerate(bulletList):
                if alienShip.rect.colliderect(shot.rect):
                    row.remove(alienShip)
                    bulletList.remove(shot)
                    playerFire.pop(idx)
                    enemyHit.pop(idx)
                    continue
            alienShip.update()
            screen.blit(pygame.transform.flip(alienShip.image, False, True), alienShip.rect)

    pygame.display.flip()
    clock.tick(60)
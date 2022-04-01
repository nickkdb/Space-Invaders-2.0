import pygame
from bullet import Bullet
from player import Player
from alien import Alien

class Level:

    def __init__(self, screen):
        self.display = screen
        self.setAliens()

    def setAliens():
        self.aliens =
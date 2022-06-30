import pygame
import random
from settings import *


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")
        self.rect = self.image.get_rect()
        self.speed = 4
        self.rect.left, self.rect.top = random.randint(0, screen_width - self.rect.width), random.randint(0, 60)

    def move(self):
        self.rect.top += self.speed

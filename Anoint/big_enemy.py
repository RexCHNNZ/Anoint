import pygame
import random
from settings import *


class BigEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy3_n1.png")
        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.left, self.rect.top = random.randint(0, screen_width - self.rect.width), random.randint(0, 20)

    def move(self):
            self.rect.top += self.speed

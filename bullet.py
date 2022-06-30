import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
        self.speed = 16

    def move(self):
        self.rect.top -= self.speed

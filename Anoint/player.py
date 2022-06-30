import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/hero1.png")
        self.rect = self.image.get_rect()  # 得到飞机的位置
        self.speed = 5  # 初始化玩家速度
        self.rect.left, self.rect.top = (screen_width - self.rect.width) / 2., (screen_height - self.rect.height)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= screen_height - self.rect.height:
            self.rect.top = screen_height - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= screen_width - self.rect.width:
            self.rect.left = screen_width - self.rect.width
        else:
            self.rect.left += self.speed

    def reset(self):
        self.rect.left, self.rect.top = (screen_width - self.rect.width) / 2., (screen_height - self.rect.height)

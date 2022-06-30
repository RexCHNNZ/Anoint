import pygame
from settings import *
from player import *
from big_enemy import *
from mid_enemy import *
from small_enemy import *
from bullet import *
import sys

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("飞机大战")
pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

bullet_sound = pygame.mixer.Sound("sound/bullet.wav")

background_img = pygame.image.load("image/background.png")
player = Player()
small = pygame.sprite.Group()
mid = pygame.sprite.Group()
big = pygame.sprite.Group()
bullets = pygame.sprite.Group()

delay = 0

while True:
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP]:
        player.moveUp()
    if key_pressed[pygame.K_DOWN]:
        player.moveDown()
    if key_pressed[pygame.K_LEFT]:
        player.moveLeft()
    if key_pressed[pygame.K_RIGHT]:
        player.moveRight()

    screen.blit(player.image, player.rect)
    if delay == 200:
        for i in range(random.randint(0, 3)):
            big.add(BigEnemy())
        delay = 0

    if delay % 50 == 0:
        for i in range(random.randint(0, 5)):
            small.add(MidEnemy())

    if delay % 30 == 0:
        for i in range(random.randint(0, 7)):
            small.add(SmallEnemy())

    if delay % 10 == 0:
        bullet_sound.play()
        bullets.add(Bullet(player.rect.midtop))

    for e in big:
        if e.rect.bottom > screen_height:
            big.remove(e)
        else:
            e.move()
            screen.blit(e.image, e.rect)

    for e in mid:
        if e.rect.bottom > screen_height:
            mid.remove(e)
        else:
            e.move()
            screen.blit(e.image, e.rect)

    for e in small:
        if e.rect.bottom > screen_height:
            small.remove(e)
        else:
            e.move()
            screen.blit(e.image, e.rect)

    for b in bullets:
        if b.rect.top < 0:
            bullets.remove(b)
        else:
            b.move()
            screen.blit(b.image, b.rect)

    pygame.sprite.groupcollide(bullets, small, True, True)
    pygame.sprite.groupcollide(bullets, mid, True, True)
    pygame.sprite.groupcollide(bullets, big, True, True)
    
    if pygame.sprite.spritecollide(player,small,False) or pygame.sprite.spritecollide(player,mid,False) or pygame.sprite.spritecollide(player,big,False):
            player.reset()

    pygame.display.update()
    delay += 1

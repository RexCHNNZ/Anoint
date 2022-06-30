import pygame
import sys
import random
import traceback
import os
from pygame.locals import *
#All constants
screenwidth = 480
screenheight = 700
bg_size = screenwidth, screenheight
color_black = (0,0,0)
color_red = (255,0,0)
color_green = (0,255,0)
color_white = (255,255,255)
global clock
#定义子弹
#普通子弹类
class Bullet1(pygame.sprite.Sprite):
    def __init__(self, rectition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/bullet1.png")
        self.rect = self.image.get_rect()                  
        self.rect.left, self.rect.top = rectition          
        self.speed = 16
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed
    def reset(self, rectition):
        self.rect.left, self.rect.top = rectition
        self.active = True
#超级子弹类        
class Bullet2(pygame.sprite.Sprite):
    def __init__(self, rectition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/bullet2.png")
        self.rect = self.image.get_rect()                  
        self.rect.left, self.rect.top = rectition          
        self.speed = 18
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed
    def reset(self, rectition):
        self.rect.left, self.rect.top = rectition
        self.active = True
#玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("image/hero1.png")
        self.image2 = pygame.image.load("image/hero2.png")
        self.mask = pygame.mask.from_surface(self.image1)# 获取飞机图像的掩膜用以更加精确的碰撞检测
        #飞机坏掉的图片
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("image/hero_blowup_n1.png"),
                                    pygame.image.load("image/hero_blowup_n2.png"),
                                    pygame.image.load("image/hero_blowup_n3.png"),
                                    pygame.image.load("image/hero_blowup_n4.png")])
        self.rect = self.image1.get_rect()#得到飞机的位置
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top= (screenwidth - self.rect.width)/2. ,(screenheight - self.rect.height - 60)
        self.speed = 10#初始化玩家速度
        self.active = True#设置飞机当前的存在属性，True表示飞机正常飞行，False表示飞机已损毁
        self.invincible = False #飞机初始化时有三秒的无敌时间
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed
    def moveDown(self):
        if self.rect.top >= screenheight - self.rect.height:
            self.rect.top = screenheight - self.rect.height
        else:
            self.rect.top += self.speed
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
    def moveRight(self):
        if self.rect.left >= screenwidth - self.rect.width:
            self.rect.left = screenwidth - self.rect.width
        else:
            self.rect.left += self.speed
    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width)/2., (self.height - self.rect.height - 60)
        # 设置飞机当前的存在属性，True表示飞机正常飞行，False表示飞机已损毁
        self.active = True
        self.invincible = True
#敌人类
#小型敌机
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("image/enemy1_down1.png"),
                                    pygame.image.load("image/enemy1_down2.png"),
                                    pygame.image.load("image/enemy1_down3.png"),
                                    pygame.image.load("image/enemy1_down4.png")])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0],bg_size[1]
        self.speed = 4
        self.rect.left,self.rect.top = (random.randint(0, self.width - self.rect.width),random.randint(-5* self.rect.height, -5))
        self.active = True
    #定义敌机的移动函数
    def move(self):
        if self.rect.top >= self.height - 60:
            self.reset()
        else:
            self.rect.top += self.speed
    def reset(self):
        self.rect.left,self.rect.top = (random.randint(0, self.width - self.rect.width),random.randint(-5* self.rect.height, 0))
        self.active = True  
#中型敌机  
class MidEnemy(pygame.sprite.Sprite):
    energy = 5
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("image/enemy2.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("image/enemy2_down1.png"),
                                    pygame.image.load("image/enemy2_down2.png"),
                                    pygame.image.load("image/enemy2_down3.png"),
                                    pygame.image.load("image/enemy2_down4.png")])
        self.image_hit = pygame.image.load("image/enemy2_hit.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0],bg_size[1]
        self.speed = 2
        self.rect.left,self.rect.top = (random.randint(0, self.width - self.rect.width),random.randint(-10* self.rect.height, -self.rect.height))
        self.active = True
        self.energy = MidEnemy.energy
        self.hit = False
    #定义敌机的移动函数
    def move(self):
        if self.rect.top >= self.height - 60:
            self.reset()
        else:
            self.rect.top += self.speed
    def reset(self):
        self.rect.left,self.rect.top = (random.randint(0, self.width - self.rect.width),random.randint(-10* self.rect.height, -self.rect.height))
        self.active = True
        self.energy = MidEnemy.energy
        self.hit = False 
#大型敌机
class BigEnemy(pygame.sprite.Sprite):
    energy = 15
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image1 = pygame.image.load("image/enemy3_n1.png")
        self.image2 = pygame.image.load("image/enemy3_n2.png")
        self.mask = pygame.mask.from_surface(self.image1)
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("image/enemy3_down1.png"),
                                    pygame.image.load("image/enemy3_down2.png"),
                                    pygame.image.load("image/enemy3_down3.png"),
                                    pygame.image.load("image/enemy3_down4.png"),
                                    pygame.image.load("image/enemy3_down5.png"),
                                    pygame.image.load("image/enemy3_down6.png")])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0],bg_size[1]
        self.speed = 2
        self.rect.left,self.rect.top = (random.randint(0, self.width - self.rect.width),random.randint(-15* self.rect.height, -5*self.rect.height))
        self.active = True
        self.energy = BigEnemy.energy
        self.image_hit = pygame.image.load("image/enemy3_hit.png")
        self.hit = False
    #定义敌机的移动函数
    def move(self):
        if self.rect.top >= self.height - 60:
            self.reset()
        else:
            self.rect.top += self.speed
    def reset(self):
        self.rect.left,self.rect.top = (random.randint(0, self.width - self.rect.width),random.randint(-15* self.rect.height, -5*self.rect.height))
        self.active = True
        self.energy = BigEnemy.energy
        self.hit = False
#定义补给包
#超级子弹
class BulletSupply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/ufo1.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = random.randint(0, screenwidth - self.rect.width),-100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        if self.rect.top >= screenheight:        
            self.reset()                         
        else:                                    
            self.rect.top += self.speed
    def reset(self):
        self.active = True
        self.rect.left,self.rect.bottom = random.randint(0, screenwidth - self.rect.width),-100
#超级炸弹    
class BombSupply(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/ufo2.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = random.randint(0, screenwidth - self.rect.width),-100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        if self.rect.top >= screenheight:        
            self.reset()                         
        else:                                    
            self.rect.top += self.speed
    def reset(self):
        self.active = True
        self.rect.left,self.rect.bottom = random.randint(0, screenwidth - self.rect.width),-100
#游戏各类初始化
pygame.init()#初始化
pygame.mixer.init()#混音器初始化
screen = pygame.display.set_mode((bg_size),0,32)#加载窗口
pygame.display.set_caption("飞机大战")#显示标题
score_font = pygame.font.SysFont("arial", 32)#设置分数显示的字体
#载入游戏音乐
#背景音乐
pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.set_volume(0.1)
#子弹声音
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
#boss飞来的声音
big_enemy_flying_sound = pygame.mixer.Sound("sound/big_spaceship_flying.wav")
big_enemy_flying_sound.set_volume(0.4)
#敌人1死掉的声音
enemy1_killed_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_killed_sound.set_volume(0.2)
#敌人2死掉的声音
enemy2_killed_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_killed_sound.set_volume(0.2)
#大boss死掉的声音
enemy3_killed_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_killed_sound.set_volume(0.2)
#自己死掉的声音
me_killed_sound = pygame.mixer.Sound("sound/game_over.wav")
me_killed_sound.set_volume(0.2)
#按钮按下的声音
button_down_sound = pygame.mixer.Sound("sound/button.wav")
button_down_sound.set_volume(0.2)
#升级的声音
level_up_sound = pygame.mixer.Sound("sound/achievement.wav")
level_up_sound.set_volume(0.2)
#爆炸的声音
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
#获得生命的声音
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
#获得子弹的声音
get_bullet_sound = pygame.mixer.Sound("sound/get_double_laser.wav")
get_bullet_sound.set_volume(0.2)
#设置帧率
clock = pygame.time.Clock()
def add_small_enemies(group1,group2,num):# 主要功能：添加小型敌机
    for i in range(num):
        e1 = SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
def add_mid_enemies(group1,group2,num):# 主要功能：添加中型敌机
    for i in range(num):
        e2 = MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)
def add_big_enemies(group1,group2,num):# 主要功能：添加大型敌机
    for i in range(num):
        e3 = BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)
def inc_speed(target, inc):# 主要功能：游戏升级时敌机速度控制
    for each in target:
        each.speed += inc
def showStartScreen():# 主要功能：游戏刚开始的界面显示，响应用户鼠标按键
    delay = 60
    switch_img = False
    running = False
    titleFont = pygame.font.SysFont('arial',28)
    #加载刚开始的图
    begin_image1 = pygame.image.load("image/background.png")
    begin_image2 = pygame.image.load("image/text.png")
    begin_image3 = pygame.image.load("image/button.png")
    begin_loads = []
    begin_loads.extend([pygame.image.load("image/game_loading1.png"),
                        pygame.image.load("image/game_loading2.png"),
                        pygame.image.load("image/game_loading3.png")])
    begin_index = 0
    begin_text = score_font.render("START",True, color_black)
    begin_rect = begin_image3.get_rect()
    begin_rect.left, begin_rect.top = 158,500
    while True:
        screen.fill(0)
        screen.blit(begin_image1,(0,0))
        screen.blit(begin_image2,(120,100))
        screen.blit(begin_image3,(158,500))
        screen.blit(begin_text,(190,504))
        if delay == 0:
            delay = 60
        delay -= 1
        if not (delay % 5):
            screen.blit(begin_loads[begin_index], (147,300))
            begin_index = (begin_index + 1) % 3
            if begin_index == 0:
                screen.blit(begin_loads[begin_index], (147,300))
        #处理游戏退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                button_down_sound.play()
                if event.button == 1 and begin_rect.collidepoint(event.pos):
                    running = True
                    break
        if running == True:
            break
        pygame.display.update()
        clock.tick(60)
    return running
# 主要功能：主循环，响应用户鼠标按键以及键盘事件
def gameBeigin(running):
    clock = pygame.time.Clock()
    background_img = pygame.image.load("image/background.png").convert()#载入背景图
    #载入游戏结束图
    gameover_img = pygame.image.load("image/gameover.png").convert()
    gameover_rect = gameover_img.get_rect()
    #载入重新开始游戏图
    back_to_game_image = pygame.image.load("image/game_again.png").convert_alpha()
    back_to_game_rect = back_to_game_image.get_rect()
    back_to_game_rect.left, back_to_game_rect.top = 90,500
    switch_img = False#控制飞机图片切换（用来模拟喷气
    delay = 60#延时
    #飞机损毁图像索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    player_destroy_index = 0
    player = Player(bg_size)#生成我方飞机
    #初始化分数
    score = 0
    if not os.path.isfile("score_record.txt"):
        f = open("score_record.txt", 'w')
        f.write("26500")
        f.close()
    paused = False#暂停游戏的标志
    #加载暂停相关的按钮
    pause_nor_image = pygame.image.load("image/game_pause_nor.png")
    pause_pressed_image = pygame.image.load("image/game_pause_pressed.png")
    resume_nor_image = pygame.image.load("image/game_resume_nor.png")
    resume_pressed_image = pygame.image.load("image/game_resume_pressed.png")
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = screenwidth - paused_rect.width - 10, 10#设置暂停键的位置
    paused_img = pause_nor_image#设置默认显示的暂停键
    #加载全屏炸弹图标
    bomb_img = pygame.image.load("image/bomb.png")
    bomb_rect = bomb_img.get_rect()
    bomb_font = score_font
    bomb_num = 3 #初始为三个炸弹
    #游戏难度级别
    level = 1
    life_img = pygame.image.load("image/life.png").convert()
    life_rect = life_img.get_rect()
    life_num = 3#一共三条命
    invincible_time = USEREVENT + 2#接触我方飞机无敌时间定时器
    flag_recorded = False#是否已经打开记录文件标志位
    #初始化射击频率
    shoot_frequency = 0
    player_down_index = 16
    #加载普通子弹
    bullet1 = []
    bullet1_index = 0
    #子弹实例化
    bullet1_num = 6
    for i in range(bullet1_num):
        bullet1.append(Bullet1(player.rect.midtop))    
    #加载超级子弹
    #定时器
    double_bullet_timer = USEREVENT + 1
    #标志位
    is_double_bullet = False
    bullet2 = []
    bullet2_index = 0
    #子弹实例化
    bullet2_num = 20
    for i in range(bullet2_num//2):
        bullet2.append(Bullet2((player.rect.centerx - 33, player.rect.centery)))
        bullet2.append(Bullet2((player.rect.centerx + 30, player.rect.centery)))
        bullet2.append(Bullet2((player.rect.centerx, player.rect.top)))
    #实例化敌方飞机
    enemies = pygame.sprite.Group()
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,1)
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,1)
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,1)
    #实例化补给包
    bullet_supply = BulletSupply(bg_size)
    bomb_supply = BombSupply(bg_size)        
    #补给包发放定时器
    supply_timer = USEREVENT
    pygame.time.set_timer(supply_timer, 10 * 1000)
    while running:#游戏开始？
        #显示背景
        screen.fill(0)
        screen.blit(background_img,(0,0))
        #显示分数
        score_text = score_font.render("score: %s" %str(score), True, color_white)
        screen.blit(score_text, (10, 5))
        #定义等级
        if level == 1 and score >3000:
            level = 2
            level_up_sound.play()
            add_small_enemies(small_enemies, enemies, 2)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            inc_speed(small_enemies, 1)
        elif level ==  2 and score > 20000:
            level = 3
            level_up_sound.play()
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 1)
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level ==  3 and score > 80000:
            level = 4
            level_up_sound.play()
            add_small_enemies(small_enemies, enemies, 4)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 1)
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
            inc_speed(big_enemies, 1)
        elif level ==  4 and score > 200000:
            level = 5
            level_up_sound.play()
            add_small_enemies(small_enemies, enemies, 6)
            add_mid_enemies(mid_enemies, enemies, 4)
            add_big_enemies(big_enemies, enemies, 2)
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
            inc_speed(big_enemies, 1)
        level_font = pygame.font.SysFont("arial", 16)
        level_text = level_font.render("level: %s" %str(level), True, color_black)
        screen.blit(level_text,(10,35))
        #处理游戏退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                button_down_sound.play()
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    #如果检测到用户在制定按钮区域按下鼠标左键
                    paused = not paused
                    if paused:
                        paused_img = resume_pressed_image
                        pygame.time.set_timer(supply_timer,0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        paused_img = pause_pressed_image
                        pygame.time.set_timer(supply_timer, 30 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                if life_num == 0:
                    if event.button == 1 and back_to_game_rect.collidepoint(event.pos):
                        gameBeigin(running)
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):#如果鼠标悬停在按钮区域
                    # 如果当前的状态是暂停
                    if paused:
                        paused_img = resume_pressed_image
                    else:
                        paused_img = pause_pressed_image
                else:
                    if paused:
                        paused_img = resume_nor_image
                    else:
                        paused_img = pause_nor_image
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RETURN:
                    gameBeigin(running)
                #按空格炸死全部的敌机
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
            elif event.type == supply_timer:
                if random.choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            elif event.type == double_bullet_timer:
                is_double_bullet = False
                pygame.time.set_timer(double_bullet_timer, 0)
            elif event.type == invincible_time:
                player.invincible = False
                pygame.time.set_timer(invincible_time, 0)
        screen.blit(paused_img, paused_rect)
        if life_num and (not paused):
            #绘制全屏炸弹数和剩余生命数量
            bomb_text = bomb_font.render("x %d" % bomb_num, True, color_black)
            bomb_text_rect = bomb_text.get_rect()
            screen.blit(bomb_img, (10, screenheight - 5 - bomb_rect.height))
            screen.blit(bomb_text,(20 + bomb_rect.width, screenheight - 5 - bomb_text_rect.height))
            if life_num:
                for i in range(life_num):
                    screen.blit(life_img, (screenwidth - i - 10 - (i+1)*life_rect.width, screenheight - 5 - life_rect.height))         
            #检测用户的键盘操作
            # 获得用户所有的键盘输入序列
            key_pressed = pygame.key.get_pressed()
            #如果用户通过键盘发出“向上”的指令,其他类似
            if key_pressed[K_w] or key_pressed[K_UP]:  
                player.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                player.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                player.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                player.moveRight()
            #每十帧发射一颗移动的子弹
            if not (delay % 6):
                bullet_sound.play()
                #如果是普通子弹
                if not is_double_bullet:
                    bullets = bullet1
                    bullets[bullet1_index].reset(player.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % bullet1_num
                #如果是超级子弹
                else:
                    bullets = bullet2
                    bullets[bullet2_index].reset((player.rect.centerx - 33, player.rect.centery))
                    bullets[bullet2_index+1].reset((player.rect.centerx + 30, player.rect.centery))
                    bullets[bullet2_index+2].reset((player.rect.centerx, player.rect.top))
                    bullet2_index = (bullet2_index + 3) % bullet2_num
            #=========绘制补给并检测玩家是否获得=======
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, player):
                    get_bomb_sound.play()
                    if bomb_num < 4:
                        bomb_num += 1
                    bomb_supply.active = False
            
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, player):
                    get_bullet_sound.play()
                    is_double_bullet = True
                    pygame.time.set_timer(double_bullet_timer, 18 * 1000)
                    bullet_supply.active = False
                    
            #=======子弹与敌人碰撞检测==========
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemies_hit = pygame.sprite.spritecollide(b, enemies,False,pygame.sprite.collide_mask)
                    if enemies_hit:
                        b.active = False
                        for e in enemies_hit:
                            if e in big_enemies or e in mid_enemies:
                                e.energy -= 1
                                e.hit = True
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
            #进行我方飞机碰撞检测
            enemies_down = pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask)
            # 如果碰撞检测返回的列表非空，则说明已发生碰撞，若此时我方飞机处于无敌状态
            if enemies_down and not player.invincible:
                player.active = False
                for e in enemies_down:
                    e.active = False#敌机损毁
            #绘制玩家飞机
            if delay == 0:
                delay = 60
            delay -= 1
            if not delay % 3:
                switch_img = not switch_img
            if player.active:
                if switch_img:
                    screen.blit(player.image1, player.rect)
                else:
                    screen.blit(player.image2, player.rect)
            else:
                if not (delay % 3):
                    screen.blit(player.destroy_images[player_destroy_index], player.rect)
                    player_destroy_index = (player_destroy_index + 1) % 4
                    if player_destroy_index == 0:
                        me_killed_sound.play()
                        life_num -= 1
                        player.reset()
                        pygame.time.set_timer(invincible_time, 3*1000)
            #绘制敌机并自动移动
            for each in big_enemies:
                if each.active:
                    each.move()
                    if not each.hit:
                        if switch_img:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                            if each.rect.bottom == -50:
                                big_enemy_flying_sound.play(-1)
                    else:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    #绘制血槽
                    pygame.draw.line(screen,color_black,(each.rect.left,each.rect.top-5),(each.rect.right, each.rect.top-5),4)
                    energy_remain = each.energy/BigEnemy.energy
                    if energy_remain > 0.4:
                        energy_color = color_green
                    else:
                        energy_color = color_red
                    pygame.draw.line(screen,energy_color,(each.rect.left, each.rect.top - 5),(each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),4)
                    if each.rect.bottom == 0:
                        big_enemy_flying_sound.play(-1)
                else:
                    big_enemy_flying_sound.stop()
                    if e3_destroy_index == 0:
                        enemy3_killed_sound.play()
                    if not (delay % 3):
                        screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            score += 3000
                            each.reset()
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if not each.hit:
                        screen.blit(each.image, each.rect)
                    else:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    #绘制血槽
                    pygame.draw.line(screen,color_black,(each.rect.left,each.rect.top - 5),(each.rect.right,each.rect.top-5),2)
                    energy_remain = each.energy/MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = color_green
                    else:
                        energy_color = color_red
                    pygame.draw.line(screen,energy_color,(each.rect.left, each.rect.top - 5), (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), 2)
                
                else:
                    if e2_destroy_index == 0:
                        enemy2_killed_sound.play()
                    if not (delay % 3):
                        screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 1000
                            each.reset()
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if e1_destroy_index == 0:
                        enemy1_killed_sound.play()
                    if not (delay % 3):
                        screen.blit(each.destroy_images[e1_destroy_index],each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 200
                            each.reset()
        elif life_num == 0:
            screen.blit(gameover_img, gameover_rect)
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            pygame.time.set_timer(supply_timer, 0)
            if not flag_recorded:
                flag_recorded = True
                with open("score_record.txt", "r") as f:
                    record_score = int(f.read())
                if score > record_score:
                    with open("score_record.txt", "w") as f:
                        f.write(str(score))
            record_score_text = score_font.render("%d" % record_score, True, color_black)
            screen.blit(record_score_text,(150, 29))
            game_over_score_text = score_font.render("%d" % score, True, color_black)
            screen.blit(game_over_score_text,(200,305))
            screen.blit(back_to_game_image,(90,500))
        pygame.display.update()#更新屏幕
        clock.tick(60)#控制游戏最大帧率
# 主要功能：主函数
# if __name__ == "__main__":
try:
    while True:
        #显示起始画面
        running = showStartScreen()
        pygame.mixer.music.play(-1)
        gameBeigin(running)
except SystemExit:
    pass
except:
    traceback.print_exc()
    pygame.quit()
    input()
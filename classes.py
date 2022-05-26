import random
import pygame
import os
from config import *

class drone(pygame.sprite.Sprite):
    def __init__(self, groups):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(img_dir, 'playerShip1_orange.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (drone_width, drone_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0

class Objeto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, 'obj.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (obj_width, obj_height))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, width - obj_width)
        self.rect.x = random.randrange(-100, -obj_height)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height or self.rect.right < 0 or self.rect.left > width:
            self.rect.y = random.randint(0, width - obj_width)
            self.rect.x = random.randint(-100, -obj_height)
            self.speedy = random.randint(-3, 3)
            self.speedx = random.randint(2, 9)

class pegar(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        anim = []
        for i in range(9):
            arq = os.path.join(img_dir, 'exp{}.png'.format(i))
            img = pygame.image.load(arq).convert()
            img = pygame.transform.scale(img, (32, 32))
            anim.append(img)
        self.anim = anim
        self.frame = 0 
        self.image = self.anim[self.frame]  
        self.rect = self.image.get_rect()
        self.rect.center = center  

        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
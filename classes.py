import random
import pygame
import os
from config import *

class drone(pygame.sprite.Sprite):
    def __init__(self, groups):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(img_dir, 'player.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (drone_width, drone_height))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = width - 10
        self.rect.bottom = height / 2
        self.speedx = 0
        self.speedy = 0
        self.groups = groups

    def update(self, score):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
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
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, width - obj_width)
        self.rect.x = random.randrange(-150, -obj_height)
        self.speedx = random.randrange(-6, 6)
        self.speedy = random.randrange(4, 18)
        self.restrito = [4, -3, -2, -1, 0, 1, 2, 3, 4]

    def update(self, tempo):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height or self.rect.right < 0 or self.rect.left > width or self.speedx in self.restrito or self.speedy in self.restrito:
            self.rect.y = random.randint(0, width - obj_width)
            self.rect.x = random.randint(-150, -obj_height)
            self.speedy = random.randint(-4 - round(tempo / 10), 4 + round(tempo / 10))
            self.speedx = random.randint(4 - round(tempo / 10), 12 + round(tempo / 10))
        while self.speedx in self.restrito or self.speedy in self.restrito:
            self.speedy = random.randint(-4 - round(tempo / 10), 4 + round(tempo / 10))
            self.speedx = random.randint(4 - round(tempo / 10), 12 + round(tempo / 10))

class Caixa(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        anim = []
        for i in range(16):
            arq = os.path.join(img_dir, 'frame_0{}.png'.format(i))
            img = pygame.image.load(arq).convert()
            img = pygame.transform.scale(img, (caixa_width, caixa_height))
            anim.append(img)
        self.anim = anim
        self.frame = 0 
        self.image = self.anim[self.frame]  
        self.rect = self.image.get_rect()
        self.rect.center = center  

        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.rect.y = random.randrange(0, width - obj_width)
        self.rect.x = random.randrange(-200, -obj_height)
        self.speedx = random.randrange(-6, 6)
        self.speedy = random.randrange(4, 18)

    def update(self, score):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height or self.rect.right < 0 or self.rect.left > width:
            self.rect.y = random.randint(0, width - obj_width)
            self.rect.x = random.randint(-200, -obj_height)
            self.speedy = random.randint(-6, 6)
            self.speedx = random.randint(4, 18)

class explodir(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        anim = []
        for i in range(9):
            arq = os.path.join(img_dir, 'exp0{}.png'.format(i))
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

    def update(self, score):
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

class Background():
      def __init__(self, tela):
            self.bgimage = pygame.image.load(os.path.join(img_dir, 'bg3.png')).convert_alpha()
            self.bgimage = pygame.transform.scale(self.bgimage, (width, height))
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = 0
            self.bgX2 = self.rectBGimg.width
 
            self.moving_speed = 5
         
      def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
             
      def render(self, tela):
         tela.blit(self.bgimage, (self.bgX1, self.bgY1))
         tela.blit(self.bgimage, (self.bgX2, self.bgY2))
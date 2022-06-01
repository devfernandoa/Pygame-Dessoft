import random
import pygame
import os
from config import *

class drone(pygame.sprite.Sprite):
    '''Classe que gera o objeto drone (jogador)

    Classe do tipo Sprite que representa o drone, suas variaveis e sua movimentação, tratando as inputs geradas pelo jogador
    '''
    
    def __init__(self, groups):
        pygame.sprite.Sprite.__init__(self)

        # Declara as diferentes posições do drone
        self.image1 = pygame.image.load(os.path.join(img_dir, 'drone_1.png')).convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (drone_width, drone_height))
        self.image2 = pygame.image.load(os.path.join(img_dir, 'drone_2.png')).convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (drone_width, drone_height))
        self.image3 = pygame.image.load(os.path.join(img_dir, 'drone_3.png')).convert_alpha()
        self.image3 = pygame.transform.scale(self.image3, (drone_width, drone_height))
        self.image4 = pygame.image.load(os.path.join(img_dir, 'drone_4.png')).convert_alpha()
        self.image4 = pygame.transform.scale(self.image4, (drone_width, drone_height))

        self.image = self.image1


        self.rect = self.image.get_rect()
        self.rect.centerx = width - 10
        self.rect.bottom = height / 2
        self.speedx = 0
        self.speedy = 0
        self.groups = groups

    def update(self, score):
        '''Atualiza a posição e velocidade do drone'''
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
        
        if self.speedx == 0 and self.speedy == 0:
            self.image = self.image1
        elif self.speedx > 0:
            self.image = self.image3
        elif self.speedx < 0:
            self.image = self.image4
        elif self.speedy > 0:
            self.image = self.image2

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
    '''Classe que gera o objeto 

    Classe do tipo Sprite que representa o objeto que o jogador tem que desviar e suas variaveis. 
    '''

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
        '''Atualiza a posição do objeto'''
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
    '''Classe que gera a Caixa 

    Classe do tipo Sprite que representa o objeto que o jogador tem que pegar e suas variaveis. Trata também de fazer a animação da caixa girando
    '''

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
        '''Atualiza a animação e posição da caixa'''
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

class Estrela(pygame.sprite.Sprite):
    '''Classe que gera o powerup Estrela 

    Classe do tipo Sprite que representa o powerup que deixará o jogador invencível. Trata também de fazer a animação da estrela girando
    '''

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        anim = []
        for i in range(16):
            arq = os.path.join(img_dir, 'estrela0{}.png'.format(i))
            img = pygame.image.load(arq).convert()
            img = pygame.transform.scale(img, (obj_width, obj_height))
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
        '''Atualiza a animação e posição da estrela'''
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
    '''Classe que gera a explosão

    Classe do tipo Sprite que representa a explosão que aparece quando o jogador é atingido por um objeto.
    '''

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
        '''Atualiza a animação da explosão'''
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
    ''' Classe que gera o fundo do jogo
    
    Classe que gera o fundo do jogo, como uma imagem de fundo que rola ao longo do tempo, e que é atualizada a cada frame.
    '''

    def __init__(self, tela):
        self.bgimage = pygame.image.load(os.path.join(img_dir, 'skyline.png')).convert_alpha()
        self.bgimage = pygame.transform.scale(self.bgimage, (width, height))
        self.rectBGimg = self.bgimage.get_rect()
 
        self.bgY1 = 0
        self.bgX1 = 0
 
        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width
 
        self.moving_speed = 5
         
        self.background = 1 
    def update(self, power):
        '''Atualiza a imagem de fundo'''

        if power == False and self.background != 1:
            self.background = 1
            self.bgimage = pygame.image.load(os.path.join(img_dir, 'skyline.png')).convert_alpha()
            self.bgimage = pygame.transform.scale(self.bgimage, (width, height))
            self.rectBGimg = self.bgimage.get_rect()
        elif power == True and self.background != 2:
            self.background = 2
            self.bgimage = pygame.image.load(os.path.join(img_dir, 'skyline-power.png')).convert_alpha()
            self.bgimage = pygame.transform.scale(self.bgimage, (width, height))
            self.rectBGimg = self.bgimage.get_rect()

        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
    def render(self, tela):
        '''Função que renderiza o fundo do jogo a cada frame'''
        tela.blit(self.bgimage, (self.bgX1, self.bgY1))
        tela.blit(self.bgimage, (self.bgX2, self.bgY2))
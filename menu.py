import pygame
import random
from os import path
from config import *

def menu(tela):
    clock = pygame.time.Clock()

    # Carrega o fundo do menu
    background = pygame.image.load(path.join(img_dir, "menu.jpg")).convert()
    background_rect = background.get_rect()

    #Sons pra quando a gente tiver musicas
    '''
    # Carrega os sons do menu
    pygame.mixer.music.load(path.join(sound_dir, "menu.ogg"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    '''

    condicao = True
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = Quit
                condicao = False
            if event.type == pygame.KEYUP:
                estado = Jogo
                condicao = False

        tela.fill(black)
        tela.blit(background, background_rect)
        pygame.display.flip()

    return estado 
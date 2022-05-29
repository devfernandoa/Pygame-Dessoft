import pygame
import random
from os import path
from config import *

def end(tela, score):
    clock = pygame.time.Clock()

    # Carrega o fundo do menu
    background = pygame.image.load(path.join(img_dir, "menu2.png")).convert()
    background_rect = background.get_rect()
    font = pygame.font.Font(path.join(font_dir, 'PressStart2P.ttf'), 40)
    texto = font.render("Fim de jogo", True, (255, 255, 255))
    texto2 = font.render("Aperte 'r' para jogar de novo", True, (255, 255, 255))

    #Sons pra quando a gente tiver musicas
    '''
    # Carrega os sons do menu
    pygame.mixer.music.load(path.join(sound_dir, "menu.ogg"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    '''

    condicao = True
    while condicao:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = Quit
                condicao = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    state = Quit
                    condicao = False
                elif event.key == pygame.K_r:
                    state = Jogo
                    condicao = False
                
        tela.fill(black)
        tela.blit(background, background_rect)
        tela.blit(texto, (width/2 - texto.get_width()/2, 60 - texto.get_height()/2))
        tela.blit(texto2, (width/2 - texto2.get_width()/2, 60 + texto.get_height()/2))
        pygame.display.flip()
    return state
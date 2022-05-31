import pygame
import random
from os import path
from config import *

def menu(tela):
    clock = pygame.time.Clock()

    # Carrega o fundo do menu
    background = pygame.image.load(path.join(img_dir, "menu2.png")).convert()
    background_rect = background.get_rect()
    font = pygame.font.Font(path.join(font_dir, 'PressStart2P.ttf'), 40)
    texto = font.render("Pressione qualquer", True, (255, 255, 255))
    texto2 = font.render("tecla para jogar", True, (255, 255, 255))
    texto3 = font.render("Use as setinhas para se mover,", True, (255, 255, 255))
    texto4 = font.render("desvie de pedras", True, (255, 255, 255))
    texto5 = font.render("e pegue caixas!", True, (255, 255, 255))

    #Sons pra quando a gente tiver musicas
    '''
    # Carrega os sons do menu
    pygame.mixer.music.load(path.join(sound_dir, "menu.ogg"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    '''

    condicao = True

    # Loop menu
    while condicao:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = Quit
                condicao = False
            if event.type == pygame.KEYUP:
                state = Jogo
                condicao = False

        tela.fill(black)
        tela.blit(background, background_rect)
        tela.blit(texto, (width/2 - texto.get_width()/2, height/4 - texto.get_height()/2))
        tela.blit(texto2, (width/2 - texto2.get_width()/2, height/4 + texto.get_height()/2))
        tela.blit(texto3, (width/2 - texto3.get_width()/2, height/2 - texto3.get_height()/2))
        tela.blit(texto4, (width/2 - texto4.get_width()/2, height/2 + texto4.get_height()/2))
        tela.blit(texto5, (width/2 - texto5.get_width()/2, height/2 + texto5.get_height()/2 + texto4.get_height()))
        pygame.display.flip()

    return state
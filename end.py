import pygame
import random
from os import path
from config import *
import json

def end(tela):
    clock = pygame.time.Clock()

    # Carrega o fundo do menu
    background = pygame.image.load(path.join(img_dir, "menu2.png")).convert()
    background_rect = background.get_rect()
    font = pygame.font.Font(path.join(font_dir, 'PressStart2P.ttf'), 40)
    texto = font.render("Fim de jogo", True, (255, 255, 255))
    texto2 = font.render("Aperte 'r' para jogar de novo", True, (255, 255, 255))

    # Abre e carrega os dados do arquivo
    hs_arquivo = open('hs.json', 'r')
    hs_dados = json.load(hs_arquivo)
    hs_arquivo.close()

    # Inicializa variaveis para o highscore
    score1 = 0
    score2 = 0
    score3 = 0
    user1 = ''
    user2 = ''
    user3 = ''

    # Loops para salvar os dados do highscore (precisa de mais de um loop para funcionar)
    for nome, valor in hs_dados.items():
        if valor > score1:
            score1 = valor
            user1 = nome
    for nome, valor in hs_dados.items():
        if valor > score2 and user1 != nome:
            score2 = valor
            user2 = nome
    for nome, valor in hs_dados.items():
        if valor > score3 and user1 != nome and user2 != nome:
            score3 = valor
            user3 = nome

    # Inicializa os textos formatados com os valores do highscore
    texto_score1 = font.render("Highscore: {} - > {}".format(user1, score1), True, (255, 255, 255))
    texto_score2 = font.render("Highscore: {} - > {}".format(user2, score2), True, (255, 255, 255))
    texto_score3 = font.render("Highscore: {} - > {}".format(user3, score3), True, (255, 255, 255))

    #Sons pra quando a gente tiver musicas
    '''
    # Carrega os sons do menu
    pygame.mixer.music.load(path.join(sound_dir, "menu.ogg"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    ''' 

    # Loop menu
    condicao = True
    while condicao:
        clock.tick(fps)

        # Fadeout da musica do jogo
        pygame.mixer.music.fadeout(5000)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = Quit
                condicao = False
            if event.type == pygame.KEYUP:
                # Se a tecla for 'r' reinicia o jogo e se for 'escape' sai do jogo
                if event.key == pygame.K_ESCAPE:
                    state = Quit
                    condicao = False
                elif event.key == pygame.K_r:
                    state = Jogo
                    condicao = False
                

        # Desenha fundo e textos
        tela.fill(black)
        tela.blit(background, background_rect)
        tela.blit(texto, (width/2 - texto.get_width()/2, 150 - texto.get_height()/2))
        tela.blit(texto2, (width/2 - texto2.get_width()/2, 150 + texto.get_height()/2))
        tela.blit(texto_score1, (width/2 - texto2.get_width()/2, 480 + texto.get_height()))
        tela.blit(texto_score2, (width/2 - texto2.get_width()/2, 480 + texto.get_height()*2))
        tela.blit(texto_score3, (width/2 - texto2.get_width()/2, 480 + texto.get_height()*3))
        pygame.display.flip()
    return state
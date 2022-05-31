import pygame
import random
from os import path
from config import *
import json

def hs(tela, score):
    font = pygame.font.Font(path.join(font_dir, 'PressStart2P.ttf'), 28)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(width / 2 - 100, height / 2, 140, 32)
    background = pygame.image.load(path.join(img_dir, "menu2.png")).convert()
    background_rect = background.get_rect()
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    texto = font.render("Digite seu nome", True, (255, 255, 255))
    texto_gameover = font.render("GAME OVER", True, (255, 255, 255))
    texto_highscore = font.render("Score -> {}".format(score), True, (255, 255, 255))


    state = Highscore

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = Quit
                condicao = False
            if event.type == pygame.QUIT:
                state = Quit
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # Código para salvar o nome e o score do jogador
                        hs_arquivo = open('hs.json', 'r')
                        hs_dados = json.load(hs_arquivo)
                        hs_arquivo.close()
                        if text not in hs_dados.keys():
                            hs_dados[text] = score
                        else:
                            if score > hs_dados[text]:
                                hs_dados[text] = score
                        hs_arquivo = open('hs.json', 'w')
                        json.dump(hs_dados, hs_arquivo)
                        hs_arquivo.close()
                        done = True
                        state = End

                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        tela.fill(black)
        tela.blit(background, background_rect)

        txt_surface = font.render(text, True, color)

        width_text = max(200, txt_surface.get_width()+10)
        input_box.w = width_text

        tela.blit(txt_surface, (input_box.x+5, input_box.y+5))
        tela.blit(texto, (width/2 - texto.get_width()/2, height/2 - texto.get_height()- 50))
        tela.blit(texto_gameover, (width/2 - texto_gameover.get_width()/2, height/3 - texto_gameover.get_height()/2))
        tela.blit(texto_highscore, (width/2 - texto_highscore.get_width()/2, height/3 + texto_highscore.get_height()* 1.5))

        pygame.draw.rect(tela, color, input_box, 2)

        pygame.display.flip()
        clock.tick(fps)
    return state
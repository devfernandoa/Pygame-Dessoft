import pygame
import random
from os import path
from config import *
import json

def hs(tela, score):
    font = pygame.font.Font(path.join(font_dir, 'PressStart2P.ttf'), 28)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(width / 2 - 50, height / 2, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    state = Highscore

    while not done:
        for event in pygame.event.get():
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
                        if text not in hs_dados:
                            hs_dados[text] = score
                        else:
                            if hs_dados[text] < score:
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

        tela.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width_text = max(200, txt_surface.get_width()+10)
        input_box.w = width_text
        # Blit the text.
        tela.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(tela, color, input_box, 2)

        pygame.display.flip()
        clock.tick(fps)
    return state
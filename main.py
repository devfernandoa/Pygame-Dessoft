import pygame
import random
import time
from config import *
from menu import *
from jogo import *
from highscore import *
from end import *

# Inicializa o pygame
pygame.init()
pygame.mixer.init()

# Inicializa a tela
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("SynthRace")

state = Menu

# Loop para diferentes telas
while state != Quit:
    if state == Menu:
        state = menu(tela)
    elif state == Jogo:
        state, score = jogo(tela)
    elif state == Highscore:
        time.sleep(1)
        state = hs(tela, score)
    elif state == End:
        state = end(tela)
    else:
        state = Quit

pygame.quit()
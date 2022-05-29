import pygame
import random
import time
from config import *
from menu import *
from jogo import *
from highscore import *
from end import *

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("SynthRace")

state = Menu
while state != Quit:
    if state == Menu:
        state = menu(tela)
    elif state == Jogo:
        state, score = jogo(tela)
    elif state == Highscore:
        state = hs(tela, score)
    elif state == End:
        state = end(tela)
    else:
        state = Quit

pygame.quit()
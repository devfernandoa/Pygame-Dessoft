import pygame
import random
from config import *
from menu import *
from jogo import *

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("SynthRace")

state = Menu
while state != Quit:
    if state == Menu:
        state = menu(tela)
    elif state == Jogo:
        state = jogo(tela)
    else:
        state = Quit

pygame.quit() 
import pygame
import time
from classes import *
from config import *

def jogo(tela):
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    sprites = pygame.sprite.Group()
    objetos = pygame.sprite.Group()
    grupos = {}
    grupos['sprites'] = sprites
    grupos['objetos'] = objetos

    bg = Background(tela)
    player = drone(grupos)
    sprites.add(player)

    for i in range(8):
        objeto = Objeto()
        objetos.add(objeto)
        sprites.add(objeto)

    quit = 0
    jogando = 1
    pegando = 2
    state = jogando

    teclas = {}
    score = 0

    '''
    # Carrega os sons do jogo
    pygame.mixer.music.load(path.join(sound_dir, "jogo.ogg"))
    pygame.mixer.music.play(-1)
    '''

    while state != quit:
        clock.tick(fps)

        bg.update()
        bg.render(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = quit
            if state == jogando:
                if event.type == pygame.KEYDOWN:

                    teclas[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8

                if event.type == pygame.KEYUP:

                    if event.key in teclas and teclas[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8
        sprites.update()

        if state == jogando:
            score += 1 / 60
            hits = pygame.sprite.spritecollide(player, objetos, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # som
                 # pegar.play()
                player.kill()
                pegando = pegar(player.rect.center)
                sprites.add(pegando)
                state = quit
                keys_down = {}
                pegando_tick = pygame.time.get_ticks()
                duracao = pegando.frame_rate * len(pegando.anim) + 400
        elif state == pegando:
            now = pygame.time.get_ticks()
            if now - pegando_tick > duracao:
                state = jogando
                player = drone(grupos)
                sprites.add(player)
        
        # Desenhando meteoros
        sprites.draw(tela)

        # Desenhando o score
        text_surface = pygame.font.Font(os.path.join(font_dir, 'PressStart2P.ttf'), 28).render("{:08d}".format(round(score)), True, yellow)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (width / 2,  10)
        tela.blit(text_surface, text_rect)

        pygame.display.update()
                
        
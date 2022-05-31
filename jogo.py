import pygame
import time
from classes import *
from config import *

def jogo(tela):
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    sprites = pygame.sprite.Group()
    objetos = pygame.sprite.Group()
    caixas = pygame.sprite.Group()
    estrelas = pygame.sprite.Group()
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
    explodindo = 2
    highscore = 3
    state = jogando

    teclas = {}
    score = 0

    tempo = 0
    tpower = 0
    power = False

    '''
    # Carrega os sons do jogo
    pygame.mixer.music.load(path.join(sound_dir, "jogo.ogg"))
    pygame.mixer.music.play(-1)
    '''

    while state != 0 or state != 3:
        clock.tick(fps)

        # Gerar uma caixa aleatoriamente
        if random.randrange(0, 120) == 69 and len(caixas) < 1:
            caixa = Caixa(player.rect.center)
            caixas.add(caixa)
            sprites.add(caixa)

        # Gera uma estrela aleatoriamente
        if random.randrange(0, 1200) == 420 and len(estrelas) < 2 and power == False:
            estrela = Estrela(player.rect.center)
            estrelas.add(estrela)
            sprites.add(estrela)

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
        sprites.update(tempo)

        if state == jogando:
            tempo += 1 / 60
            hits = pygame.sprite.spritecollide(player, objetos, True, pygame.sprite.collide_mask)
            ponto = pygame.sprite.spritecollide(player, caixas, True, pygame.sprite.collide_mask)
            powerup = pygame.sprite.spritecollide(player, estrelas, True, pygame.sprite.collide_mask)
            if len(hits) > 0 and power == False:
                # som
                 # pegar.play()
                player.kill()
                state = highscore
                keys_down = {}
                explodindo = explodir(player.rect.center)
                sprites.add(explodindo)
                explodindo_tick = pygame.time.get_ticks()
                duracao = explodindo.frame_rate * len(explodindo.anim) + 400
            elif len(ponto) > 0:
                # som
                # pegar.play()
                score += 1
                caixa.kill()
            elif len(powerup) > 0:
                # som
                # powerup.play()
                power = True
                estrela.kill()
            if power:
                tpower += 1/60
                if tpower > 4:
                    power = False
                    tpower = 0
                tela.fill(black)
        elif state == explodindo:
            now = pygame.time.get_ticks()
            if now - explodindo_tick > duracao:
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
        if state == 3:
            break
    return state, score
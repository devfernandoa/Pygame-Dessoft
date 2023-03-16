import pygame
import time
from classes import *
from config import *


def jogo(tela):
    clock = pygame.time.Clock()

    som_powerup = pygame.mixer.Sound(path.join(sound_dir, "powerup.wav"))

    # Inicializa grupos
    sprites = pygame.sprite.Group()
    objetos = pygame.sprite.Group()
    caixas = pygame.sprite.Group()
    estrelas = pygame.sprite.Group()
    grupos = {}
    grupos['sprites'] = sprites
    grupos['objetos'] = objetos
    grupos['caixas'] = caixas
    grupos['estrelas'] = estrelas

    # Inicializa objetos
    bg = Background(tela)
    player = drone(grupos)
    sprites.add(player)

    for i in range(8):
        objeto = Pedra()
        objetos.add(objeto)
        sprites.add(objeto)

    # Inicializa variaveis
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

    # Carrega os sons do jogo
    pygame.mixer.music.load(path.join(sound_dir, "jogo.mp3"))
    pygame.mixer.music.play(loops=-1)

    # Loop do jogo
    while state != 0 or state != 3:
        clock.tick(fps)

        # Gerar uma caixa aleatoriamente
        if random.randrange(0, 120) == 69 and len(caixas) < 1:
            caixa = Caixa(player.rect.center)
            caixas.add(caixa)
            sprites.add(caixa)

        # Gera uma estrela aleatoriamente
        if random.randrange(0, 1500) == 420 and len(estrelas) < 2 and power == False:
            estrela = Estrela(player.rect.center)
            estrelas.add(estrela)
            sprites.add(estrela)

        # Atualizar o fundo
        bg.update(power)
        bg.render(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = quit
                pygame.quit()
                break
            if state == jogando:
                if event.type == pygame.KEYDOWN:
                    teclas[event.key] = True
                    # Movimenta o drone
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8

                if event.type == pygame.KEYUP:

                    if event.key in teclas and teclas[event.key]:
                        # Volta a velocidade do drone para 0 ao soltar a tecla
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8
        sprites.update(tempo)

        if state == jogando:
            # Conta o tempo (60 frames por segundo)
            tempo += 1 / 60

            # Verifica se o colisões
            hits = pygame.sprite.spritecollide(
                player, objetos, True, pygame.sprite.collide_mask)
            ponto = pygame.sprite.spritecollide(
                player, caixas, True, pygame.sprite.collide_mask)
            powerup = pygame.sprite.spritecollide(
                player, estrelas, True, pygame.sprite.collide_mask)

            # Verifica se o player colidiu com algum objeto e roda a animação de explosão
            if len(hits) > 0 and power == False:
                # som
                # pegar.play()
                player.kill()
                state = highscore
                explodindo = explodir(player.rect.center)
                sprites.add(explodindo)
                explodindo_tick = pygame.time.get_ticks()
                duracao = explodindo.frame_rate * len(explodindo.anim) + 400

            # Verifica se o player colidiu com uma caixa e adiciona um ponto ou dois
            elif len(ponto) > 0:
                # Verifica se o poder está ativo
                if power:
                    score += 2
                else:
                    score += 1
                caixa.kill()

            # Verifica se durante o powerup o player colidiu com um objeto e adiciona um ponto
            elif len(hits) > 0 and power == True:
                score += 1
                # Chance aleatória de ao destruir uma pedra 2 virem no lugar
                if random.randrange(0, 5) != 1:
                    objeto = Pedra()
                    objetos.add(objeto)
                    sprites.add(objeto)
                else:
                    for i in range(2):
                        objeto = Pedra()
                        objetos.add(objeto)
                        sprites.add(objeto)

            # Verifica se o player colidiu com uma estrela e ativa o powerup
            elif len(powerup) > 0:
                # som
                # powerup.play()
                power = True
                estrela.kill()

            # Conta a duração do powerup
            if power:
                if tpower == 0:
                    som_powerup.play()
                tpower += 1/60
                if tpower > powerup_duracao:
                    power = False
                    tpower = 0

        elif state == explodindo:
            now = pygame.time.get_ticks()
            if now - explodindo_tick > duracao:
                state = jogando
                player = drone(grupos)
                sprites.add(player)

        # Desenhando meteoros
        sprites.draw(tela)

        # Desenhando o score
        text_surface = pygame.font.Font(os.path.join(font_dir, 'PressStart2P.ttf'), 28).render(
            "{:08d}".format(round(score)), True, yellow)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (width / 2,  10)
        tela.blit(text_surface, text_rect)

        pygame.display.update()
        if state == 3:
            break
    return state, score

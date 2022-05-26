import pygame
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

    player = drone(grupos)
    sprites.add(player)

    for i in range(8):
        objeto = Objeto()
        objetos.add(objeto)
        sprites.add(objeto)

    quit = 0
    jogando = 1
    pegando = 2
    estado = jogando

    teclas = {}
    score = 0

    '''
    # Carrega os sons do jogo
    pygame.mixer.music.load(path.join(sound_dir, "jogo.ogg"))
    pygame.mixer.music.play(-1)
    '''

    while estado != quit:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.quitUIT:
                estado = quit
            if estado == jogando:
                if event.type == pygame.KEYDOWN:

                    teclas[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_SPACE:
                        player.shoot()

                if event.type == pygame.KEYUP:

                    if event.key in teclas and teclas[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8
        sprites.update()

        if estado == jogando:
            score += 1
            hits = pygame.sprite.spritecollide(player, objetos, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                pickup.play()
                player.kill()
                pickup = pegar(player.rect.center)
                sprites.add(pegando)
                estado = quit
                keys_down = {}
                pegando_tick = pygame.time.get_ticks()
                duracao = pickup.frame_ticks * len(pickup.explosion_anim) + 400
        elif estado == pegando:
            now = pygame.time.get_ticks()
            if now - pegando_tick > duracao:
                estado = jogando
                player = drone(grupos)
                sprites.add(player)

        # ----- Gera saídas
        tela.fill(black)  # Preenche com a cor branca
        tela.blit(pygame.image.load(os.path.join(img_dir, 'starfield.png')).convert(), (0, 0))
        # Desenhando meteoros
        sprites.draw(tela)

        # Desenhando o score
        text_surface = pygame.font.Font(os.path.join(font_dir, 'PressStart2P.ttf'), 28).render("{:08d}".format(score), True, yellow)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (width / 2,  10)
        tela.blit(text_surface, text_rect)
from os import path

# Caminhos de diretorios
img_dir = path.join(path.dirname(__file__), 'assets', 'img')
sound_dir = path.join(path.dirname(__file__), 'assets', 'sound')
font_dir = path.join(path.dirname(__file__), 'assets', 'font')

# Tela
width = 1200
height = 960

# Frames por segundo
fps = 60

# Dados dos objetos
obj_width = 100
obj_height = 76
caixa_width = 192
caixa_height = 108
drone_width = 150
drone_height = 150

powerup_duracao = 4

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Estados
Menu = 0
Jogo = 1
Quit = 2
Highscore = 3
End = 4

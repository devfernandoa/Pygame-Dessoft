from os import path

# Caminhos de diretorios
img_dir = path.join(path.dirname(__file__), 'assets', 'img')
sound_dir = path.join(path.dirname(__file__), 'assets', 'sound')
font_dir = path.join(path.dirname(__file__), 'assets', 'font')

# Tela
width = 600
height = 480

# Frames por segundo
fps = 60 

# Dados dos objetos
obj_width = 50
obj_height = 38
drone_width = 50
drone_height = 38

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
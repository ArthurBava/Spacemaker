import pygame
import sys
from tkinter import simpledialog
from pygame.locals import *

# Inicializar o Pygame
pygame.init()

# Definir configurações básicas
tamanho = (1000, 563)
branco = (255, 255, 255)  # Corrigido para a cor branca correta
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
fundo = pygame.image.load("assets/bg.jpg")
icone = pygame.image.load("assets/space.png")
sound = pygame.mixer.Sound("assets/spacesound.mp3")
pygame.mixer.Sound.play(sound)
pygame.display.set_caption("SpaceMarker")
pygame.display.set_icon(icone)

# Lista para armazenar os pontos das estrelas
pontos = []
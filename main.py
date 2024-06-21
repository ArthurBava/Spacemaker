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

def jogar():
    global pontos

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 23)
    input_text = ""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_RETURN:
                    print("Informação digitada:", input_text)
                    input_text = ""
                elif event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                print("Clique do mouse na posição:", event.pos)
                nome_stars = simpledialog.askstring("Estrela", "Qual o nome da estrela?")
                if not nome_stars:
                    nome_stars = "Desconhecido"
                cord_mouse = event.pos
                dados = {
                    "nome_stars": nome_stars,
                    "cord_mouse": cord_mouse
                }
                pontos.append(dados)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_F10]:
            try:
                with open('dados_space', 'w') as arquivo:
                    for dados in pontos:
                        arquivo.write(f"{dados}\n")
                print("Estrelas salvas com sucesso!")
            except:
                print("Erro ao salvar as estrelas!")
        if keys[pygame.K_F11]:
            try:
                with open('dados_space', 'r') as arquivo:
                    pontos = [eval(dados) for dados in arquivo.readlines()]
                print("Estrelas carregadas com sucesso!")
            except:
                print("Erro ao carregar as estrelas!")
        if keys[pygame.K_F12]:
            try:
                with open('dados_space', 'w') as arquivo:
                    pass
                pontos = []
                print("Estrelas deletadas com sucesso!")
            except:
                print("Erro ao deletar as estrelas!")
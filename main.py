import pygame
import sys
from tkinter import simpledialog
from pygame.locals import *

# Inicializar o Pygame
pygame.init()


tamanho = (1000, 563)
branco = (255, 255, 255)  
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
        
        
        tela.blit(fundo, (0, 0))
        text_surface = font.render("Pressione F10 para Salvar os Pontos", True, branco)
        tela.blit(text_surface, (20, 10))
        text_surface = font.render("Pressione F11 para Carregar os Pontos", True, branco)
        tela.blit(text_surface, (20, 30))
        text_surface = font.render("Pressione F12 para Deletar os Pontos", True, branco)
        tela.blit(text_surface, (20, 50))

        for star in pontos:
            pygame.draw.circle(tela, branco, star['cord_mouse'], 5)
            text_surface = font.render(f"{star['nome_stars']} {str(star['cord_mouse'])}", True, branco)
            tela.blit(text_surface, (star['cord_mouse'][0], star['cord_mouse'][1] - 20))
        
        if len(pontos) > 1:
            l_temp = [p["cord_mouse"] for p in pontos]
            pygame.draw.lines(tela, branco, False, l_temp)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    jogar()
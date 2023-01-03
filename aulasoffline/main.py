#inicia a biblioteca pygame
import pygame

# tamanho da tela width = largura e height = altura em pixels
#cores de forma fácil
WIDTH = 800
HEIGHT = 600
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#inicia a biblioteca gerando a tela
pygame.init()
#comando para controlar os parametros width e height
#surface é a tela da janela criada

surface = pygame.display.set_mode((WIDTH, HEIGHT))
#desenho com comando draw epecificções abaixo
#Onde desenhar/Cor/
pygame.draw.rect(surface, AMARELO, pygame.Rect(30, 30, 60, 60))
pygame.draw.rect(surface, VERMELHO, pygame.Rect(90, 90, 160, 160))
pygame.draw.rect(surface, AZUL, pygame.Rect(400, 400, 120, 120))
#comando que atualiza a tela para criar fps
pygame.display.flip()

#Mantém  o jogo aberto
running = True
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

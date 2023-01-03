#inicia a biblioteca pygame
import pygame


# tamanho da tela width = largura e height = altura em pixels
WIDTH = 800
HEIGHT = 600


#inicia a biblioteca gerando a tela
pygame.init()
#comando para controlar os parametros width e height
tela = pygame.display.set_mode((WIDTH, HEIGHT))


#parametro que controla a pemanecia da janela criada
running = True
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    #Esta função é usada para atualizar o conteúdo de toda a superfície de exibição da tela.
    pygame.display.flip():


#desenhar na tela recem criada

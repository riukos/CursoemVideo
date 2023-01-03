import pygame
from pygame.locals import *
from sys import exit
from pygame import sprite

pygame.init()

#tela
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('BATALHA')

#load images
#background images
background_img = pygame.image.load()

run = True
while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

pygame.quit()






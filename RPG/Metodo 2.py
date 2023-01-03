import pygame
from pygame.locals import *
from sys import exit
from pygame.sprite import Sprite

pygame.init()

largura = 960
altura = 600


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('sprites')


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/attack_1.png'))
        self.sprites.append(pygame.image.load('sprites/attack_2.png'))
        self.sprites.append(pygame.image.load('sprites/attack_3.png'))
        self.sprites.append(pygame.image.load('sprites/attack_4.png'))
        self.sprites.append(pygame.image.load('sprites/attack_5.png'))
        self.sprites.append(pygame.image.load('sprites/attack_6.png'))
        self.sprites.append(pygame.image.load('sprites/attack_7.png'))
        self.sprites.append(pygame.image.load('sprites/attack_8.png'))
        self.sprites.append(pygame.image.load('sprites/attack_9.png'))
        self.sprites.append(pygame.image.load('sprites/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        self.animar = False


toda_as_sprites = pygame.sprite.Group()
sapo = Sapo()
toda_as_sprites.add(sapo)


def atacar(self):
    self.animar = True


def update(self):
    self.atual = self.atual + 1
    self.image = self.sprites[self.atual]
    if self.atual >= len(self.sprites):
        self.atual = 0


while True:
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    toda_as_sprites.draw(tela)
    toda_as_sprites.update()
    pygame.display.update()

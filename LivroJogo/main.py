import pygame

# p = parede
# <space> = espaço
mapa = [
    "ppppppppppppppppppppppppppppppppppppppppppppp",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "p                                                                            p",
    "pppppppppppppppppppppppppppppppppppppppp",
]
# Configurações mapa de fundo
AMARELO = (0xFF, 0xFF, 0x00)
PRETO = (0x00, 0x00, 0x00)
TELA_WIDTH = 800
TELA_HEIGHT = 600
# tamanho dos pixels 20, 30
BLK_WIDTH = TELA_WIDTH / 40
BLK_HEIGHT = TELA_HEIGHT / 20

pygame.init()
tela = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))

# controle de x,y no mapa
for id_linha, linha in enumerate(mapa):
    for id_coluna, caracter in enumerate(linha):
        cor = PRETO
        if caracter == "P":
            cor = AMARELO
        x = id_coluna * BLK_WIDTH
        y = id_linha * BLK_HEIGHT
        r = pygame.rect((x, y), (BLK_WIDTH, BLK_HEIGHT))
        pygame.draw.rect(tela, cor, r, 0)
pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()



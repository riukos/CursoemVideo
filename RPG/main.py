#Rpg usando C4 que precisa de apenas d6 nos lances
import pygame
import random
import sys,time

if __ name__ == "__main__":
    print('Funciona!')
#Função para digitalização lenta dos textos
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./60)


#Função que simula o dado de 6 faces
d6 = random.randint(1,6)


#Função para parametros de formatação de textos
def hist(dsc):
    print('*' *50)
    print(dsc)
    print('*' *50)


sprint(hist('Ola seja bem vindo a Allgord Terra de dragões e Magos'))



#sprint('Olá aventureiro, seja bem vindo a Allgord\n'
       #'Reino de dragões e magos\n'
       #'Tragédias e glórias\n')





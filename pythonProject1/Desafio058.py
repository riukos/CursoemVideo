import random
from time import sleep
num1 = 0
teste = 1
cont = 0
while teste != num1:
    num1 = int(input('Digite um numero de 0 a 10: '))
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    teste = random.choice(num)
    print('Processando...')
    sleep(0.5)
    if teste == num1:
        print('Você é muito bom, eu escolhei o numero: {} e você acertou com {} tentativas!'.format(teste, cont))
    else:
        print('Eu escolhi o numero: {} e você errou, tente outra vez.'.format(teste))
        cont = cont +1


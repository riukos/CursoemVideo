import random
from time import sleep
num1 = int(input('Digite um numero de 0 a 5: '))
num = [1,2,3,4,5]
teste = random.choice(num)
print('Processando...')
sleep(2)
if teste == num1:
    print('Você é muito bom, eu escolhei o numero:{} e você acertou!'.format(teste))
else:
    print('Eu escolhi o numero: {} e você errou, tente outra vez.'.format(teste))
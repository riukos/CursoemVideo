from random import choice
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
jogador = str(input('Digite entre pedra, papel ou tesoura: '))
if jogador == pc:
    print('Aconteceu um empate! ambos escolheram {}.'.format(pc))
elif jogador == lista[0] and pc == lista[1]:
    print('Voce escolheu {} e o computador escolheu {} computador venceu! '.format(jogador,pc))
elif jogador == lista[0] and pc == lista[2]:
    print('Voce escolheu {} e o computador escolheu {}  jogador venceu.'.format(jogador, pc))
elif jogador == lista[1] and pc == lista[0]:
    print('Voce escolheu {} e o computador escolheu {} jogador venceu! '.format(jogador, pc))
elif jogador == lista[1] and pc == lista[2]:
    print('Voce escolheu {} e o computador escolheu {} computador venceu.'.format(jogador, pc))
elif jogador == lista[2] and pc == lista[0]:
    print('Voce escolheu {} e o computador escolheu {} computador venceu.'.format(jogador, pc))
elif jogador == lista[2] and pc == lista[1]:
    print('Voce escolheu {} e o computador escolheu {} jogador venceu! '.format(jogador, pc))
else:
    print('escolha entre pedra papel ou tesoura!')
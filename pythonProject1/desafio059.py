menu = 0
somar = 1
multiplicar = 2
maior = 3
novo = 4
sair = 5
while menu != 5:
    v1 = int(input('Digite o Primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair
    ''')
    menu = int(input('Digite o numero desejado no menu: '))
    if menu == somar:
        total = v1 + v2
        print('Você escolheu somar e o resultado é: {}'.format(total))
        break
    if menu == multiplicar:
        total = v1 * v2
        print('Você escolheu multiplicar e o seu resultado é: {}.'.format(total))
        break
    if menu == maior:
        if v1 > v2:
            print('Você escolheu maior e o maior valor é: {}'.format(v1))
        else:
            print('Voce escolheu maior e o Maior valor é: {}'.format(v2))
        break
    if menu == novo:
        v1 = int(input('Digite o Primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
        print('''
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos numeros
            [5] sair''')
        menu = int(input('Digite o numero desejado no menu: '))
    if menu == sair:
        break
    else:
        print('Digite uma opção valida!')

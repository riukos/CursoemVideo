import random
w = 0
while True:
    print('-=' * 10)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('-=' * 10)
    n = int(input('Digite um valor: '))
    r = ' '
    while r not in 'PpIi':
        r = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    p = random.randint(0, 11)
    teste = p + n
    p1 = 0
    if r == 'P':
        if teste % 2 == 0:
            print('Você venceu! ')
            w += 1
        else:
            print('Você perdeu!!')
            break
    elif r == 'I':
        if teste % 2 == 1:
            print('Você venceu!! ')
            v += 1
        else:
            print('Você perdeu!! ')
            break
    print('vamos jogar novamente!')
print(f'O jogo acabou! você ganhou {w} vezes!')


'''while True:
        print(f' Você escolheu o numero {n} e {r} e o computador escolheu o numero {p} e {p1}')
        if l >= 1:
            break
        elif teste % 2 == 0 and r == 'P':
            w += 1
            print(f'Você ganhou {w} vezes, vamos de novo!! ')
            break
        elif teste % 2 == 0 and r == 'I':
            l += 1
            print(f'Acabou!! você ganhou {w} vezes')
            break
        elif teste % 2 == 0 and p1 == 'P':
            l += 1
            print(f'Acabou!! você ganhou {w} vezes')
            break
        elif teste % 2 == 0 and p1 == 'I':
            w += 1
            print(f'Você ganhou {w} vezes, vamos de novo!! ')
            break
        elif teste % 2 != 0 and p1 == 'I':
            l += 1
            print(f'Acabou!! você ganhou {w} vezes')
            break
        elif teste % 2 != 0 and r == 'I':
            w += 1
            print(f'Você ganhou {w} vezes, vamos de novo!! ')
            break
    if l >= 1:
        break
'''


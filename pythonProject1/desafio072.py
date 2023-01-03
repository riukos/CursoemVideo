num = ('Zero', 'Um', 'Doiz', 'Trez', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez,', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
resp = 'S'
while True:
    if resp in 'Ss':
        while True:
            num1 = int(input('Digite um numero de 0 a 20 para ver por extenso: '))
            if 0 <= num1 <= 20:
                break
            print('Digite um numero valido!!', end=' ')
        print(f'Seu numero por extenso é: {num[num1]}')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    elif resp == 'Nn':
        break
    else:
        print('Digite uma resposta valida')
        resp = 'Ss'


'''s = 'S'
n = 'N'
num = 0
maior = 0
menor = 0
cont = 0
media = 0
total = 0
cond = 'S'
while cond == s:
    if cond == s and cond != n:
        if cond == s:
            num = int(input('Digite um numero inteiro: '))
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
            else:
                menor = num
            cont += 1
            media += num
            total = media / cont
            print('O maior numero é: {} o menor numero é {} a media é: {}'.format(maior, menor, total))
            cond = str(input('Deseja continuar? [S/N] ')).upper()
        else:
            print('Digite uma opção valida')'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar?  [S/N]  '))
media = soma / quant
print('A quantiade de numeros digitado é: {} e sua media é: {}'.format(soma, media))
print('O maior valor digitado é: {} e o menor é: {}'.format(maior, menor))

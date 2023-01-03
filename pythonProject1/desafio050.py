s = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        s = s + n
        cont += 1
print('Você digitou {} valores PARES e a soma dos numeros pares é: {}'.format(cont, s))
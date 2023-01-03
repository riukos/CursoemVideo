from random import randint
numeros = []
n = 0

def sorteia():
    for n in range(1, 6):
        n = randint(0, 10)
        print(f'O numero sorteado é: {n}')
        numeros.append(n)

def somapar(list):
    soma = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma += numeros[i]
    print(f'A soma dos numeros pares é: {soma}')


sorteia()
print(numeros)
somapar(numeros)


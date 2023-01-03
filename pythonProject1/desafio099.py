def maior(*num):
    quant = len(num)
    print(f'Analizando {quant} numeros!')
    maior = 0
    for i in range(len(num)):
        if num[i] > 0:
            maior = num[i]
        if num[i] > maior:
            maior = num[i]
    print(maior)
maior(10, 2, 3, 5, 11)
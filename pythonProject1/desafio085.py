num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite um numero: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort(reverse=True)
num[1].sort(reverse=True)
print(num)
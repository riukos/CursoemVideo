lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
a = (2, 5, 4)
b = lanche + a
for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} ')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print(sorted(lanche))
print(b)
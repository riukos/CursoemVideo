valorc = float(input('Digite o valor da casa que deseja comprar: '))
salario = float(input('Qual o salario do comprador: '))
tempo = float(input('Em quantos anos planeja pagar a casa: '))
tempot = tempo * 12
condi30 = (salario / 100) * 30
parcela = valorc / tempot
if condi30 <= parcela:
    print('Seu emprestimo foi negado! sua parcela ficou : {} e é mais que 30% do seu salario'.format(parcela))
else:
    print('Seu emprestimo foi aprovado e o valor da sua parcela é R${}'.format(parcela))
print(tempot, condi30, parcela)
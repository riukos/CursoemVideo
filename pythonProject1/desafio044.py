preco = float(input('Digite o valor do seu pedido: '))
condpag = str(input('''Escolha entre as formas de pagamento:'
                dinheiro
                cartao
                xcartao2
                xmais3:''')).strip()
cond = [  'dinheiro',
                 'cartao',
                 'xcartao2',
                 'xmais3']
if condpag == cond[0]:
    print('Seu produto tera 10% de desconto e custara: {:.2f}'.format(preco - ((preco / 100)*10)))
elif condpag == cond[1]:
    print("Seu produce tera 5% de desconto e custara: {:.2f}".format(preco - ((preco / 100) * 5)))
elif condpag == cond[2]:
    print('Seu produto tera o preco normal!')
elif condpag == cond[3]:
    print('Seu produto tera 20% de juros e custara {:.2f}'.format((preco + ((preco / 100)*20))))
else:
    print("Digite uma forma de pagamento valida!")
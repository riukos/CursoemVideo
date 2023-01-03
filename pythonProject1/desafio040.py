nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua media é: {:.1f} e você está REPROVADO'.format(media))
elif media >= 5 and media < 6.9:
    print('Sua media é: {:.1f} e você está em RECUPERAÇÃO'.format(media))
else:
    print('Sua media é: {:.1f} e você está APROVADO'.format(media))

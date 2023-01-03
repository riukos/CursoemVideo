times = ('Palmeiras', ' Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'America-MG', 'Fortaleza', 'Botafogo', 'Santos', 'Goiás', 'São Paulo', 'Bragantino', 'Coritiba', 'Ceará SC', 'Cuiabá', 'Avai', 'Atlético-GO', 'Juventude')
print(f'Os 5 primeiros colocados são {times[:5]}')
print(f'Os 4 ultimos são {times[-4:]}')
print(sorted(times))
for cont in range(0, len(times)):
    if times[cont] == 'Corinthians':
        cont += 1
        print(f'Corinthians esta na {cont}ª posição.')
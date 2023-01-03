def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado
    :param show:  (opicional) Mostrar ou não o calculo.
    :return: O valor fatorial do numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}  ', end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f


#programa princial
print(fatorial(5, True))
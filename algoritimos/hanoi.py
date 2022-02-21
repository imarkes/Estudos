def hanoi(n: int, orig: str, aux: str, dest: str) -> str:
    """
    Ordena as peças de acordo com a origem e destino
    :param n: 1
    :param orig: 'A'
    :param aux: 'B'
    :param dest: 'C'
    :return:A->B:1
            A->C:2
            B->C:1 ...
    """
    if n >= 1:
        hanoi(n - 1, orig, dest, aux)
        print(f'{orig}->{dest}:{n}')
        hanoi(n - 1, aux, orig, dest)


for i in range(1, 4):
    print(' ****** Algoritimos %s ' % i)
    hanoi(i, 'A', 'B', 'C')

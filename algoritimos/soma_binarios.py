from collections import deque
from itertools import zip_longest


def soma_bin(n: str, n2: str) -> str:
    """
    Soma dois numeros binarios.
    :param n: '000011101010'
    :param n2: '01010101010111'
    :return: '1011001000001'
    """
    n = int(n, 2)
    n2 = int(n2, 2)
    return format(n + n2, 'b')


# print('exemplo 1: -> ', soma_bin('000011101010', '01010101010111'))


def soma_reversa(s):
    """Reverte a ordenação do parametros"""
    return map(int, reversed(s))


def soma_bin2(n: str, n2: str) -> str:
    """
    Soma dois numeros binarios e retorna seu inverso.
    :param n: '000011101010'
    :param n2: '01010101010111'
    :return: 01011001000001
    """
    n = soma_reversa(n)
    n2 = soma_reversa(n2)
    digito = 0
    result = deque()
    for d, d2, in zip_longest(n, n2, fillvalue=0):
        sum_digito = digito + d + d2
        digito = 0 if sum_digito < 2 else 1
        result.appendleft(str(sum_digito % 2))
    if sum_digito == 1:
        result.appendleft('1')
    return ''.join(result)


# print('exemplo 2: -> ', soma_bin2('000011101010', '01010101010111'))


def soma_reversa_lista(s: str) -> list:
    """Retira o ultimo elemento da lista"""
    result = []
    s = list(s)
    while s:
        result.append(int(s.pop()))
    return result


def zip_longo(n: str, n2: str, nulo):
    """

    :param n: '000011101010'
    :param n2: '01010101010111'
    :param nulo:
    :return:[('0', '0'), ('1', '0'), ('n', 'n')]
    """
    n = list(n)
    n2 = list(n2)
    menor, maior = sorted([n, n2], key=len)
    faltante = len(maior) - len(menor)
    menor.extend([nulo] * faltante)
    result = []
    for i, d in enumerate(maior):
        result.append((d, menor[i]))
    return result


# print(zip_longo('000011101010', '01010101010111', 0))


def soma_bin3(n: str, n2: str) -> str:
    """
    Soma numeros binarios e reverte seu valor.
    :param n: '000011101010'
    :param n2: '01010101010111'
    :return: 01011001000001
    """
    n = soma_reversa(n)
    n2 = soma_reversa(n2)
    digito = 0
    result = deque()
    for d, d2, in zip_longo(n, n2, nulo=0):
        sum_digito = digito + d + d2
        digito = 0 if sum_digito < 2 else 1
        result.appendleft(str(sum_digito % 2))
    if sum_digito == 1:
        result.appendleft('1')
    return ''.join(result)

# print('exemplo 3: -> ', soma_bin2('000011101010', '01010101010111'))

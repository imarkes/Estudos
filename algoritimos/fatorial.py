

def fatoria(n):
    """
    Calcula o fatorial de um numero
    :param n: int
    :return: int
    """
    if n < 0:
        return 0
    i = fat = 1
    while i <= n:
        fat = fat * i
        i += 1
    return fat


# print(fatoria(5))


def fatorial_recursivo(n):
    """
    Calcula o fatorial de forma recursiva.
    :param n: int
    :return: int
    """
    if n < 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

# print(fatorial_recursivo(5))
import bisect

lista = [0, 10, 20, 30, 40, 50, 60, 70]


def busca_binaria(lista: list, posicao: int) -> int:
    """
    Busca a posição de um elemento na lista.
    :param lista: [0, 10, 20, 30, 40, 50, 60, 70]
    :param posicao: 20
    :return: index posição
    """
    esqueda, direita = 0, len(lista) - 1

    while esqueda <= direita:
        meio = (esqueda + direita) // 2
        elemento = lista[meio]
        if elemento == posicao:
            return meio
        elif elemento > posicao:

            direita = meio - 1
        else:

            esqueda = meio + 1
    return None


# print(busca_binaria(lista, 20))


def busca_binaria_bisect(lista: list, item: int) -> int:
    """
    Efetua busca binaria utilizando função bisct
    :param lista: [0, 10, 20, 30, 40, 50, 60, 70]
    :param item: 30
    :return: 3
    """
    i = bisect.bisect_left(lista, item)
    return i if i < len(lista) and lista[i] == item else None


# print(busca_binaria_bisect(lista, 30))


def busca_sequencial(lista: list, numero: int) -> int:
    """
    Executa a busca sequencial em uma lista e retorna o index
    :param lista:[0, 10, 20, 30, 40, 50, 60, 70]
    :param numero: 10
    :return: 2
    """
    for pos in range(len(lista)):
        if lista[pos] == numero:
            print(f'O numero: {numero}, está na posição: {pos}')
            return True
    return False


# print(busca_sequencial(lista, 10))


def busca_binaria_recursiva(lista: list, elemento: int, min=0, max=None):
    """
    Executa a busca binaria de forma recursiva e retorna o index procurado.
    :param lista: [0, 10, 20, 30, 40, 50, 60, 70]
    :param elemento:
    :param min: int
    :param max: int
    :return: int
    """
    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max - min) // 2

    if lista[meio] > elemento:
        return busca_binaria_recursiva(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria_recursiva(lista, elemento, meio + 1, max)
    else:
        return meio


# print(busca_binaria_recursiva([0, 10, 20, 30, 40, 50, 60, 70], 50))


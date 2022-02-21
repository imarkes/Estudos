def mediana_de_duas_listas(a: list, b: list) -> float:
    """
    >>> mediana_de_duas_listas([1], [])
    1
    >>> mediana_de_duas_listas([1], [2])
    1.5
    >>> mediana_de_duas_listas([1], [2,3000])
    2

    :param a:
    :param b:
    :return:
    """
    lista_concatenada = a + b
    return calcula_mediana_ordenada(lista_concatenada)


def calcula_mediana_ordenada(lista: list) -> float:
    """
    >>> calcula_mediana_ordenada([1])
    1
    >>> calcula_mediana_ordenada([1,2])
    1.5
    >>> calcula_mediana_ordenada([1,3000, 2, 3])
    2.5

    :param lista:
    :return:
    """
    lista.sort()
    return mediana(lista)


def mediana(lista):
    tamanho = len(lista)
    meio_lista = tamanho // 2
    if tamanho % 2 == 1:
        return lista[meio_lista]
    return (lista[meio_lista] + lista[meio_lista] - 1) / 2


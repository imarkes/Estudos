''' Remoção de elementos repetidos '''
lista = ['jaca', 'jaca', 'jaca', 'café', 'café', 'abacate']


def remove_duplicados(lsta: list) ->dict:
    """
    Remove palavras duplicadas de um array
    :param lsta:['jaca', 'jaca', 'jaca', 'café', 'café', 'abacate']
    :return:{'café', 'jaca', 'abacate'}
    """
    return set(lsta)


print('Exemplo 1: -> ', remove_duplicados(lista))


def remove_duplicados_em_tempo_linear(lst):
    result = []
    repetidos = set()

    for item in lst:
        if item not in repetidos:
            result.append(item)
            repetidos.add(item)
    return result


print('Exemplo 2: -> ', remove_duplicados_em_tempo_linear(lista))

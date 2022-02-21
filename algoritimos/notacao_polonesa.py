""" Dado a lista de operação ['2','1','+','3','*'],['4','13','5','/','+'] resolva em notação polonesa reversa."""
import operator

from tests.calcula_mediana_listas import calcula_mediana_ordenada


def notacao_polonesa_reversa(expressao: list[str]) -> int:
    """
    >>> notacao_polonesa_reversa(['2','1','+','3','*'])
    9
    >>> notacao_polonesa_reversa(['4','13','5','/','+'])
    6

    """

    global res
    pilha = []
    for elemento in expressao:
        try:
            elementos = int(elemento)
            pilha.append(elementos)

        except ValueError:
            sinal = elemento
            elemento_2 = pilha.pop()
            elemento_1 = pilha.pop()

            if sinal == '+':
                res = elemento_1 + elemento_2
            elif sinal == '-':
                res = elemento_1 - elemento_2
            elif sinal == '*':
                res = elemento_1 * elemento_2
            elif sinal == '/':
                res = elemento_1 // elemento_2

            pilha.append(res)

    return pilha.pop()


def notacao_polonesa_reversa_exemplo_2(expressao: list[str]) -> int:
    """
    >>> notacao_polonesa_reversa_exemplo_2(['2','1','+','3','*'])
    9
    >>> notacao_polonesa_reversa_exemplo_2(['4','13','5','/','+'])
    6

    """
    sinal_operacao = {'+': operator.add,
                      '-': operator.sub,
                      '*': operator.mul,
                      '/': operator.floordiv}

    pilha = []
    for elemento in expressao:
        try:
            elementos = int(elemento)
            pilha.append(elementos)

        except ValueError:
            sinal = elemento
            elemento_2 = pilha.pop()
            elemento_1 = pilha.pop()

            operacao = sinal_operacao[sinal]
            res = operacao(elemento_1, elemento_2)

            pilha.append(res)

    return pilha.pop()




"""Dado o conjunto de palavras ['hit', 'dot', 'dog', 'lot', 'log'] a partir da frase inicial ('hit') transforme
na frase final ('cog') alterando apenas uma letra e retorne o seu tamenho."""


def transformando_palavras(inicio: str, final: str, conjunto: set) -> int:
    """
    >>> transformando_palavras('dog','cog', {'hit', 'dot', 'dog', 'lot', 'log'})
    2

    # >>> transformando_palavras('dot','cog', {'hit', 'dot', 'dog', 'lot', 'log'})
    # 3
    """
    palavra_atual = inicio
    tamanho_menor_caminho = 2

    if mudou_apenas_uma_letra(palavra_atual, final):
        return tamanho_menor_caminho


def mudou_apenas_uma_letra(palavra_atual, final):
    return sum(1 for a, b in zip(palavra_atual, final) if a != b) == 1

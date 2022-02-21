from collections import Counter


def cria_matriz(num_lin: int, num_col: int, valor: int) -> list[list]:
    """
    Cria uma lista de matrizes
    :param num_lin: 2
    :param num_col: 6
    :param valor: 8
    :return: [[8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8]]
    """
    matriz = []
    for i in range(num_lin):
        linha = []
        for j in range(num_col):
            linha.append(valor)
        matriz.append(linha)
    return matriz


# print(cria_matriz(2, 6, 8))


def soma_matriz(a: list, b: list) -> list[list]:
    """
    Soma duas matrizes
    :param a: [[1, 2, 3], [5, 6, 7]]
    :param b: [[8, 9, 10], [1, 2, 3]]
    :return: [[9, 11, 13], [6, 8, 10]]
    """
    num_lin = len(a)
    num_col = len(a[0])
    C = cria_matriz(num_lin, num_col, 0)

    for lin in range(num_lin):
        for col in range(num_col):
            C[lin][col] = a[lin][col] + b[lin][col]
    return C


A = [[1, 2, 3], [5, 6, 7]]
B = [[8, 9, 10], [1, 2, 3]]


# print(soma_matriz(A, B))


def multiplica_matrizes(A: list, B: list) -> list[list]:
    """
    Multiplica matrizes
    :param A: [[1, 2, 3], [5, 6, 7]]
    :param B: [[8, 9], [2, 3], [5, 5]]
    :return: [[27, 30], [87, 98]]
    """
    num_lin_A, num_col_A = len(A), len(A[0])
    num_lin_B, num_col_B = len(B), len(B[0])
    assert num_col_A == num_lin_B

    C = []
    for linha in range(num_lin_A):
        # Começa uma nova linha
        C.append([])
        for coluna in range(num_col_B):
            # Adiciona uma nova coluna na linha
            C[linha].append(0)
            for k in range(num_col_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C


A = [[1, 2, 3], [5, 6, 7]]
B = [[8, 9], [2, 3], [5, 5]]


# print(multiplica_matrizes(A, B))


def soma_array(numeros: list, alvo: int) -> list:
    """
    Recebe uma lista de inteiros e retorna a soma alvo.
    :param numeros: [3, 5, -4, 8, 11, 1, -1, 6]
    :param alvo: 10
    :return: [-1, 11]
    """
    alvo = alvo
    for pos in numeros:
        for p in numeros:
            if pos + (p) == alvo and pos != p:
                print([pos, p])


# soma_array([3, 5, -4, 8, 11, 1, -1, 6], 10)

def organiza_lista(blacks: list, orange: list) -> list:
    """
    Ordena pares de listas
    :param blacks: [150, 179, 149, 152, 154]
    :param orange: [162, 181, 151, 160, 170]
    :return: [[149, 150, 152, 179], [151, 160, 162, 181]]
    """
    if len(blacks) % 2 == 1 and len(orange) % 2 == 1:
        alunos = blacks[:-1], orange[:-1]

        if sum(alunos[0]) <= sum(alunos[1]):
            blacks = sorted(alunos[0])
            orange = sorted(alunos[1])
            print(True)
            print([blacks, orange])
        else:
            print(False)
    else:
        print(False)


organiza_lista([150, 179, 149, 152, 154], [162, 181, 151, 160, 170])


def conta_letras(letras: str) -> str:
    """
    Conta a quantidade de letras na string
    :param letras: 'BBBBBBBBBBBBBAACCCDD'
    :return: 9B4B2A3C2D
    """
    lets = dict(Counter(letras))
    dicionario = ''
    for k, total in lets.items():

        if total > 9:
            dicionario += f'9{k}'
            dicionario += f'{total - 9}' + f'{k}'
        else:
            dicionario += f'{total}' + f'{k}'

    print(dicionario)

# conta_letras('BBBBBBBBBBBBBAACCCDD')

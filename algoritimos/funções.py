import operator

produtos = []


def cadastra_itens(desc: str, valor: float, quantidade: int) -> list[dict]:
    """
    Cadastra itens.
    :param desc: Produto 1
    :param valor: 20
    :param quantidade: 4
    :return: {'produto1': [20, 4, 80]}
    """
    desc = desc
    valor = valor
    quantidade = quantidade
    total = valor * quantidade
    produtos.append({desc: [valor, quantidade, total]})
    return produtos


def escolhe_imposto(opcao: int) -> int:
    """
    Calcula o imposto de acordo com a opção.
    :param opcao: ICMS
    :return: 12.0
    """
    total = 10
    impostos = {
        0: 'ISENTO',
        1: 'ICMS',
        2: 'IPI'}
    if opcao == 1:
        total += total * 0.2
        print(total)
    elif opcao == 2:
        total += total * 0.5
        print(total)
    else:
        total = total
        print(total)
    return impostos[opcao]


# imp = escolhe_imposto(1)
# print(imp)
# prod = cadastra_itens('item', 20, 4)
# prod = cadastra_itens('item', 30, 42)
# prod = cadastra_itens('item', 40, 14)
# prod = cadastra_itens('item', 25, 43)
# print(prod)


produtos_2 = [('caneta', 5.0), ('celular', 800), ('violão', 300)]


# Aplicando o listcomprerension
# print([nome for nome, valor in produtos_2])


def filtrando_valor(kwargs):
    """
    Retorna nome e valor de acordo com filtro aplicado.
    :param kwargs: [('caneta', 5.0), ('celular', 800), ('violão', 300)]
    :return:[('celular', 800)]
    """
    _, valor = kwargs
    return valor > 300


# print(list(filter(filtrando_valor, produtos_2)))


def extrai_nome(arg):
    """
    Mapeia os argumentos de acordo com o filtro passado.
    :param arg:
    :return:
    """
    nome, _ = arg
    return nome


print(list(map(extrai_nome, produtos_2)))

print(list(map(extrai_nome, filter(filtrando_valor, produtos_2))))

print(list(map(operator.itemgetter(0), filter(filtrando_valor, produtos_2))))

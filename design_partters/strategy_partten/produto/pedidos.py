from collections import namedtuple
from decimal import Decimal


class Item:
    """Cria o objeto itens do pedido."""

    def __init__(self, descricao: str, preco: float, quantidade: int) -> None:
        self.preco = preco
        self.quantidade = quantidade
        self.descricao = descricao

    def total(self) -> float:
        """Calcula o total do pedido"""
        return self.preco * self.quantidade


class Pedido:
    """Cria o objeto Pedido."""

    def __init__(self):
        self._itens = []

    def adicionar(self, *item):
        """Adiciona os itens a lista de pedidos"""
        self._itens.extend(item)

    def total(self):
        return sum(item.total() for item in self._itens)

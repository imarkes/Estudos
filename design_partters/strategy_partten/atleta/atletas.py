from interfaces import Ihabilidade
from typing import Type


class Atleta:
    """ A classe Atleta se torna gernerica e todos seus atributos e metodos será passado a uma interface"""

    def __init__(self, habilidade: Type[Ihabilidade]):
        '''

        :param habilidade:
        '''
        self.habilidade = habilidade

    def acao(self):
        self.habilidade.comportamento()

    def atributos(self):
        self.habilidade.nivel_atributo()


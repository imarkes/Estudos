from abc import ABC, abstractmethod


class Ihabilidade(ABC):
    """
        A classe Ihabilidade se torna um molde abstrato,
         forçando a quaisquer outro atleta a ter seus metodos/atributos.
    """

    @abstractmethod
    def comportamento(self):
        pass

    @abstractmethod
    def nivel_atributo(self):
        pass

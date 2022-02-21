class Jogar:
    """Cria o objeto Jogar."""

    def acao(self):
        print('Estou jogando')


class Programar:
    """Cria o objeto Programar"""

    def acao(self):
        print('Estou programando')


class Pessoa:
    """Cria o objeto Pessoa."""

    def __init__(self, comportamento):
        self.comportamento = comportamento

    def realizar_acao(self):
        """Define a ação que o objeto irá realizar de acordo com o comportamento."""
        self.comportamento.acao()


pessoa1 = Pessoa(Jogar())  # Jogar é a dependencia
pessoa1.realizar_acao()

pessoa2 = Pessoa(Programar())  # Programar é a dependencia
pessoa2.realizar_acao()

''' 
    Considerado o factoring ou fabrica.
    Através de uma unica classe pessoa podemos ter diversos comportamentos/ação 
    A injeção de dependência é semelhante a uma fabrica.

'''

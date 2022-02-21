from interfaces import Ihabilidade


class CorrerRapido(Ihabilidade):
    """
        O Corredor obrigatoriamente herda os metodos e atributos da interface.
    """

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        """Define o comportamento do atleta."""
        print('Correndo a 60km/h')

    def nivel_atributo(self):
        """Define o nilve de atividade do atleta."""
        print(f'Nivel de corrida: {self.nivel}')

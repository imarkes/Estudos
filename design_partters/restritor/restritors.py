class Cao:
    """Cria o Objeto Cao."""

    def __init__(self, nome: str, raca: str, sexo: str) -> str:
        self._sexo = sexo  # Atributo privado
        self.raca = raca
        self.nome = nome


class EmbrulhoRestritor:
    """Proteje os atributos da classe Cao"""

    def __init__(self, protegido):
        self._protegido = protegido

    def __getattr__(self, att):
        if att.startswith('_'):  # se o atributo começar com _
            raise AttributeError(f'Atributo Protegido: {att}')
        return getattr(self._protegido, att)


if __name__ == '__main__':
    rex = Cao('Rex', 'vira lata', 'macho')
    print(rex.nome, rex.raca, rex._sexo)

    rex_restrito = EmbrulhoRestritor(rex)
    print(rex_restrito.nome)
    print(rex_restrito._sexo) # Não é possivel acessar o atributo.

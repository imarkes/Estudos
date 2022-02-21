class _Telefone:
    """Objeto Telefone"""

    def telefonar(self, ddd: str, numero: str) -> str:
        """Executa uma ligação."""
        print(f'Ligando para ({ddd}) {numero}')


class _WhatsApi:
    """Objeto WhatApp"""

    def ligar(self, zap: str) -> str:
        """Liga para um numero Whats"""
        print(f'Ligar pelo whats para o numero: {zap}')


class WhatsTelefoneAdapter:
    """Adaptador para o telefone ou Whats, se necessario apenas troca-lo"""

    def __init__(self, whats_api):
        self._whats_api = whats_api

    def telefonar(self, ddd, numero):
        """Efetua uma ligação."""
        return self._whats_api.ligar(f'{ddd}{numero}')


telefone = WhatsTelefoneAdapter(_WhatsApi())


# Ex-2
class _TelegramApi:
    """Objeto Telegram"""

    def call(self, telefone: str, pais: str) -> str:
        """Liga pelo telegram"""
        print(f'{telefone} no pais: {pais}')


class TelegramTelefoneAdapter(_TelegramApi):
    """Adaptador criado, se necessário apenas troca-lo."""

    def telefonar(self, ddd, telefone, pais):
        """Efetua uma ligação."""
        self.call(f' ligando pelo telegram {ddd} {telefone}', pais=pais)


telefone1 = TelegramTelefoneAdapter()

if __name__ == '__main__':
    telefone.telefonar('73', '123456789')
    telefone1.telefonar('77', '987654321', 'argentina')

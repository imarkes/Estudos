from abc import ABC, abstractmethod
from typing import Dict


class InterfaceDB(ABC):
    """ Os Objetos que vir desta interface terá que implementar o metodo select_one"""

    @abstractmethod
    def select_one(self):
        pass


class SqLiteRepositorio(InterfaceDB):
    def select_one(self) -> Dict:
        return {
            'Success': True,
            'Mensagem': 'Funcionando'
        }

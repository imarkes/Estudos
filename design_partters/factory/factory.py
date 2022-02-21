from design_partters.factory.cases import UseCase
from design_partters.factory.databases import SqLiteRepositorio


class SqLiteFactoring:

    @staticmethod
    def create() -> UseCase:
        return UseCase(SqLiteRepositorio())

    '''
        EM CASO DE ALTERAÇÃO APENAS A DEPENDENCIA SE ALTERA.
    '''

from design_partters.factory.databases import SqLiteRepositorio

from typing import Type, Dict, Union


class UseCase:

    def __init__(self, repositorio: Type[SqLiteRepositorio]):
        self.__repositorio = repositorio

    def retorno(self, data: bool) -> Union[Dict, None]:
        if data is True:
            repositorioResponse = self.__repositorio.select_one()
            return repositorioResponse

        return None
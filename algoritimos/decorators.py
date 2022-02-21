import functools
import time
from time import strftime


def dec_hora(func):
    """Instancia uma função como parametro.
    :param: Decora uma função ex: olá_mundo.
    """
    print('O decorator é semelhante ao closure')

    def envoltoria() -> str:
        """Após a função decorador ser executada, executa a envoltoria"""
        now = strftime('%H:%M:%S')
        print(f'{now}, Executando a função')
        return func()

    return envoltoria


@dec_hora
def ola_mundo():
    """Executa o decorador e depois a propria função."""
    return 'Diga: Olá Mundo'


# decorador com parametros


def logar(fmt='%H:%M:%S'):
    """Recebe parametros na funçao decoradora"""

    def decorador(func):
        """Chama a função envoltoria."""

        @functools.wraps(func)
        def fun_interna(*args, **kwargs):
            """Exec a função interna de acordo com os parametros."""
            agora = strftime(fmt)
            print(f'{agora}, executando a função {func.__name__}')
            return func(*args, **kwargs)

        return fun_interna

    return decorador


@logar()
def helo_word2():
    return 'Diga: Helo Word2'


if __name__ == '__main__':
    # print(ola_mundo())
    print(helo_word2())

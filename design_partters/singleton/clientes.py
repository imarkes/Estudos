class _ClasseProtegida:
    """Define um objeto inacessivel."""
    pass


UNICA_INSTANCIA = _ClasseProtegida()


class _Singleton:
    pass


_singleton = None


def get_singleton():
    global _singleton
    if _singleton is None:
        _singleton = _Singleton()
    return _singleton


class Invocavel:
    def __init__(self, numero):
        self.numero = numero

    def __call__(self, *args, **kwargs):
        return self.numero


######################### EXEMPLO 3 ###########################

class _Singleton2:
    pass


SINGLETON = _Singleton2()

if __name__ == '__main__':
    invocavel = map(Invocavel, range(1, 4))
    # invocavel2 = map(Invocavel2, range(8, 11))
    #
    for i in invocavel:
        print('Exemplo 1: -> ', i())

    singleton_exemplo = SINGLETON
    print(singleton_exemplo)

if __name__ == '__main__':
    print(UNICA_INSTANCIA)
    print(id(UNICA_INSTANCIA))

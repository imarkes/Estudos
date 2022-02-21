import math


class Baskara:
    """
    Calcula a formula de Baskara
    """

    def main(self):
        """
        Recebe do usuario os numeros inteiros positivos e executa a fução
        :return:
        """
        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        c = float(input('Digite o valor de C: '))
        print(self.calcula_raiz(a, b, c))

    def delta(self, a: int, b: int, c: int):
        """
        Recebe numeros inteiros positivo e calcula o delta.
        :param a:
        :param b:
        :param c:
        :return: b ** 2 - 4 * a * c
        """
        return b ** 2 - 4 * a * c

    def calcula_raiz(self, a:int, b:int, c:int):
        """
        Calcula a raiz quadrada de delta.
        :param a: int
        :param b: int
        :param c: int
        :return: int
        """
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2


if __name__ == '__main__':
    b = Baskara()
    b.main()

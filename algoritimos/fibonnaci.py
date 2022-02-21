def fibonacci_recursivo(n):
    """
    Calcula o fibonnaci de forma recursiva
    :param n:
    :return:
    """
    if n < 2:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


print(fibonacci_recursivo(7))
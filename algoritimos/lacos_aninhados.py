# Cria uma tabuada.
linha = 1
coluna = 1
while linha <= 10:

    while coluna <= 10:
        print(linha * coluna, end='\t')
        coluna += 1
    linha += 1
    print()
    coluna = 1

# Fatorial
n = 1
while n >= 0:
    n = int(input('numero: ', ))
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n = int(input('numero 2: '))

# Fatorial numeros pirmos
n = int(input('numero >1: '))
fator = 2
multiplicidade = 0
while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0:
        print('fator', fator, 'multiplicidade = ', multiplicidade)
    fator += 1
    multiplicidade = 0



def eh_primo(x: int) -> int:
    """
    Verifica se o numero é primo.
    :param x:
    :return:
    """
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x / 2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True


n = int(input('digite um numero: '))
while n > 0:
    if eh_primo(n):
        print(n, 'é primo')
    else:
        print(n, 'não é primo')
    n = int(input('numero 2: '))

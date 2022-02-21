from design_partters.strategy_partten.atleta.atletas import Atleta
from design_partters.strategy_partten.atleta.corredores import CorrerRapido


bolt = Atleta(CorrerRapido(2))
bolt.acao()
bolt.atributos()

'''
    CRIA A INTERFACE 
    CRIA A CLASSE GENERICA(ATLETA), A CLASSE GENERICA OBRIGATORIAMENTE DEVE TER OS ATRIBUTOS OU METODOS DA INTERFACE
    A CLASSE CORRER-RAPIDO DEVE TER OS METODOS OU ATRIBUTOS DA CLASSE GENERICA.

'''

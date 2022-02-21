from design_partters.factory.factory import SqLiteFactoring


caso_uso = SqLiteFactoring.create()
response = caso_uso.retorno(True)

print(response)


'''
    CRIA A INTERFACE ABSTRATA
    CRIA A CLASSE GENERICA(NO CASO DATABASE)
    CRIA OS CASOS DE USO
    APLICA O FACTORY UNINDO OS ELEMENTOS
'''
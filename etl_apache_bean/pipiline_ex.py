# IMPORTA OS PACOTES:
# import apache_beam as beam
# frm apache_beam.option.pipeline_options import PipelineOptions

# Instanciando
# pipeline_options = PipelineOptions(args=None)
# pipeline = beam.Pipeline(options=pipeline_options) -> Em produção mais parametros são passados: qtd maquinas, memoria...

"""
CRIANDO OS METODOS DE ETL
"""


def converte_texto_em_lista(texto_string, delimitador=';'):
    """
    :param texto_string: '1;29/03/2003;16h00;Sábado'
    :param delimitador: ' ; '
    :return: ['1', '29/03/2003', '16h00', 'Sábado']
    """
    return texto_string.split(delimitador)


def transformar_lista_em_dicionario(listas, label):
    """
    :param listas: ['29/03/2003', '16h00', 'Sábado', 'Athlético-PR', 'PR']
    :param label: ['Data', 'Horário', 'Dia', 'Mandante', 'Estado']
    :return: {'Data': '29/03/2003', 'Horário': '16h00', 'Dia': 'Sábado', 'Mandante': 'Athlético-PR', 'Estado': 'PR'}
    """
    return dict(zip(label, listas))


def trata_datas(elemento):
    """
    :param elemento: {'Data': '29/03/2003'}
    :return: {'Data': '03-2003'}
    """
    elemento['mes_ano'] = '-'.join(elemento['Data'].split('/')[1:])
    return elemento


def cria_chave(elemento):
    """
    :param elemento: Recebe um dict {key:value}
    :return: retorna uma tupla (key,value)
    """
    chave = elemento['Estado']
    return chave, elemento


def desempacotando_dicionarios(elemento):
    """
    :param elemento: Recebe uma tupla ('UF', [{},{}])
    :return: ('UF-Data', Dia)
    """
    uf, registros = elemento
    for registro in registros:
        yield f"{uf}-{registro['mes_ano'], registro['Dia']}"


def filtra_campos_vazios(elemento):
    """
    :param elemento: Recebe um elemento (key, {'campo1': [], 'campo2':[1.0]})
    :return: (key, {'campo1':[1.0]})
    """
    chave, dados = elemento
    if all([
        dados['campo1'],
        dados['campo2']
    ]):
        return True
    return False


def desagrupando_elementos(elemento):
    """
    :param elemento: ('PR-03-2003', {'campo1': [5.0], 'campo2':[1.0]})
    :return:(PR,03-2003, 5.0,1.0)
    """
    chave, dados = elemento
    campo1 = dados['campo1'][0]
    campo2 = dados['campo2'][0]
    uf, mes, ano = chave.split('-')
    return uf, mes, ano, str(campo1), str(campo2)


def preparando_csv(elemento, delimitador=';'):
    """
    :param delimitador: ";"
    :param elemento: ('PR', 3, 2003, 5.0, 1.0)
    :return: ('PR'; 3; 2003; 5.0; 1.0)
    """
    return f"{delimitador}".join(elemento)


# CRIANDO PIPELINES E JUNTANDO
"""
    campeonato(
        pipeline
        | "Leitura do dataset dados campeonato" >> ReadFromText('Dados_campeonato.txt', skip_header_lines=1)
        | "Conversao de texto para lista" >> beam.Map(converte_csv_em_lista)
        | "Conversao de lista para dicionarios" >> beam.Map(transformar_lista_em_dicionario, colunas)
        | "Tratando as datas" >> beam.Map(trata_datas)
        | "Criar uma chave para o elemento" >> beam.Map(cria_chave)
        | "Agrupa pela chave escolhida" >> beam.GroupByKey()
        | "Descompactando elemento" >> beam.FlatMap(desempacotando_dicionarios)
        | "combina os elementos pela chave" >> beam.CombinePerkey(sum)
       #| "Mostra os resultados na tela" >> beam.Map(print)
    )

    clubes(
        pipeline
        | "Leitura do dataset dados campeonato" >> ReadFromText('clubes.txt', skip_header_lines=1)
        | "Conversao de texto para lista" >> beam.Map(converte_csv_em_lista)
        | "Conversao de lista para dicionarios" >> beam.Map(transformar_lista_em_dicionario, colunas)
        | "Tratando as datas" >> beam.Map(trata_datas)
        | "Criar uma chave para o elemento" >> beam.Map(cria_chave)
        | "Agrupa pela chave escolhida" >> beam.GroupByKey()
        | "Descompactando elemento" >> beam.FlatMap(desempacotando_dicionarios)
        | "combina os elementos pela chave" >> beam.CombinePerkey(sum)
        #| "Mostra os resultados na tela" >> beam.Map(print)
    )

    resultado(
        ({'campeonato':campeonato, 'clubes':clubes})
        #| "Unindo as pcols com empilhamento >> beam.Flatten()
        #| "Agrupamento das pcols pela chave >> beam.GroupByKey()
        #| "Filtrando dados vazios >> beam.Filter(filtra_campos_vazios)
        | "mesclando as pcols, isso substitui o flatten e o GroupByKey >> beam.CoGroupByKey()
        | "Preparando o csv" >> beam.Map(preparando_csv)
        | "Descompactando elementos" >> beam.Map(desagrupando_elementos)
    )
    headers = 'UF;MES;ANO;VALOR;QUANTIDADE'
    resultado | "Cria o csv com a pcol resultado" >> WriteTotext('nome_csv, file_name_suffix = '.csv', header=headers)
    pipeline.run()
"""

arquivo = '29/03/2003;16h00;Sábado;Athlético-PR;PR'
colunas = ['Data', 'Horário', 'Dia', 'Mandante', 'Estado']
lista = ['29/03/2003', '16h00', 'Sábado', 'Athlético-PR', 'PR'], ['29/03/2003', '16h00', 'Sábado', 'Guarani', 'SP']

elemento_dict = {'Data': '29/03/2003', 'Horário': '16h00', 'Dia': 'Sábado', 'Mandante': 'Athlético-PR', 'Estado': 'PR',
                 'mes_ano': '03-2003'}

if __name__ == '__main__':
    ...
    # a = converte_texto_em_lista(arquivo, ';')
    # print(a)
    # b = transformar_lista_em_dicionario(lista, colunas)
    # print(b)
    # c = trata_datas(
    #     {'Data': '29/03/2003', 'Horário': '16h00', 'Dia': 'Sábado', 'Mandante': 'Athlético-PR', 'Estado': 'PR'})
    # print(c)
    # d = cria_chave(elemento_dict)
    # print(d)
    # e = desempacotando_dicionarios(('PR', {'Data': '29/03/2003', 'Horário': '16h00', 'Dia': 'Sábado',
    #                                        'Mandante': 'Athlético-PR', 'Estado': 'PR', 'mes_ano': '03-2003'}))
    # print(e)
    # f = desagrupando_elementos(('PR-03-2003', {'campo1': [5.0], 'campo2': [1.0]}))
    # print(f)
    # g = preparando_csv(('PR', '03', '2003', '5.0', '1.0'))
    # print(g)

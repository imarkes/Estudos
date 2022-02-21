import csv


def ler_csv(file):
    """
    Ler arquivos CSV
    :param file:
    :return:
    """
    X = []
    Y = []
    arquivo = open(file, 'rb')
    leitor = csv.reader(arquivo)

    leitor.next()  # Pula a linha de cabeçãlho se necessário.

    for label1, label2, label3 in leitor:
        X.append([int(label1), int(label2)])
        Y.append(int(label3))

    return X, Y


def ler_csv_para_salvar_em_banco(self, filename):
    """Ler o arquivo e insere as linhas no banco de dados."""
    try:
        FILE_CSV = csv.DictReader(open(filename, encoding='utf-8'))

        for row in FILE_CSV:
            self.inserir_dados_no_bd(row['campo1'], row['campo2'], row['campo3'])

        print('Success')

    except ConnectionError as e:
        raise (f'Erro ao inserir os dados: Error: {e}')


def criar_csv():
    """Cria um arquivo CSV de acordo com o result recebido. """
    result = ''

    try:
        with open('nome_arquivo.csv', 'w', newline='', encoding='utf-8') as file:

            fieldnames = ['campo1', 'campo2', 'campo3']

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in result:
                writer.writerow(
                    {'campo1': row[0], 'campo2': row[1], 'campo3': row[2]})

    finally:
        file.close()

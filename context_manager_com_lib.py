# Importando o decorator contextmanager do módulo contextlib
from contextlib import contextmanager

# Definindo uma função que atuará como um context manager
@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        # Mensagem informando que o arquivo está sendo aberto
        print('Abrindo arquivo')
        # Abrindo o arquivo com o modo especificado e encoding 'utf8'
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        # Yielding o objeto do arquivo para o bloco with
        yield arquivo
    except Exception as e:
        # Capturando e imprimindo qualquer exceção que ocorra
        print('Ocorreu erro', e)
    finally:
        # Mensagem informando que o arquivo está sendo fechado
        print('Fechando arquivo')
        # Fechando o arquivo
        arquivo.close()

# Usando o context manager com a palavra-chave with
with my_open('aula150.txt', 'w') as arquivo:
    # Escrevendo linhas no arquivo
    arquivo.write('Linha 1\n')
    # Esta linha contém um erro de argumento, que irá causar uma exceção
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    # Imprimindo o objeto arquivo dentro do bloco with
    print('WITH', arquivo)

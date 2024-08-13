# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html

# Definindo uma exceção personalizada chamada MeuError que herda de Exception
class MeuError(Exception):
    ...

# Definindo outra exceção personalizada chamada OutroError que herda de Exception
class OutroError(Exception):
    ...

# Função que levanta uma exceção personalizada MeuError
def levantar():
    # Criando uma instância de MeuError com argumentos 'a', 'b', 'c'
    exception_ = MeuError('a', 'b', 'c')
    # Levantando a exceção MeuError
    raise exception_

# Bloco try-except para capturar e tratar exceções
try:
    # Chamando a função que levanta a exceção
    levantar()
except (MeuError, ZeroDivisionError) as error:
    # Captura exceções do tipo MeuError ou ZeroDivisionError
    # Imprimindo o nome da classe da exceção capturada
    print(error.__class__.__name__)
    # Imprimindo os argumentos passados para a exceção
    print(error.args)
    print()
    # Criando uma nova exceção OutroError com uma mensagem
    exception_ = OutroError('Vou lançar de novo')
    # Relançando a nova exceção, mantendo a cadeia de exceções
    raise exception_ from error

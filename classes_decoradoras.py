# Definição da classe Multiplicar
class Multiplicar:
    def __init__(self, multiplicador):
        # Inicializa a instância com o multiplicador fornecido
        self._multiplicador = multiplicador

    def __call__(self, func):
        # Define o método __call__ para transformar a instância em um decorador
        def interna(*args, **kwargs):
            # Define a função interna que será retornada pelo decorador
            resultado = func(*args, **kwargs)
            # Multiplica o resultado da função decorada pelo multiplicador
            return resultado * self._multiplicador
        # Retorna a função interna que realiza a multiplicação
        return interna


# Utiliza a classe Multiplicar como decorador para a função soma
@Multiplicar(2)
def soma(x, y):
    # Função que retorna a soma de dois números
    return x + y


# Chama a função soma(2, 4) decorada com Multiplicar(2)
# O resultado da soma (2 + 4) será multiplicado por 2
dois_mais_quatro = soma(2, 4)
# Imprime o resultado final, que é 12
print(dois_mais_quatro)

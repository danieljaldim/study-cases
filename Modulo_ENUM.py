import enum

# Função simples para mover em uma direção qualquer
def mover(direcao):
    print(f'Movendo para {direcao}')

# Chamadas para a função mover com strings como argumentos
mover('esquerda')
mover('direita')
mover('acima')
mover('abaixo')

# Definindo uma enumeração para direções
class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

# Exibindo valores da enumeração
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)

# Função para mover utilizando a enumeração Direcoes
def mover(direcao: Direcoes):
    # Verifica se a direção fornecida é uma instância da enumeração Direcoes
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    # Exibe a direção em que está se movendo
    print(f'Movendo para {direcao.name} ({direcao.value})')

# Chamadas para a função mover utilizando a enumeração Direcoes
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)

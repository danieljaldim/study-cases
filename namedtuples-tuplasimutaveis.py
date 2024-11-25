# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple
from collections import namedtuple

from typing import NamedTuple

# Define uma classe chamada Carta que herda de NamedTuple.
# NamedTuple é uma forma de definir tuplas nomeadas com campos tipados.
class Carta(NamedTuple):
    valor: str = 'VALOR'  # Define um campo 'valor' com o tipo str e um valor padrão 'VALOR'.
    naipe: str = 'NAIPE'  # Define um campo 'naipe' com o tipo str e um valor padrão 'NAIPE'.

# Comentado: Outra forma de criar uma tupla nomeada utilizando namedtuple da biblioteca collections.
# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )

# Cria uma instância de Carta, passando apenas o valor 'A'.
# O campo 'naipe' usará o valor padrão 'NAIPE' definido na classe.
as_espadas = Carta('A')

# Exibe os campos e valores de as_espadas como um dicionário.
print(as_espadas._asdict())  # {'valor': 'A', 'naipe': 'NAIPE'}

# Exibe a representação da tupla as_espadas.
print(as_espadas)  # Carta(valor='A', naipe='NAIPE')

# Acessa e imprime o primeiro campo da tupla usando índice.
print(as_espadas[0])  # 'A'

# Acessa e imprime o campo 'valor' usando o nome do campo.
print(as_espadas.valor)  # 'A'

# Acessa e imprime o segundo campo da tupla usando índice.
print(as_espadas[1])  # 'NAIPE'

# Acessa e imprime o campo 'naipe' usando o nome do campo.
print(as_espadas.naipe)  # 'NAIPE'

print()  # Imprime uma linha em branco para separação.

# Exibe os nomes dos campos da tupla.
print(as_espadas._fields)  # ('valor', 'naipe')

# Exibe os valores padrão dos campos definidos na classe Carta.
print(as_espadas._field_defaults)  # {'valor': 'VALOR', 'naipe': 'NAIPE'}

# Itera sobre os valores da tupla as_espadas e os imprime.
for valor in as_espadas:
    print(valor)  # 'A' e 'NAIPE' serão impressos em linhas separadas.

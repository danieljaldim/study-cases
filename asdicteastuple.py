# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple

@dataclass(repr=True)  # O decorador @dataclass com repr=True gera automaticamente um método __repr__ que inclui todos os atributos da classe na sua representação.
@dataclass
class Pessoa:
    nome: str         # Atributo 'nome' do tipo string
    sobrenome: str    # Atributo 'sobrenome' do tipo string

# Bloco de código principal que será executado apenas se o script for rodado diretamente
if __name__ == '__main__':
    # Criação de uma lista de objetos 'Pessoa' com diferentes valores para nome e sobrenome
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    
    # Ordena a lista de pessoas em ordem decrescente com base no sobrenome
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)  # Imprime a lista de pessoas ordenadas
    
    p1 = Pessoa('Luiz', 'Otávio')  # Cria uma instância de 'Pessoa' com nome 'Luiz' e sobrenome 'Otávio'
    
    # Converte a instância 'p1' em um dicionário e imprime as chaves do dicionário
    print(asdict(p1).keys())
    
    # Imprime os valores do dicionário gerado por asdict
    print(asdict(p1).values())
    
    # Imprime os pares chave-valor do dicionário gerado por asdict
    print(asdict(p1).items())
    
    # Converte a instância 'p1' em uma tupla e imprime o primeiro elemento da tupla (que é o valor do atributo 'nome')
    print(astuple(p1)[0])

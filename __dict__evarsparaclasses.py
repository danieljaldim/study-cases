# Definição da classe Pessoa
class Pessoa:
    # Atributo de classe que armazena o ano atual
    ano_atual = 2022

    # Método construtor (__init__) para inicializar os atributos de instância
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância para o nome
        self.idade = idade  # Atributo de instância para a idade

    # Método de instância para calcular o ano de nascimento
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade  # Retorna o ano de nascimento calculado com base na idade
    
# Dicionário com dados para criar uma instância de Pessoa
dados = {'nome': 'João', 'idade': 35}

# Criação de uma instância de Pessoa utilizando o desempacotamento do dicionário
p1 = Pessoa(**dados)

# As linhas comentadas abaixo mostram como manipular os atributos da instância diretamente

# p1.nome = 'EITA'  # Modifica o atributo nome da instância p1
# print(p1.idade)  # Imprime o atributo idade da instância p1

# Adiciona um novo atributo 'outra' na instância p1 usando __dict__
# p1.__dict__['outra'] = 'coisa'

# Modifica o atributo 'nome' na instância p1 usando __dict__
# p1.__dict__['nome'] = 'EITA'

# Remove o atributo 'nome' da instância p1 usando __dict__
# del p1.__dict__['nome']

# Imprime o dicionário de atributos da instância p1 usando __dict__
# print(p1.__dict__)

# Imprime o dicionário de atributos da instância p1 usando vars (equivalente a __dict__)
# print(vars(p1))

# Acessa e imprime o atributo 'outra' adicionado anteriormente
# print(p1.outra)

# Acessa e imprime o atributo 'nome' da instância p1
# print(p1.nome)
# Imprime o dicionário de atributos da instância p1 usando vars
print(vars(p1))

# Acessa e imprime o atributo 'nome' da instância p1
print(p1.nome)
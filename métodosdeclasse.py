# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
# Classe Pessoa com métodos de classe e factories
class Pessoa:
    ano = 2023  # Atributo de classe

    # Método construtor (__init__) para inicializar os atributos de instância
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância para o nome
        self.idade = idade  # Atributo de instância para a idade

    # Método de classe (classmethod) que recebe a classe como primeiro parâmetro (cls)
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')  # Imprime uma mensagem

    # Método de classe (classmethod) que cria uma instância de Pessoa com 50 anos de idade
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)  # Retorna uma nova instância de Pessoa com 50 anos

    # Método de classe (classmethod) que cria uma instância de Pessoa com nome 'Anônima'
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)  # Retorna uma nova instância de Pessoa com nome 'Anônima'
    
    # Criação de uma instância de Pessoa usando o método construtor normal
p1 = Pessoa('João', 34)

# Criação de uma instância de Pessoa usando o método de classe criar_com_50_anos
p2 = Pessoa.criar_com_50_anos('Helena')

# Criação de uma instância de Pessoa usando o método construtor normal
p3 = Pessoa('Anônima', 23)

# Criação de uma instância de Pessoa usando o método de classe criar_sem_nome
p4 = Pessoa.criar_sem_nome(25)

# Imprime o nome e a idade da instância p2
print(p2.nome, p2.idade)

# Imprime o nome e a idade da instância p3
print(p3.nome, p3.idade)

# Imprime o nome e a idade da instância p4
print(p4.nome, p4.idade)
# Definindo a classe base Pessoa
class Pessoa:
    # Atributo de classe, compartilhado por todas as instâncias
    cpf = '1234'

    # Método inicializador, chamado ao criar uma instância da classe
    def __init__(self, nome, sobrenome):
        self.nome = nome  # Atributo de instância
        self.sobrenome = sobrenome  # Atributo de instância

    # Método que imprime o nome completo e o nome da classe
    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)  # __class__.__name__ obtém o nome da classe da instância


# Definindo a classe Cliente que herda de Pessoa
class Cliente(Pessoa):
    # Sobrescrevendo o método falar_nome_classe
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)  # __class__.__name__ obtém o nome da classe da instância


# Definindo a classe Aluno que herda de Pessoa
class Aluno(Pessoa):
    # Sobrescrevendo o atributo de classe cpf
    cpf = 'cpf aluno'
    ...


# Criando uma instância de Cliente
c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()  # Chama o método falar_nome_classe definido na classe Cliente

# Criando uma instância de Aluno
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()  # Chama o método falar_nome_classe herdado da classe Pessoa
print(a1.cpf)  # Acessa o atributo de classe cpf definido na classe Aluno

# Mostra a documentação da classe Cliente, incluindo métodos herdados e sobrescritos
# help(Cliente)
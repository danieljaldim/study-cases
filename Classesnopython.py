# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome  # Inicializa o atributo nome
        self.sobrenome = sobrenome  # Inicializa o atributo sobrenome

# Criação de instâncias da classe Pessoa com nome e sobrenome
p1 = Pessoa('Luiz', 'Otávio')
p2 = Pessoa('Maria', 'Joana')

# Impressão dos atributos nome e sobrenome de p1
print(p1.nome)
print(p1.sobrenome)

# Impressão dos atributos nome e sobrenome de p2
print(p2.nome)
print(p2.sobrenome)
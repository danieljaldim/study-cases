# Definição da classe Carro
class Carro:
    # Método construtor da classe, inicializa o objeto com o nome do carro
    def __init__(self, nome):
        self.nome = nome  # Atributo nome para armazenar o nome do carro

    # Método para simular a ação de acelerar o carro
    def acelerar(self):
        print(f'{self.nome} está acelerando...')  # Imprime uma mensagem indicando que o carro está acelerando


# Exemplo de uso de métodos de string em Python
string = 'Luiz'
print(string.upper())  # Converte a string para letras maiúsculas e imprime

# Criação de um objeto da classe Carro com o nome 'Fusca'
fusca = Carro('Fusca')
print(fusca.nome)  # Imprime o nome do carro 'Fusca'
fusca.acelerar()  # Chama o método acelerar para o objeto 'Fusca'

# Criação de outro objeto da classe Carro com o nome 'Celta'
celta = Carro(nome='Celta')
print(celta.nome)  # Imprime o nome do carro 'Celta'
celta.acelerar()  # Chama o método acelerar para o objeto 'Celta'
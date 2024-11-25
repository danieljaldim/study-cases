# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        # Método construtor que inicializa o objeto Cliente com um nome e uma lista vazia de endereços.
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        # Método que cria um novo objeto Endereco e o adiciona à lista de endereços do cliente.
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        # Método que adiciona um objeto Endereco existente à lista de endereços do cliente.
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        # Método que imprime todos os endereços associados ao cliente.
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        # Método especial que é chamado quando o objeto Cliente é destruído.
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        # Método construtor que inicializa o objeto Endereco com uma rua e um número.
        self.rua = rua
        self.numero = numero

    def __del__(self):
        # Método especial que é chamado quando o objeto Endereco é destruído.
        print('APAGANDO,', self.rua, self.numero)


# Criação de um objeto Cliente chamado 'Maria'
cliente1 = Cliente('Maria')

# Inserção de dois endereços usando o método inserir_endereco
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)

# Criação de um objeto Endereco chamado endereco_externo
endereco_externo = Endereco('Av Saudade', 123213)

# Inserção de endereco_externo no cliente usando o método inserir_endereco_externo
cliente1.inserir_endereco_externo(endereco_externo)

# Listagem de todos os endereços do cliente
cliente1.listar_enderecos()

# Destruição do objeto cliente1, o que acionará o método __del__ de Cliente
del cliente1

# Impressão dos atributos do objeto endereco_externo
print(endereco_externo.rua, endereco_externo.numero)

# Indicação de que o código terminou
print('**** AQUI TERMINA MEU CÓDIGO****')

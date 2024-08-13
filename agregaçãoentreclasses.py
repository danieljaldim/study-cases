# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

# Classe Carrinho para gerenciar produtos
class Carrinho:
    def __init__(self):
        # Inicializa a lista de produtos vazia
        self._produtos = []

    # Método para calcular o total dos preços dos produtos no carrinho
    def total(self):
        # Soma o preço de cada produto na lista de produtos
        return sum([p.preco for p in self._produtos])

    # Método para inserir múltiplos produtos no carrinho
    def inserir_produtos(self, *produtos):
        # Adiciona cada produto fornecido à lista de produtos
        for produto in produtos:
            self._produtos.append(produto)

    # Método para listar todos os produtos no carrinho
    def listar_produtos(self):
        print()
        # Imprime o nome e o preço de cada produto no carrinho
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

# Classe Produto para representar um produto com nome e preço
class Produto:
    def __init__(self, nome, preco):
        # Atributos de instância para nome e preço do produto
        self.nome = nome
        self.preco = preco

# Instancia a classe Carrinho
carrinho = Carrinho()

# Cria duas instâncias da classe Produto
p1 = Produto('Caneta', 1.20)
p2 = Produto('Camiseta', 20)

# Insere os produtos no carrinho
carrinho.inserir_produtos(p1, p2)

# Lista os produtos no carrinho
carrinho.listar_produtos()

# Imprime o total dos preços dos produtos no carrinho
print(carrinho.total())

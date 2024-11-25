# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
class Escritor:
    def __init__(self, nome) -> None:
        # Inicializa a instância da classe Escritor com o atributo nome
        self.nome = nome
        # Atributo privado _ferramenta inicializado como None
        self._ferramenta = None

    @property
    def ferramenta(self):
        # Getter para o atributo _ferramenta
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        # Setter para o atributo _ferramenta
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome):
        # Inicializa a instância da classe FerramentaDeEscrever com o atributo nome
        self.nome = nome

    def escrever(self):
        # Método que retorna uma string indicando que a ferramenta está escrevendo
        return f'{self.nome} está escrevendo'

# Cria uma instância da classe Escritor com o nome 'Luiz'
escritor = Escritor('Luiz')

# Cria uma instância da classe FerramentaDeEscrever com o nome 'Caneta Bic'
caneta = FerramentaDeEscrever('Caneta Bic')

# Cria uma instância da classe FerramentaDeEscrever com o nome 'Máquina'
maquina_de_escrever = FerramentaDeEscrever('Máquina')

# Define a ferramenta do escritor como a máquina de escrever
escritor.ferramenta = maquina_de_escrever

# Imprime a string retornada pelo método escrever da caneta
print(caneta.escrever())  # Saída: Caneta Bic está escrevendo

# Imprime a string retornada pelo método escrever da máquina de escrever
print(maquina_de_escrever.escrever())  # Saída: Máquina está escrevendo

# Imprime a string retornada pelo método escrever da ferramenta do escritor (máquina de escrever)
print(escritor.ferramenta.escrever())  # Saída: Máquina está escrevendo

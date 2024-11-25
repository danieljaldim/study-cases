class Carro:
    # Atributo de classe
    total_carros = 0

    def __init__(self, nome):
        # Atributo de instância
        self.nome = nome
        # Incrementa o contador de carros a cada criação de instância
        Carro.total_carros += 1

    def mostrar_nome(self):
        print(f'Nome do carro: {self.nome}')

    @classmethod
    def mostrar_total_carros(cls):
        print(f'Total de carros: {cls.total_carros}')

# Criando instâncias da classe Carro
carro1 = Carro('Fusca')
carro2 = Carro('Celta')

# Acessando o atributo de instância
carro1.mostrar_nome()  # Saída: Nome do carro: Fusca
carro2.mostrar_nome()  # Saída: Nome do carro: Celta

# Acessando o atributo de classe
Carro.mostrar_total_carros()  # Saída: Total de carros: 2
class Carro:
    # Atributo de classe
    num_de_rodas = 4

    def __init__(self, nome, cor):
        # Atributos de instância
        self.nome = nome
        self.cor = cor
        self.ligado = False

    # Método de instância
    def ligar(self):
        self.ligado = True
        print(f'{self.nome} está ligado.')

    # Método de instância
    def desligar(self):
        self.ligado = False
        print(f'{self.nome} está desligado.')

    # Método de classe
    @classmethod
    def obter_num_de_rodas(cls):
        return cls.num_de_rodas

    # Método estático
    @staticmethod
    def checar_combustivel():
        print('Verificando nível de combustível...')

# Criando instâncias da classe Carro
fusca = Carro('Fusca', 'Azul')
celta = Carro('Celta', 'Vermelho')

# Chamando métodos de instância
fusca.ligar()
celta.desligar()

# Acessando atributo de classe
print(f'Todos os carros têm {Carro.num_de_rodas} rodas.')

# Chamando método de classe
print(Carro.obter_num_de_rodas())

# Chamando método estático
Carro.checar_combustivel()
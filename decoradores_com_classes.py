# Função para criar uma representação string de um objeto
def meu_repr(self):
    # Obtém o nome da classe do objeto
    class_name = self.__class__.__name__
    # Obtém o dicionário de atributos da instância
    class_dict = self.__dict__
    # Cria a representação string do objeto
    class_repr = f'{class_name}({class_dict})'
    return class_repr

# Decorador que adiciona a função meu_repr como método __repr__ de uma classe
def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls

# Decorador para modificar o comportamento do método falar_nome
def meu_planeta(metodo):
    # Função interna que será chamada no lugar do método original
    def interno(self, *args, **kwargs):
        # Chama o método original
        resultado = metodo(self, *args, **kwargs)
        # Se 'Terra' estiver no resultado, retorna uma mensagem especial
        if 'Terra' in resultado:
            return 'Você está em casa'
        # Caso contrário, retorna o resultado original
        return resultado
    return interno

# Decorando a classe Time com o decorador adiciona_repr
@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

# Decorando a classe Planeta com o decorador adiciona_repr
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    # Decorando o método falar_nome com meu_planeta
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'

# Criando instâncias da classe Time
brasil = Time('Brasil')
portugal = Time('Portugal')

# Criando instâncias da classe Planeta
terra = Planeta('Terra')
marte = Planeta('Marte')

# Imprimindo a representação string das instâncias da classe Time
print(brasil)    # Output: Time({'nome': 'Brasil'})
print(portugal)  # Output: Time({'nome': 'Portugal'})

# Imprimindo a representação string das instâncias da classe Planeta
print(terra)     # Output: Planeta({'nome': 'Terra'})
print(marte)     # Output: Planeta({'nome': 'Marte'})

# Chamando o método falar_nome nas instâncias da classe Planeta
print(terra.falar_nome())    # Output: 'Você está em casa'
print(marte.falar_nome())    # Output: 'O planeta é Marte'

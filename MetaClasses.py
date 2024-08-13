# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)

# object acima
# class Foo:
#     ...

# Definimos uma função meu_repr que irá retornar uma string
# representando a instância da classe, mostrando o nome da classe e os atributos da instância.
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

# Definimos uma metaclasse chamada Meta.
class Meta(type):
    # O método __new__ da metaclasse é chamado antes de __init__ e é responsável por criar a nova classe.
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        # Cria a nova classe utilizando o método __new__ da metaclasse pai.
        cls = super().__new__(mcs, name, bases, dct)
        # Adiciona um atributo 'attr' com valor 1234 à nova classe.
        cls.attr = 1234
        # Substitui o método __repr__ da nova classe pela função meu_repr.
        cls.__repr__ = meu_repr

        # Verifica se a nova classe tem um método 'falar' e se ele é chamável.
        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            # Se a condição não for satisfeita, lança um erro NotImplementedError.
            raise NotImplementedError('Implemente falar')

        return cls

    # O método __call__ é chamado quando uma instância da classe é criada.
    def __call__(cls, *args, **kwargs):
        # Cria a instância utilizando o método __call__ da classe pai.
        instancia = super().__call__(*args, **kwargs)

        # Verifica se a instância tem um atributo 'nome'.
        if 'nome' not in instancia.__dict__:
            # Se a condição não for satisfeita, lança um erro NotImplementedError.
            raise NotImplementedError('Crie o attr nome')

        return instancia

# Definimos uma classe Pessoa que usa a metaclasse Meta.
class Pessoa(metaclass=Meta):
    # Descomente a linha abaixo para testar o comportamento sem um método 'falar' válido.
    # falar = 123

    # O método __new__ é chamado antes de __init__ e é responsável por criar a nova instância.
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    # O método __init__ é chamado para inicializar a nova instância.
    def __init__(self, nome):
        print('MEU INIT')
        # A linha abaixo está comentada para testar o comportamento sem um atributo 'nome'.
        # self.nome = nome

    # Define o método 'falar' que imprime uma mensagem.
    def falar(self):
        print('FALANDO...')

# Cria uma instância da classe Pessoa com o nome 'Luiz'.
p1 = Pessoa('Luiz')
# Chama o método 'falar' da instância p1.
p1.falar()

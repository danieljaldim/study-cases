# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        # O método __new__ é chamado antes de __init__.
        # Ele é responsável por criar uma nova instância da classe.
        # O super().__new__(cls) chama o método __new__ da superclasse
        # (no caso, a classe object) para criar a instância.
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        # O método __init__ é o inicializador da instância.
        # Ele é chamado logo após __new__, para inicializar a instância criada.
        self.x = x
        print('Sou o init')

    def __repr__(self):
        # O método __repr__ é usado para obter a representação em string
        # "oficial" do objeto. É útil para depuração.
        return 'A()'


# Criação de uma instância da classe A.
a = A(123)

# Acessando o atributo 'x' da instância.
print(a.x)

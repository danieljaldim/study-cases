# Definindo a classe A que herda de object
class A(object):
    # Atributo de classe
    atributo_a = 'valor a'

    # Construtor da classe A
    def __init__(self, atributo):
        self.atributo = atributo

    # Método da classe A
    def metodo(self):
        print('A')

# Definindo a classe B que herda da classe A
class B(A):
    # Atributo de classe
    atributo_b = 'valor b'

    # Construtor da classe B
    def __init__(self, atributo, outra_coisa):
        # Chama o construtor da superclasse (A)
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    # Método da classe B
    def metodo(self):
        print('B')

# Definindo a classe C que herda da classe B
class C(B):
    # Atributo de classe
    atributo_c = 'valor c'

    # Construtor da classe C
    def __init__(self, *args, **kwargs):
        # Chama o construtor da superclasse (B)
        super().__init__(*args, **kwargs)

    # Método da classe C
    def metodo(self):
        # Chama diretamente o método da classe A
        A.metodo(self)
        # Chama diretamente o método da classe B
        B.metodo(self)
        # Executa o próprio método da classe C
        print('C')

# Instância da classe C
c = C('Atributo', 'Qualquer')

# Chama o método da instância da classe C
c.metodo()

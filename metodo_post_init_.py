from dataclasses import dataclass

@dataclass
@dataclass(init=False)  # O decorador @dataclass é usado para simplificar a criação de classes com atributos. O parâmetro init=False desabilita a geração automática do método __init__.
class Pessoa:
    nome: str          # Declaração do atributo 'nome' como uma string.
    sobrenome: str     # Declaração do atributo 'sobrenome' como uma string.

    @property
    def nome_completo(self):
        # Define uma propriedade 'nome_completo' que retorna o nome completo da pessoa.
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        # Setter para a propriedade 'nome_completo' que permite alterar o nome completo.
        # O valor é dividido em nome e sobrenome usando o método split().
        nome, *sobrenome = valor.split()
        # A variável 'sobrenome' é reatribuída com a junção das partes restantes.
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)
    
    def __init__(self, nome, sobrenome):
        # O método __init__ é definido manualmente, uma vez que init=False no @dataclass.
        # Inicializa os atributos 'nome' e 'sobrenome' com os valores passados.
        self.nome = nome
        # A linha a seguir foi sobrescrita erroneamente. Ela junta os sobrenomes novamente em uma única string.
        self.sobrenome = ' '.join(sobrenome)
        # Finalmente, reatribui o valor para o atributo 'sobrenome' (isto não faz sentido, pois o valor foi sobrescrito anteriormente).
        self.sobrenome = sobrenome
        # Define o nome completo com base nos valores passados.
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    def __post_init__(self):
        # O método __post_init__ é um gancho especial fornecido pelo @dataclass, que é executado após o __init__.
        # Neste caso, apenas imprime "POST INIT" quando é chamado.
        print('POST INIT')

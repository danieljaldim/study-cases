from dataclasses import dataclass

# A classe 'Pessoa' é decorada com '@dataclass', o que automaticamente
# gera métodos especiais como '__init__', '__repr__', '__eq__', entre outros.
@dataclass
class Pessoa:
    nome: str         # Define o atributo 'nome' como uma string
    idade: int        # Define o atributo 'idade' como um inteiro
    sobrenome: str    # Define o atributo 'sobrenome' como uma string

    # Um método que age como uma propriedade para obter o nome completo
    @property
    def nome_completo(self):
        # Retorna o nome completo combinando o nome e sobrenome
        return f'{self.nome} {self.sobrenome}'

    # Define um setter para a propriedade 'nome_completo'
    # Este método permite atribuir um valor ao 'nome_completo'
    @nome_completo.setter
    def nome_completo(self, valor):
        # Divide o valor recebido em nome e sobrenome usando o método 'split'
        nome, *sobrenome = valor.split()
        # Atribui o primeiro valor ao atributo 'nome'
        self.nome = nome
        # Junta o restante das partes como sobrenome e atribui ao atributo 'sobrenome'
        self.sobrenome = ' '.join(sobrenome)

# Verifica se o código está sendo executado diretamente (e não importado como módulo)
if __name__ == 'main':
    # Cria duas instâncias de 'Pessoa' com os mesmos valores para comparar
    p1 = Pessoa('Luiz', 30)
    p2 = Pessoa('Luiz', 30)
    # Verifica se p1 e p2 são iguais usando o método '__eq__' gerado automaticamente pelo dataclass
    print(p1 == p2)  # Retorna True porque os atributos são iguais

    # Cria uma nova instância de 'Pessoa' com nome e sobrenome
    p1 = Pessoa('Luiz', 'Otávio')
    # Atribui um novo nome completo usando o setter da propriedade 'nome_completo'
    p1.nome_completo = 'Maria Helena'
    # Imprime a instância 'p1'. O dataclass gera um método '__repr__' que mostra os atributos
    print(p1)  # Exibe algo como Pessoa(nome='Maria', idade=30, sobrenome='Helena')

    # Imprime o nome completo da pessoa usando a propriedade 'nome_completo'
    print(p1.nome_completo)  # Exibe 'Maria Helena'

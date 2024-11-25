# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json  # Importa o módulo json para trabalhar com arquivos JSON.

# Constante que define o caminho do arquivo onde os dados serão armazenados.
CAMINHO_ARQUIVO = 'aula127.json'

# Definição da classe Pessoa, que tem dois atributos: nome e idade.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Inicializa o atributo nome.
        self.idade = idade  # Inicializa o atributo idade.

# Instâncias da classe Pessoa são criadas.
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

# Cria uma lista de dicionários representando os objetos Pessoa.
# vars(obj) e obj.__dict__ retornam o dicionário de atributos de um objeto.
bd = [vars(p1), p2.__dict__, vars(p3)]

# Função para salvar os dados no arquivo JSON.
def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:  # Abre o arquivo no modo de escrita.
        print('FAZENDO DUMP')  # Exibe uma mensagem informando que o dump está sendo feito.
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)  # Escreve a lista bd no arquivo em formato JSON.

# Verifica se o script está sendo executado diretamente.
if __name__ == '__main__':
    print('ELE É O __main__')  # Exibe uma mensagem indicando que o script é o principal.
    fazer_dump()  # Chama a função fazer_dump para salvar os dados no arquivo JSON.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f'Título: {livro.titulo}, Autor: {livro.autor}')

# Exemplo de uso
biblioteca = Biblioteca()
livro1 = Livro('1984', 'George Orwell')
livro2 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien')

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

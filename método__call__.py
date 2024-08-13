class CallMe:
    def __init__(self, phone):
        # O construtor (__init__) inicializa o atributo phone com o número de telefone fornecido.
        self.phone = phone

    def __call__(self, nome):
        # O método especial __call__ permite que a instância da classe seja chamada como uma função.
        # Quando a instância é chamada com um argumento (nome), ela imprime uma mensagem e retorna um valor fixo (2134).
        print(nome, 'está chamando', self.phone)
        return 2134


# Cria uma instância da classe CallMe com o número de telefone '23945876545'.
call1 = CallMe('23945876545')

# Chama a instância call1 como se fosse uma função, passando 'Luiz Otávio' como argumento.
# Isso invoca o método __call__ da instância call1.
retorno = call1('Luiz Otávio')

# Imprime o valor retornado pelo método __call__, que é 2134.
print(retorno)

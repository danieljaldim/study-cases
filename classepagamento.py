class Pagamento:
    def __init__(self, valor, metodo_pagamento):
        self._valor = valor
        self._metodo_pagamento = metodo_pagamento

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser positivo")
        self._valor = valor

    @property
    def metodo_pagamento(self):
        return self._metodo_pagamento

    @metodo_pagamento.setter
    def metodo_pagamento(self, metodo):
        metodos_validos = ['cartao', 'boleto', 'paypal']
        if metodo not in metodos_validos:
            raise ValueError(f"Método de pagamento inválido. Escolha um dos seguintes: {', '.join(metodos_validos)}")
        self._metodo_pagamento = metodo


# Exemplo de uso
try:
    pagamento = Pagamento(100, 'cartao')
    print(pagamento.valor)  # 100
    print(pagamento.metodo_pagamento)  # cartao
    pagamento.valor = -50  # Levanta ValueError
except ValueError as e:
    print(e)  # "O valor do pagamento deve ser positivo"

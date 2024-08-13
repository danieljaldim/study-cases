# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor  # Atributo da instância que armazena a cor da tinta

    @property
    def cor(self):
        print('PROPERTY')  # Imprime 'PROPERTY' quando a propriedade 'cor' é acessada
        return self.cor_tinta  # Retorna o valor do atributo 'cor_tinta'

    @property
    def cor_tampa(self):
        return 123456  # Retorna um valor fixo (123456) para a propriedade 'cor_tampa'

# Criando uma instância da classe Caneta com a cor 'Azul'
caneta = Caneta('Azul')

# Acessando a propriedade 'cor' várias vezes, imprimindo 'PROPERTY' e o valor 'Azul'
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)

# Acessando a propriedade 'cor_tampa' e imprimindo o valor 123456
print(caneta.cor_tampa)

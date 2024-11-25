# Python Dunder Methods __repr__ e __str__
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Método construtor que inicializa os atributos x e y de um objeto da classe Ponto.

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'
        # Método especial que retorna uma string de representação oficial do objeto,
        # usada para depuração e logging. Aqui, retorna o nome da classe e os valores
        # dos atributos x e y.

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
        # Método especial que sobrecarrega o operador +. Permite somar dois objetos
        # da classe Ponto, retornando um novo objeto Ponto com os valores somados dos
        # atributos x e y.

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other
        # Método especial que sobrecarrega o operador >. Permite comparar dois objetos
        # da classe Ponto, retornando True se a soma dos atributos x e y do objeto
        # self for maior que a soma dos atributos x e y do objeto other.

# Bloco principal do script, executado apenas se o script for executado diretamente.
if __name__ == '__main__':
    p1 = Ponto(4, 2)  # Cria um objeto Ponto com x=4 e y=2
    p2 = Ponto(6, 4)  # Cria um objeto Ponto com x=6 e y=4
    p3 = p1 + p2      # Soma os objetos p1 e p2, resultando em um novo objeto Ponto
    print(p3)         # Imprime a representação do objeto p3
    print('P1 é maior que p2', p1 > p2)  # Compara p1 e p2, verificando se p1 é maior que p2
    print('P2 é maior que p1', p2 > p1)  # Compara p2 e p1, verificando se p2 é maior que p1

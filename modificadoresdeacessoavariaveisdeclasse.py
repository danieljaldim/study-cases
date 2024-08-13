# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial  # Importação do módulo partial, mas ele não está sendo usado no código atual.

class Foo:
    def __init__(self):
        # Atributos da classe
        self.public = 'isso é público'  # Atributo público
        self._protected = 'isso é protegido'  # Atributo protegido (indicação de que deve ser usado apenas dentro da classe ou subclasses)
        self.__exemplo = 'isso é private'  # Atributo privado (indicação de que deve ser usado apenas dentro da classe)

    def metodo_publico(self):
        # Método público (pode ser acessado de qualquer lugar)
        # self._metodo_protected()  # Comentado, mas se descomentado, chamaria o método protegido
        # print(self._protected)  # Comentado, mas se descomentado, imprimirá o atributo protegido
        print(self.__exemplo)  # Imprime o atributo privado
        self.__metodo_private()  # Chama o método privado
        return 'metodo_publico'  # Retorna uma string indicando que este é o método público

    def _metodo_protected(self):
        # Método protegido (indicativo para ser usado apenas dentro da classe ou subclasses)
        print('_metodo_protected')  # Imprime uma string indicando que este é o método protegido
        return '_metodo_protected'  # Retorna uma string indicando que este é o método protegido

    def __metodo_private(self):
        # Método privado (indicativo para ser usado apenas dentro da classe)
        print('__metodo_private')  # Imprime uma string indicando que este é o método privado
        return '__metodo_private'  # Retorna uma string indicando que este é o método privado


f = Foo()  # Cria uma instância da classe Foo
# print(f.public)  # Comentado, mas se descomentado, imprimirá o atributo público
print(f.metodo_publico())  # Chama o método público e imprime o retorno

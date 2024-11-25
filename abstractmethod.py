# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

# Importando as funcionalidades necessárias para criar métodos abstratos
from abc import ABC, abstractmethod

# Definindo uma classe abstrata que herda de ABC (Abstract Base Class)
class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    # Definindo uma propriedade abstrata com getter
    @property
    def name(self):
        return self._name

    # Definindo um setter abstrato para a propriedade name
    @name.setter
    @abstractmethod
    def name(self, name): 
        pass

# Definindo uma classe concreta que herda de AbstractFoo
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')  # Linha comentada, sem utilidade no momento

    # Implementando o setter abstrato da classe base
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

# Criando uma instância da classe concreta Foo e atribuindo o valor 'Bar' ao atributo name
foo = Foo('Bar')
# Imprimindo o valor do atributo name
print(foo.name)

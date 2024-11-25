# Variável global
contador_global = 0

# Função procedural
def calcular_soma(a, b):
    return a + b

# Função funcional
def aplicar_funcao_dupla(funcao, valor):
    return funcao(funcao(valor))

def duplicar(x):
    return x * 2

# Classe orientada a objetos
class Contador:
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1
        print(f'Contador da Instância: {self.contador}')

# Função que utiliza variável global
def incrementar_contador_global():
    global contador_global
    contador_global += 1
    print(f'Contador Global: {contador_global}')

# Uso procedural
resultado = calcular_soma(3, 5)
print(f'Soma Procedural: {resultado}')

# Uso funcional
resultado_funcional = aplicar_funcao_dupla(duplicar, 3)
print(f'Resultado Funcional: {resultado_funcional}')

# Uso orientado a objetos
contador_instancia = Contador()
contador_instancia.incrementar()

# Uso de variável global
incrementar_contador_global()
incrementar_contador_global()

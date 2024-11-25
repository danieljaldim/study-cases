# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome  # Nome do carro
        self._motor = None  # Atributo protegido para o motor do carro
        self._fabricante = None  # Atributo protegido para o fabricante do carro

    @property
    def motor(self):
        return self._motor  # Getter para o atributo motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor  # Setter para o atributo motor

    @property
    def fabricante(self):
        return self._fabricante  # Getter para o atributo fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor  # Setter para o atributo fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome  # Nome do motor


class Fabricante:
    def __init__(self, nome):
        self.nome = nome  # Nome do fabricante


# Criação de instâncias de carros, motores e fabricantes
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen  # Associando fabricante ao carro
fusca.motor = motor_1_0  # Associando motor ao carro
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)  # Saída: Fusca Volkswagen 1.0

gol = Carro('Gol')
gol.fabricante = volkswagen  # Associando fabricante ao carro
gol.motor = motor_1_0  # Associando motor ao carro
print(gol.nome, gol.fabricante.nome, gol.motor.nome)  # Saída: Gol Volkswagen 1.0

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat  # Associando fabricante ao carro
fiat_uno.motor = motor_1_0  # Associando motor ao carro
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)  # Saída: Uno Fiat 1.0

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford  # Associando fabricante ao carro
focus.motor = motor_2_0  # Associando motor ao carro
print(focus.nome, focus.fabricante.nome, focus.motor.nome)  # Saída: Focus Titanium Ford 2.0
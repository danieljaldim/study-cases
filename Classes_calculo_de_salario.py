class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_salario(self):
        return self.salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def get_salario(self):
        return self.salario + self.bonus

class Estagiario(Funcionario):
    def __init__(self, nome, salario, bolsa):
        super().__init__(nome, salario)
        self.bolsa = bolsa

    def get_salario(self):
        return self.salario + self.bolsa

# Função para calcular a média dos salários
def calcular_media_salarios(funcionarios):
    total_salario = sum(funcionario.get_salario() for funcionario in funcionarios)
    return total_salario / len(funcionarios)

# Criando instâncias de funcionários
funcionarios = [
    Funcionario('João', 3000),
    Gerente('Ana', 5000, 2000),
    Estagiario('Pedro', 1000, 500)
]

# Calculando e imprimindo a média dos salários
media_salarios = calcular_media_salarios(funcionarios)
print(f'Média dos salários: {media_salarios}')

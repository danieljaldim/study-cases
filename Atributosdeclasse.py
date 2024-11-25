# Atributos de classe
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


class Nascimento:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Pegar_Nascimento(self):
        return Nascimento.ano_atual - self.idade

z1 = Nascimento('Daniel', 20)
z2 = Nascimento('Adriana', 53)    

print(z1.Pegar_Nascimento())
print(z2.Pegar_Nascimento())

         
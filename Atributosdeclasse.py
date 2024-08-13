

class Nascimento:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Pegar_Nascimento(self):
        return Nascimento.ano_atual - self.idade

z1 = Nascimento('Daniel', 20)
z2 = Nascimento('Adriana', 43)    

print(z1.Pegar_Nascimento())
print(z2.Pegar_Nascimento())

         
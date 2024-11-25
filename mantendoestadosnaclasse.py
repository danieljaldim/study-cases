# Mantendo estados dentro da classe
# Definindo a classe Camera
class Camera:
    # Método construtor da classe Camera, inicializando nome e estado de filmagem
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando
          
    # Método para iniciar a filmagem
    def filmar(self):
        # Verifica se a câmera já está filmando
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return

        # Se não estiver filmando, começa a filmar
        print(f'{self.nome} está filmando...')
        self.filmando = True

    # Método para parar a filmagem
    def parar_filmar(self):
        # Verifica se a câmera não está filmando
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return

        # Se estiver filmando, para a filmagem
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    # Método para tirar uma fotografia
    def fotografar(self):
        # Verifica se a câmera está filmando, pois não pode fotografar enquanto filma
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        # Se não estiver filmando, tira uma fotografia
        print(f'{self.nome} está fotografando...')

# Criando instâncias da classe Camera
c1 = Camera('Canon')
c2 = Camera('Sony')

# Testando os métodos da instância c1
c1.filmar()          # Deve iniciar a filmagem
c1.filmar()          # Deve informar que já está filmando
c1.fotografar()      # Não pode fotografar enquanto está filmando
c1.parar_filmar()    # Deve parar a filmagem
c1.fotografar()      # Agora pode tirar uma fotografia

print()

# Testando os métodos da instância c2
c2.parar_filmar()    # Não está filmando, então deve informar isso
c2.filmar()          # Deve iniciar a filmagem
c2.filmar()          # Deve informar que já está filmando
c2.fotografar()      # Não pode fotografar enquanto está filmando
c2.parar_filmar()    # Deve parar a filmagem
c2.fotografar()      # Agora pode tirar uma fotografia

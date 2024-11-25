# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        # Método inicializador que define o host e inicializa user e password como None
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # Método de instância para definir o usuário
        self.user = user

    def set_password(self, password):
        # Método de instância para definir a senha
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        # Método de classe (classmethod) que cria uma instância da classe Connection
        # e define user e password
        connection = cls()  # Cria uma nova instância da classe Connection
        connection.user = user  # Define o usuário
        connection.password = password  # Define a senha
        return connection  # Retorna a instância configurada

    @staticmethod
    def log(msg):
        # Método estático (staticmethod) para registrar mensagens de log
        print('LOG:', msg)


    def connection_log(msg):
    # Função externa para registrar mensagens de log
         print('LOG:', msg)


# Cria uma instância da classe Connection com autenticação
c1 = Connection.create_with_auth('luiz', '1234')
# As duas linhas a seguir são equivalentes ao que foi feito na linha acima
# c1.set_user('luiz')
# c1.set_password('1234')

# Usa o método estático para registrar uma mensagem de log
print(Connection.log('Essa é a mensagem de log'))

# Imprime o usuário da conexão criada
print(c1.user)
# Imprime a senha da conexão criada
print(c1.password)
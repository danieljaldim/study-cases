"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
import abc  # Importa o módulo abc para criar classes e métodos abstratos

# Define a classe abstrata 'Conta'
class Conta(abc.ABC):
    # Método inicializador que recebe agência, conta e saldo
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia  # Atributo que armazena o número da agência
        self.conta = conta  # Atributo que armazena o número da conta
        self.saldo = saldo  # Atributo que armazena o saldo da conta

    # Define um método abstrato para saque, que deve ser implementado nas subclasses
    @abc.abstractmethod
    def sacar(self, valor): ...
    
    # Método para depositar um valor na conta
    def depositar(self, valor):
        self.saldo += valor  # Adiciona o valor ao saldo atual
        self.detalhes(f'(DEPÓSITO {valor})')  # Exibe detalhes da operação

    # Método para exibir os detalhes da conta e mensagem adicional
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')  # Mostra o saldo formatado com mensagem
        print('--')  # Exibe uma linha divisória

    # Método para representar o objeto como uma string
    def __repr__(self):
        class_name = type(self).__name__  # Obtém o nome da classe
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'  # Cria uma representação dos atributos
        return f'{class_name}{attrs}'  # Retorna a string final formatada


# Define a classe 'ContaPoupanca' que herda de 'Conta'
class ContaPoupanca(Conta):
    # Implementa o método de saque específico para conta poupança
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor  # Calcula o saldo após o saque

        # Verifica se o saldo após o saque é suficiente
        if valor_pos_saque >= 0:
            self.saldo -= valor  # Reduz o saldo pelo valor do saque
            self.detalhes(f'(SAQUE {valor})')  # Exibe detalhes da operação
            return self.saldo  # Retorna o saldo atualizado

        # Caso o saldo seja insuficiente
        print('Não foi possível sacar o valor desejado')  # Mensagem de erro
        self.detalhes(f'SAQUE NEGADO {valor}')  # Exibe detalhes do saque negado

# Define a classe 'ContaCorrente' que herda de 'Conta'
class ContaCorrente(Conta):
    # Método inicializador que inclui o limite
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)  # Chama o inicializador da classe 'Conta'
        self.limite = limite  # Atributo que armazena o limite da conta

    # Implementa o método de saque específico para conta corrente
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor  # Calcula o saldo após o saque
        limite_maximo = -self.limite  # Define o limite máximo que o saldo pode atingir

        # Verifica se o saldo após o saque está dentro do limite
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor  # Reduz o saldo pelo valor do saque
            self.detalhes(f'(SAQUE {valor})')  # Exibe detalhes da operação
            return self.saldo  # Retorna o saldo atualizado

        # Caso o saldo seja insuficiente
        print('Não foi possível sacar o valor desejado')  # Mensagem de erro
        print(f'Seu limite é {-self.limite:.2f}')  # Exibe o limite disponível
        self.detalhes(f'(SAQUE NEGADO {valor})')  # Exibe detalhes do saque negado
    
    # Método para representar o objeto como uma string, incluindo o limite
    def __repr__(self):
        class_name = type(self).__name__  # Obtém o nome da classe
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}), {self.limite!r})'  # Representa os atributos
        return f'{class_name}{attrs}'  # Retorna a string final formatada
        

# Executa o código de teste apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    # Cria uma instância de ContaPoupanca com agência 111 e conta 222
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)  # Tenta sacar R$1,00
    cp1.depositar(1)  # Deposita R$1,00
    cp1.sacar(1)  # Tenta sacar R$1,00 novamente
    cp1.sacar(1)  # Tenta sacar R$1,00 novamente
    print('##')  # Separador visual

    # Cria uma instância de ContaCorrente com agência 111, conta 222, saldo 0 e limite 100
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)  # Tenta sacar R$1,00
    cc1.depositar(1)  # Deposita R$1,00
    cc1.sacar(1)  # Tenta sacar R$1,00
    cc1.sacar(1)  # Tenta sacar R$1,00
    cc1.sacar(98)  # Tenta sacar R$98,00
    cc1.sacar(1)  # Tenta sacar R$1,00 (dentro do limite)
    print('##')  # Separador visual

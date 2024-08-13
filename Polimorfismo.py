# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

from abc import ABC, abstractmethod

# Classe abstrata base para diferentes tipos de notificações
class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem  # Inicializa a mensagem da notificação

    @abstractmethod
    def enviar(self) -> bool:
        # Método abstrato que deve ser implementado por subclasses
        # Retorna um valor booleano indicando se a notificação foi enviada
        pass

# Classe concreta para envio de notificações por e-mail
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        # Implementação do método abstrato 'enviar' para envio de e-mail
        print('E-mail: enviando - ', self.mensagem)
        return True  # Simula o sucesso no envio do e-mail

# Classe concreta para envio de notificações por SMS
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        # Implementação do método abstrato 'enviar' para envio de SMS
        print('SMS: enviando - ', self.mensagem)
        return False # Simula a falha no envio do SMS

# Função que envia uma notificação e imprime o resultado
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()  # Chama o método 'enviar' da notificação

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')

# Criação de uma instância de NotificacaoEmail e envio da notificação
notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

# Criação de uma instância de NotificacaoSMS e envio da notificação
notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)

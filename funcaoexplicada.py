# Função que realiza a soma de dois números
def soma(a, b):
    return a + b

# Função que realiza a subtração de dois números
def subtracao(a, b):
    return a - b

# Função que realiza a multiplicação de dois números
def multiplicacao(a, b):
    return a * b

# Função que realiza a divisão de dois números e trata a divisão por zero
def divisao(a, b):
    return a / b
try:
    divisao
except ZeroDivisionError:
    print('Erro: Divisão por zero não permitida')    

# Função principal do programa
def main():
    # Solicita ao usuário o primeiro número e converte para inteiro
    num1 = int(input("Digite o primeiro número: "))
    # Solicita ao usuário o segundo número e converte para inteiro
    num2 = int(input("Digite o segundo número: "))
    
    # Chama a função de soma com os números fornecidos e armazena o resultado
    resultado_soma = soma(num1, num2)
    # Exibe o resultado da soma
    print(f"Soma: {resultado_soma}")
    
    # Chama a função de subtração com os números fornecidos e armazena o resultado
    resultado_subtracao = subtracao(num1, num2)
    # Exibe o resultado da subtração
    print(f"Subtração: {resultado_subtracao}")

    # Chama a função de multiplicação com os números fornecidos e armazena o resultado
    resultado_multiplicacao = multiplicacao(num1, num2)
    # Exibe o resultado da multiplicação
    print(f'Multiplicação: {resultado_multiplicacao}')

    # Chama a função de divisão com os números fornecido e armazena o resultado
    resultado_divisao = divisao(num1, num2)
    # Exibe o resultado da divisão e trata as excessões por zero
    print(f'Divisão: {resultado_divisao}')

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Chama a função principal do programa
    main()
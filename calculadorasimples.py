def calcular(numero_1, numero_2, operacao):
    if operacao == '+':
        return numero_1 + numero_2
    elif operacao == '-':
        return numero_1 - numero_2
    elif operacao == '*':
        return numero_1 * numero_2
    elif operacao == '/':
        try:
            return numero_1 / numero_2
        except ZeroDivisionError:
            return 'Erro: Divisão por zero não é permitida'
    else:
        return 'Erro: Operação inválida'

try:
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite mais um número: '))
    operacao = input('Escolha uma operação (+, -, *, /): ')
    
    resultado = calcular(numero_1, numero_2, operacao)
    print(f'O resultado da operação é: {resultado}')

except ValueError:
    print('Erro: Por favor, digite apenas números inteiros')


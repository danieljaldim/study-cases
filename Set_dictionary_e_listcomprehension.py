# List Comprehension é útil quando se deseja criar uma nova lista aplicando alguma transformação ou filtragem nos elementos de uma coleção existente.

# [expressao for item in iterable if condicao]
# expressao: A expressão que calcula os elementos da nova lista.
# item: O item corrente do iterable.
# iterable: Uma coleção de elementos sobre a qual a compreensão está sendo feita.
# condicao (opcional): Um filtro que seleciona quais elementos do iterable devem ser incluídos na nova lista.

# Lista de quadrados de números pares de 0 a 9
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  

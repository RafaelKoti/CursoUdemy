from sys import getsizeof

# Generator Expressions
    # Uma forma mais rápida para Listas, dicionários e etc
    # Menos memória alocada
    # Valores em bytes

numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
print(getsizeof(numeros))

print('====')

numeros = (x * 10 for x in range(1000000))
print(type(numeros))
print(getsizeof(numeros))
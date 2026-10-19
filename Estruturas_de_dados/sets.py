# Sets (listas)
# Similares a listas
# Evitam itens duplicados e não utilizam index

lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

numeros1 = set(lista1)
numeros2 = set(lista2)

print(numeros1 | numeros2) # Union
print(numeros1 - numeros2) # Difference
print(numeros1 ^ numeros2) # Simemetric Difference
print(numeros1 & numeros2) # And

print(len(numeros1))
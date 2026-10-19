# Sets (listas)
# Similares a listas
# Evitam itens duplicados e não utilizam index
# Sets com Funções

lista1 = [1, 2, 3, 4, 5, 6]
set1 = {1, 2, 3, 4, 5, 6, 1, 2}
set1.add(7)
set1.update([6, 7, 8, 9, 10])
set1.remove(10)

print(lista1)
print(set1)

print(type(lista1))
print(type(set1))
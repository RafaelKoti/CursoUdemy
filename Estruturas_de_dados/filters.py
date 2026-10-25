# Filter Function
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, filtrando os itens. (list, tuple, dic etc.)

valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))
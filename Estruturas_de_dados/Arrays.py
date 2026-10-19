# Array (Matriz)
# São Similares a listas
# Mlehor Performace

from array import array

Letras = ["A", "B", "C", "D"]
numeros_inteiros = [10, 20, 30, 40]
numeros_float = [1.2, 2.2, 3.2]

print(Letras)
print(numeros_inteiros)
print(numeros_float)

Letras = array("u", ["A", "B", "C", "D"])
numeros_inteiros = array("i", [10, 20, 30, 40])
numeros_float_ = array("f", [1.2, 2.2, 3.2])

print(Letras)
print(numeros_inteiros)
print(numeros_float)

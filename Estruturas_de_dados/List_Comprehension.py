# List Comprehension
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# frutas2 = []

# for iten in frutas1:
#     if 'n' in item:[cite: 6]
#         frutas2.append(iten)[cite: 6]

frutas2 = [iten for iten in frutas1 if 'k' in iten]

print(frutas2)
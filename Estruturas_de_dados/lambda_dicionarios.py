# Lambda Function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'

"""def somar(x):
    return x + 10

print(somar(2))"""


#somar10 = lambda x, y: x + y + 10

#print(somar10(2, 2))

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4


print(somar(2))
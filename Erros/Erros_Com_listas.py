# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro


try:
    lista = ['a','b','c']
    print(lista[3])
except IndexError:
    print("Ta errado aí irmão")
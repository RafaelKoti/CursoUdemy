# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(type(valor))
except ValueError:
    print("Tenta de novo ai irmão kkkk, digita só número")
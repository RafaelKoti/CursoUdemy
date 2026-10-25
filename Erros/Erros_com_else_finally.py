# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro


try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Tenta de novo ai irmão kkkk, digita só número")
finally:
    print("Código OK")

""" else:
    print("O cara digitou um valor correto")
    resultado = valor * 2
    print(resultado) """
    
print("Código com mais linhas abaixo")
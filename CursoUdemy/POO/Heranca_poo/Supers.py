# Sistema de Escola

class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status


    def Apresentar(self):
        print(f"Meu nome é {self.nome}")

    def VerificarStatus(self):
        print(f"Status: {"ATIVO" if self.status else "Inativo"}")


class Aluno(Escola):
    def __init__(self, nome, idade, status, ano):
        super().__init__(nome, idade, status)
        self.ano = ano

    def Apresentar(self):
        super().Apresentar()
        print(f"Tenho {self.idade} e estou no {self.ano} da Faculdade")

class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia


class Assistente(Escola):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco   

    def Apresentar(self):
        super().Apresentar()
        print("Eu sou uma Asistente da Faculdade")

Aluno1 = Aluno("Rafael Koti", 19, True, "4ª Semestre")
Professor1 = Professor("Anderson", 45, True, "POO")
Assistente1 = Assistente("Cris", 52, False, "Bloco A")

Aluno1.Apresentar()
Assistente1.Apresentar()
Assistente1.VerificarStatus()
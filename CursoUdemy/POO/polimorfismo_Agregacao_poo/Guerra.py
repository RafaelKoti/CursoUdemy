# Polimorfismo

class Personagens():
    def Falar(self):
        print("Eu sou um Personagem")


class Guerreiro(Personagens):
    def Falar(Self):
        print("Eu sou um Guerreiro Foda :)")

class Mago(Personagens):
    def Falar(Self):
        print("Eu sou um Mago Maneiro :)")

class Arqueiro(Personagens):
    def Falar(Self):
        print("Eu sou um Arqueiro legal :)")

## Criando os objetos:


personagens = [Guerreiro(), Mago(), Arqueiro()]

for p in personagens:
    p.Falar()
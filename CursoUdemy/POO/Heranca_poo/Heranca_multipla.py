# Herança Multipla

# Classe Avô

class Animal:
    def __init__(self, nome):
        self.nome = nome

## Classes Pai
class Predador(Animal):
    def cacando(self):
        print(f"O {self.nome} está caçando!")

class Presa(Animal):
    def fugindo(self):
        print(f"O {self.nome} está sendo caçado!")


## Classes Filhas
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Predador, Presa):
    pass

coelho1 = Coelho("Coelhin")
Tigre1 = Tigre("Tigrinho")
golfinho1 = Golfinho("Golfinho")

coelho1.fugindo()
Tigre1.cacando()
golfinho1.cacando()
class Animal:
    def __init__(self, especie, nome, cor):
        self.especie = especie
        self.nome = nome
        self.cor = cor

    def apresentar(self):
        print(f"Espécie: {self.especie}, chamado {self.nome} e ele tem pelagem {self.cor}.")


class Gato(Animal):
    def EmitirSom(self):
        print("O Gato fez: Miarr")

class Cachorro(Animal):
    def EmitirSom(self):
        print("Cachorro falou: Osvaldo, então podemos beber")

class Elefante(Animal):
    def EmitirSom(self):
        print("Elefante faz que som? 🤔")


gato1 = Gato("Persa", "Joelson", "Branca")
gato1.apresentar()
gato1.EmitirSom()
print("\n")

cachorro1 = Cachorro("BullDog", "Edinilson", "Preto") #
cachorro1.apresentar()
cachorro1.EmitirSom()
print("\n")

elefante1 = Elefante("Asiático", "Jobinson", "Cinza") 
elefante1.apresentar()
elefante1.EmitirSom()

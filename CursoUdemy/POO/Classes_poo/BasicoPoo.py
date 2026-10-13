## Classes, Construtores e Métodos

class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def MostrarCor(self):
        print(f"A cor da casa é roxa {self.cor}")

    def MostrarQuartos(self):
        print(f"Essa casa tem {self.quartos} quartos")

    def MostrarBanheiros(self):
        print(f"E esta casa tem {self.banheiros} banheiros")

    def AdicionarQuartos(self):
        self.quartos += 2
        print(f"Esta casa tem {self.quartos} quartos")

    def PintandoCasa(self, Nova_Cor_Casa):
        print(f"A sua casa tinha a cor {self.cor}, porém estamos pintando de {Nova_Cor_Casa}...")

PrimeiraCasa = Casa("Roxin maneiro", 4, 2)
SegundaCasa = Casa("Verde maneirin", 2, 4)


print("\nPrimeira casa: ")
PrimeiraCasa.MostrarCor()
PrimeiraCasa.MostrarQuartos()
PrimeiraCasa.MostrarBanheiros()
PrimeiraCasa.AdicionarQuartos()
PrimeiraCasa.PintandoCasa("Vermelho PT")

print("\n Segunda Casa: ")
SegundaCasa.MostrarCor()
SegundaCasa.MostrarQuartos()
SegundaCasa.MostrarBanheiros()
SegundaCasa.AdicionarQuartos()
SegundaCasa.PintandoCasa("Azul Bolsonaro")
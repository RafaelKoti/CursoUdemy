class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
        self.ligado = True
        self.seta = None

    def MostrarInformacoes(self):
        print(f"A cor do carro é {self.cor} e seu ano é de {self.ano}")

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("Ligamos o carro")

        else:
            print("O carro já está ligado no 220 KKKKKK")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Desligamos o carro KKKKKKK")

        else:
            print("O carro já estava desligado")

    def LigarSeta(self, direcao):
        if not self.ligado:
            print("Liga o carro primeiro seu animal >:)")
            return

        self.seta = direcao
        print(f"A Seta foi ligada para a {self.seta}")

Carro1 = Carro("Preto", 2025)
Carro1.MostrarInformacoes()
Carro1.ligar()
Carro1.LigarSeta("Direita")
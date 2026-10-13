class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Apresentar(self):
        print(f"Olá, o meu nome é {self.nome} e eu tenho {self.idade} anos de idade")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo ):
        super().__init__(nome, idade)
        self.cargo = cargo

    def Trabalhar(self):
        print(f"Nome: {self.nome}, e está trabalhando como {self.cargo}")
  
class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def Comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f"Olá {self.nome}, A sua compra de {valor_compra} foi aprovada, seu novo saldo atual é de {self.saldo}")

        else:
            print(f"Olá {self.nome}, o seu saldo é insuficiente, e sua compra foi negada")


Funcionario1 = Funcionario("James", 45, "Analista de Sitemas")
Funcionario1.Apresentar()

Cliente1 = Cliente("Joelson", 23, 250)
Cliente2 = Cliente("Maria", 43, 12)

Cliente1.Apresentar()
Cliente2.Apresentar()

Cliente1.Comprar(23)
Cliente2.Comprar(76)
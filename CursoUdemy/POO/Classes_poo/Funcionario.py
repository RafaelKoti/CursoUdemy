class Funcionario:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def MostrarInformacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Cargo: {self.cargo}")

    def Promover(self, novo_cargo):
        print(f"{self.nome} foi promovido(a) a nova função de {novo_cargo}")

    def AtualizarIdade(self, nova_idade):
        if nova_idade > self.idade:
            print(f"Atualizando a idade de {self.idade} para {nova_idade}")

        else:
            print("A nova idade tem que ser maior que a idade atual")

colaborador1 = Funcionario("Ana", 40, "Assistente Administrativo Junior")
Colaborador2 = Funcionario("Pedro", 23, "Desenvolvedor Junior")

colaborador1.MostrarInformacoes()
colaborador1.Promover("Assistente Administrativo Sênior")
colaborador1.AtualizarIdade(41)
## Agregação


class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []

    def AdicionarMotor(self, motor):
        self.motores.append(motor)

    def ListarMotores(self):
        for motor in self.motores:
            print(f"Marca do Motor: {motor.marca} - {motor.potencia} Cavalos de Potência")

## Criando os motores (Objetos)

Motor_V6 = Motor("Ford", 450)
Motor_V8 = Motor("Ferrari", 650)
Motor_V12 = Motor("Honda", 700)

## Criando o carro e adicionando o motor a ele
Carro1 = Carro()
Carro1.AdicionarMotor(Motor_V6)
Carro1.AdicionarMotor(Motor_V8)
Carro1.AdicionarMotor(Motor_V12)

## Listando os motores

Carro1.ListarMotores()
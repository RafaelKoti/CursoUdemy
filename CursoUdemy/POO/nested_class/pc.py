# Criando a Classe Main

# Nested Class pode ser como com condomínio, onde terá vários apartamentos

# Todos existem em um contexto só, sem a classe Main (Computador) GPU e CPU
# só exitem dentro do Computador, e não funcionam sem ele

class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria, cpu_nome, cpu_cores, cpu_clock):
        self.modelo = modelo
        self.gpu_memoria = gpu_memoria
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)

    
    def MostrarConfiguracao(self):
        print(f"Computador: {self.modelo}")
        self.gpu.Mostrar_Gpu()
        self.cpu.Mostrar_Cpu()

    class GPU: # Nested Class
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb

        def Mostrar_Gpu(self):
            print(f"GPU: {self.nome} - {self.memoria_gb}")

    class CPU: # Nested Class
        def __init__(self, nome, cores, clock_ghz):
            self.nome = nome
            self.cores = cores
            self.clock_ghz = clock_ghz

        def Mostrar_Cpu(self):
            print(f"CPU: {self.nome} - {self.cores} núcleos e possuí {self.clock_ghz} GHz")

# Parte de Utilzação

pc1 = Computador("PC de Mesa", "RX 7800XT", "16gb", "Ryzen 7 9800x", 16, 6.7)
pc1.MostrarConfiguracao()

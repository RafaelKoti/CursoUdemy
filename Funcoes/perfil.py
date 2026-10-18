def criar_perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


criar_perfil(nome ="Beatriz", cargo ="Engenheira", cidade ="Lisboa")   
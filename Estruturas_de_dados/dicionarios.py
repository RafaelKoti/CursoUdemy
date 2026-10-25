# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...

aluno = {
    'nome': 'Ana', 
    'idade': 16, 
    'nota_final': 'A', 
    'aprovação': True, 
    'Matérias': ["Física", "Matemática", "Inglês"]
}

aluno.update({"Rua": "Casa dos Coqueiros"})
del aluno["Rua"]

for keys, values in aluno.items():
    print(keys,":", values)
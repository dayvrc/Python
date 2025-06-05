import pandas as pd

nome_arquivo = r'Estacio\RAD\notas.csv'
dados_alunos = pd.read_csv(nome_arquivo, delimiter=';')

dados_alunos['Media'] = dados_alunos[['Nota1','Nota2','Nota3']].mean(axis=1)

alunos_aprovados = dados_alunos[dados_alunos['Media']>=7]

print("Alunos aprovados:")
print(alunos_aprovados[['Nome','Media']].to_string(index=False))


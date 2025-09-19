# Create a program that reads a student’s name and average grade, also storing the status in a dictionary. In the end, display the contents of the structure on the screen (failed or passed).

dicionario = {}
dicionario ['nome'] = str(input('Qual o nome do aluno? '))
dicionario ['média'] = float(input(f'Qual a média do {dicionario["nome"]} ? '))
if dicionario['média'] >= 7.50:
    dicionario['situação'] = 'Aprovado'
elif 5 <= dicionario['média'] < 7.50:
    dicionario['situação'] = 'Recuperação'
else: 
    dicionario['situação'] = 'Reprovado'

print(f' O aluno {dicionario ["nome"]} foi {dicionario["situação"]}')
# Create a program that reads the name and two grades of several students and stores everything in a composite list. At the end, show a report card containing the average of each one and allow the user to display the grades of each student individually. Type 999 to stop.

lista = list()
pergunta = 'S'
n_alunos = 0
while pergunta == 'S':
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    nota1 = float(input('Digite a nota da primeira prova: '))
    nota2 = float(input('Digite a nota da segunda prova; '))
    lista.append([nome, nota1, nota2])
    n_alunos += 1
    pergunta = str(input('Deseja continuar? Sim ou não?')).strip().upper()[0]
    if pergunta not in 'SN':
        pergunta = str(input('Não entendi. Sim ou não?')).strip().upper()[0] 
    if pergunta == 'N':
        break
for c in range(n_alunos):
    print (f'Aluno {lista[c][0]}: {lista[c][1]} | {lista[c][2]} ')
aluno = str(input('De quem você quer saber a nota? [999 para parar]')).strip().capitalize()
encontrado = False
for p in range(len(lista)):
    if lista[p][0] == aluno:
        print(f'As notas do {aluno} foram {lista[p][1]} e {lista[p][2]}')
        encontrado = True
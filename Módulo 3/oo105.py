# Create a program with a function called grades() that can receive multiple student grades and will return a dictionary with the following information:

def notas():
    boletim = dict()
    listanota = list()
    resp = 'S'
    c = 0
    while resp == 'S':
        nome = str(input('Nome do aluno: ')).strip().capitalize()
        nota = float(input(f'Qual a nota do aluno {nome} ? '))
        boletim [nome] = nota

        resp = str(input('Quer continuar?')).strip().upper()[0]
        if resp not in 'SN':
            resp = str(input('Não entendi. Quer continuar?')).strip().upper()[0]
        if resp == 'N':
            break
 
    media = sum(boletim.values())/len(boletim)
    print(f'Foram lidas {len(boletim)}')
    print(f' A maior nota é {max(boletim.values())} e a menor é {min(boletim.values())}')
    print(f'A media da turma é {media:.2f}')
            
    resp_situaçao = str(input('Quer saber a situação de qual aluno?')).strip().capitalize()
    if resp_situaçao in boletim:
        nota = boletim[resp_situaçao]
        if  nota >= 7:
            print('O aluno foi APROVADO')
        if 5 >= nota < 7: 
            print('O aluno está de recuperação')
        else:
            print(f' O aluno foi REPROVADO')
        print(f'O aluno {nome} tirou {nota}.')
    else:
        print('Aluno não encontrado!')
notas()
            


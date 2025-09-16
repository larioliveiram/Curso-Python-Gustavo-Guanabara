# Create a program that reads the age and gender of several people. After each person is registered, the program should ask if the user wants to continue or not. At the end, display:
# A) How many people are over 18 years old.
# B) How many men were registered.
# C) How many women are under 20 years old.

idade = total = maioridade = mulher = homem = 0
sexo = pergunta = ''
while True:
    if pergunta in 'S':
        idade = int(input('Qual a sua idade?'))
        sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()[0]
        pergunta = str(input('Quer continuar?')).strip().upper()[0]
        total += 1
        if sexo not in 'MF':
            print ('Sexo errado. Feminino ou Masculino?')
            sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()[0]
        if idade >= 18:
            maioridade += 1
        if sexo in 'M':
            homem += 1
        if sexo in 'F' and idade < 20:
            mulher += 1
    elif pergunta in 'N':
        print(f''' Foram cadastradas {total} pessoas sendo 
              {maioridade} com mais de 18 anos
               {homem} do sexo masculino
               {mulher} mulheres com menos de 20 anos''')
        break
    else:
        print('Erro. Digite sim ou não.')
        pergunta = str(input('Quer continuar?')).strip().upper()[0]

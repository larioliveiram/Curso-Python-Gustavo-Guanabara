#Develop a program that reads the name, age, and gender of 4 people. At the end of the program, display:
# The average age of the group
# The name of the oldest man
# How many women are under 20 years old

soma = 0
média = 0
maioridade = 0
nomevelho = ''
totmulher = 0
for c in range (1,5):
    print ((20*'-') + f' {c}ª PESSOA ' + (20*'-'))
    nome = str(input('Qual o seu nome?'))
    idade = int(input('Qual a sua idade?'))
    sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()
    soma = soma + idade 
    if c == 1 and sexo == 'M':
        maioridade = idade 
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade 
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher = totmulher + 1
mediaidade = soma / 4
print(f' A média de idade do grupo é {mediaidade:.0f} anos')
print (f'O homem mais velho se chama {nomevelho} e tem {maioridade} anos')
print (f' No grupo tem {totmulher} mulheres com menos de 20 anos')
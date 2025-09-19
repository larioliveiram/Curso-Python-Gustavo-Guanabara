# Create a program that reads the name, gender, and age of several people, storing each person’s data in a dictionary and all dictionaries in a list. At the end, display:
# A) How many people were registered
# B) The average age of the group
# C) A list of all the women
# D) A list of all the people whose age is above the average.

pergunta = 'S'
pessoas = list()
somaidade =  0
listamulher = list()
while pergunta == 'S':
    dicionario = {}
    dicionario ['nome'] = str(input('Qual o seu nome? ')).strip().capitalize()
    dicionario ['sexo'] = str(input(' Qual o sexo? [F/M]')).strip().upper()[0]
    dicionario ['idade'] = int(input(' Qual a sua idade? '))
    
    pessoas.append(dicionario.copy())
    somaidade += dicionario ['idade']
    
    pergunta = str(input('Quer continuar?')).strip().upper()[0]
    if pergunta not in 'SN':
        pergunta = str(input('Não entendi. Quer continuar?')).strip().upper()[0]

media = somaidade/len(pessoas)
listamulher = [p['nome'] for p in pessoas if p['sexo'] == 'F' ]
maisvelhas = [p['nome'] for p in pessoas if p['idade'] > media]

print(f' Foram cadastras {len(pessoas)} pessoas.')
print(f' A média de idade é {media:.0f}')
print(f'As mulheres são: {listamulher}')
print(f' As pessoas mais velhas que a média são: {maisvelhas}')
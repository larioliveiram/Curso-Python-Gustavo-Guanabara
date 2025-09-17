# Write a program that reads the name and weight of several people, storing everything in a list. At the end, display:
# A) How many people were registered
# B) A list of the heaviest people
# C) A list of the lightest people

pergunta = 'S'
c = 1
pessoas = list()
final = list()
while pergunta == 'S':
    nome = str(input(f'Qual o nome da {c}ª pessoa?'))
    peso = float(input(f'Qual o peso da {c}ª pessoa?'))
    pessoas.append([nome,peso])
    c += 1
    pergunta = str(input('Quer continuar?')).strip().upper()[0]
    
    if pergunta not in 'SN':
        pergunta = str(input('Não entendi. Sim ou Não? ')).strip().upper()[0]
print(pessoas)
final.append(pessoas[:])
final.sort(key=lambda x: x[1])
print(f' Foram cadastradas {c-1} pessoas.')
print(f' As pessoas mais pesadas são {final[-1][0]} com {final[-1][1]}Kg e as mais leves {final[-1][0]} com {final[-1][1]}')



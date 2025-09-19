# Create a program where 4 players roll a die and get random results. Store these results in a dictionary. At the end, sort this dictionary, knowing that the winner is the one who rolled the highest number. 

from random import randint
from time import sleep

jogador = []
for j in range(0,4):
    nome = str(input(f'Digite o nome do jogador {j+1}: '))
    n = randint(1,6)
    jogador.append({'nome': nome, 'n': n} )

total = sorted(jogador, key=lambda x: x ['n'], reverse=True)

print(f"{'Ranking Jogadores':^30}")
sleep(1)
for i, jogadores in enumerate(total, 1):
    print(f"{i}º lugar: {jogadores['nome']} tirou {jogadores['n']}")


# Create a program that lets the computer play Rock-Paper-Scissors with you.
# The game should ask for your move and the computer's move, then display the result.
# The possible moves are: Rock, Paper, and Scissors.

from random import randint
from time import sleep
print('Vamos jogar Jokenpô!')
comp = randint(1,3)
print('''Escolha uma opção:
               1 - Pedra 
               2 - Papel 
               3 - Tesoura''')
eu = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
if comp == eu:
    print(f'Eu escolhi {comp} e você escolheu {eu}. Deu empate! Vamos tentar de novo!')
elif (comp == 1 and eu == 3) or (comp == 2 and eu == 1) or (comp == 3 and eu == 2):
    print (f' Eu escolhi {comp} e você escolheu {eu}. Eu ganhei!') 
else:
    print(f' Eu escolhi {comp} e você escolheu {eu}. Você ganhou!')
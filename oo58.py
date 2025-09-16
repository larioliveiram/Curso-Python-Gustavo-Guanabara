# Improve the game from Challenge 28, where the computer "thinks" of a number between 0 and 10. Now, the player will keep guessing until they get it right, showing at the end how many attempts were needed to win.

import random
from time import sleep 
n = random.randint(0,10)
palpites = 0
nunusuario = -1
resp = str(input('Vamos brincar de advinhar o número que estou pensando?')).strip().upper()
if resp == 'SIM' or resp == 'S':
    print('boa escolha, vamos começar!')
    sleep(1)
    while nunusuario != n:
        nunusuario = int(input('Diga um número de 0 a 10: '))
        if nunusuario == n: 
            print ('Parabéns! Você acertou em cheio!')
            palpites += 1
        if nunusuario < 0 or nunusuario > 10: 
            print(' Eu disse de 0 a 10, vamos tentar novamente!')
        elif nunusuario != n: 
            print('Errado, tente de novo')
            palpites += 1
    print(f' Voce precisou de {palpites} palpites para acertar')
else:
    print('Que pena, vamos jogar outra hora!')
        
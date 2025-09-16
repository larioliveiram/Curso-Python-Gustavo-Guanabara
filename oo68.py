# Write a program that plays even or odd with the computer. The game will only stop when the player loses, showing the total number of consecutive wins achieved at the end of the game.

from random import randint
from time import sleep
com = str(input('Vamos jogar par ou impar?')).strip().upper()[0]
if com in 'S':
    print('Bora jogar!')
    sleep (1)
    v = njogador = ncomputador =  0
    while True:
        jogador = str(input(' Você quer ser Par ou Impar?')).strip().upper()[0]
        print ('Certo, eu sou impar' if jogador == 'P' else 'Vou ser Par então' )
        ncomputador = randint(0,10)
        njogador = int(input('Digite um valor de 0 a 10: ')) 
        sleep(1) 
        if (ncomputador + njogador)%2 == 0 and jogador == 'P':
            print (f'Pensei no número {ncomputador} que somados à {njogador} da {ncomputador + njogador} que é par. Você ganhou!')
            v += 1
        elif (ncomputador + njogador)%2 == 0 and jogador == 'I':
            print (f'Pensei no número {ncomputador} que somados à {njogador} da {ncomputador + njogador} que é par. Você perdeu!')
            break
        elif (ncomputador + njogador)%2 != 0 and jogador in 'P':
            print (f'Pensei no número {ncomputador} que somados à {njogador} da {ncomputador + njogador} que é ímpar. Você perdeu')
            break
        elif (ncomputador + njogador)%2 != 0 and jogador in 'I':
            print (f'Pensei no número {ncomputador} que somados à {njogador} da {ncomputador + njogador} que é impar. Você ganhou!')
            v += 1
    print (f'Foram {v} vitórias! Parabéns')     
else:
    print('Que pena, até a próxima!')
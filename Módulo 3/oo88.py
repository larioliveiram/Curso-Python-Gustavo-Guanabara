# Write a program that helps a MEGA SENA player generate lottery picks. The program should ask how many games will be generated and then randomly draw 6 numbers between 1 and 60 for each game, storing everything in a nested list.

from random import randint
jogos = int(input('Quantos jogos você precisa? '))
lista = list()
n = 1
while n <= jogos:
    for i in range(6): 
        lista.append(randint(1,60))
    lista.sort()
    print (f' O jogo {n} será: {lista}')
    n += 1
    lista.clear()
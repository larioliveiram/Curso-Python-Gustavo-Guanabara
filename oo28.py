#Escreva um programa que faça o computador "pensa" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep #importa o módulo time que permite controle de tempo
n = random.randint(0,5) #gera um número aleatório entre 0 e 5
print('Vou pensar em um número, tente adivinhar')
nusuario = int(input('Diga um número de 0 a 5:'))
print ('calma que estou pensando...')
sleep (4) #indica os segundos que o programa vai esperar para continuar
if nusuario == n:
    print('Parabéns, você acertou em cheio!')
if nusuario <0 or nusuario >5:
    print('Eu disse de 0 a 5, vamos tentar novamante!')
else:
    print(f'Ganhei! Eu pensei no número {n}. Tente novamente!')
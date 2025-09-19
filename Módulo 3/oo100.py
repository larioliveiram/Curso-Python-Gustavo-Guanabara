# Create a program that has a list called numbers and two functions called draw() and sumEven(). The first function will randomly select 5 numbers and place them in the list, and the second function will display the sum of all even values drawn by the previous fun

from random import randint
numeros = []

def sorteio():
    for n in range(0,5):
        numeros.append(randint(1,50))

def somapar():
    soma = 0
    for n in  numeros:
        if n % 2 == 0:
            soma += n
    print(f' Somando os valores pares de {numeros}, temos {soma}')

sorteio()
somapar()


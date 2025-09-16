# Create a program that generates five random numbers and stores them in a tuple. After that, display the list of generated numbers and also indicate the smallest and largest values in the tuple.

from random import randint
numeros_sorteados = tuple(randint(1,100) for _ in range(5)) #sortei um numero de 1 a 100, faça isso 5x
print(f'Os números sorteados foram {numeros_sorteados}, sendo o maior {max(numeros_sorteados)} e o menor {min(numeros_sorteados)}')
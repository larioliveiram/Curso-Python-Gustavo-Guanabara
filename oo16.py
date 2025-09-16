# Create a program that reads any real number from the keyboard and displays its integer part.

from math import trunc
n = float(input('Digite um número:'))
print(f'O número {n} tem a parte inteira {trunc(n)}')
print(f'Outra forma de dar o mesmo resultado é {int(n)}')



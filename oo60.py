# Write a program that reads any number and displays its factorial. Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

from time import sleep
n = int (input('Digite um númaro para calcular seu fatorial: '))
f = 1
print (f'Calculando {n}! =', end=' ')
sleep (1)
while n >0:
    print (f'{n} x' if n > 1 else f'{n} = ', end=' ')
    f *= n
    n -= 1
    sleep (1)
    print (f'{f}')
 

# Write a program that reads the lengths of the opposite and adjacent sides of a right triangle, calculates, and displays the length of the hypotenuse.

import math
cato = float(input('Qual o comprimento do cateto oposto?'))
cata = float(input('Qual o comprimento do cateto adjacente?'))
print(f'Sendo cateto oposto {cato} e cateto adjacente {cata} a hipotenusa desse triangulo é {math.sqrt(cata**2 + cato**2):.2f}')
print(f' Otra forma de medir é {(cata**2 + cato**2)**(1/2)}')
print(f' Utilizando o math de outra maneira {math.hypot(cata,cato):.2f}')




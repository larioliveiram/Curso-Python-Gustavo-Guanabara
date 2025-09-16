# Write a program that reads any angle and displays its sine, cosine, and tangent values.

import math
â = float (input('Qual o valor do ângulo?'))
print(f'Certo, com um ângulo de {â:.0f} o cosseno desse triângulo é {math.cos(math.radians(â)):.2f} o seno é {math.sin(math.radians(â)):.2f} e a tangente é {math.tan(math.radians(â)):.2f}')
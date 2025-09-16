# Redo triangle challenge 35, but now using the logical "and" operator to check if the segments can form a triangle. The program should read the lengths of the three segments and inform whether they can form a triangle or not. If they can, indicate which type of triangle will be formed: equilateral, isosceles, or scalene.

r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1) and r1 == r2 == r3:
    print (' As retas formam um triângulo equilátero!')
elif (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1) and (r1 == r2 or r1 == r3 or r2 == r3):
    print (' As retas formam um triângulo isósceles!')
elif (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print (' As retas formam um triângulo escaleno!')
else:
    print (' As retas não formam um triângulo!')

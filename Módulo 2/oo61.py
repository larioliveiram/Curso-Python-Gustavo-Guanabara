# Redo Challenge 51, reading the first term and the common difference of an arithmetic progression, displaying the first 10 terms of the progression using a while loop.

a1 = int(input('Digite o primeiro número: '))
r = int(input('Digite a razão: '))
c = 0
while c <= 10:
    print (f'{a1 + c*r} ', end='  ')
    c += 1


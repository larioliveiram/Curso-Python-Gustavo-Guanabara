# Develop a program that reads the first term and the common difference of an arithmetic progression. At the end, display the first 10 terms of this progression.

a1 = int(input('Digite o primeiro número:'))
r = int (input('Digite a razão:'))
for c in range(0,10):
    print(a1 + c*r, end=' > ')
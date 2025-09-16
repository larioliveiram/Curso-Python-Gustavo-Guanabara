# Write a program that reads an integer and tells whether it is a prime number or not.

n = int(input('Digite um número:'))
tot = 0 # total vai começar com zero
for c in range (1, n+1): #contador que vai de 1 até o numero digitado +1 pq o ultimo n não é contado
    if n%c == 0: # o n tem que ser divisvel por c
       tot = tot + 1 # toda vez que o numero for divisivel por c, o total vai aumentar 1
print (f' O número {n} foi divisivel {tot} vezes')
if tot == 2 : # se no total ele foi dividido por 1 e ele meso, ou seja, 2 vezes
    print ('E por isso ele é primo')
else:
    print ('E por isso ele não é primo')


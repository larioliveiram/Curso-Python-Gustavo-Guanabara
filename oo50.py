# Develop a program that reads six integers and displays the sum of only those that are even. If the entered value is odd, disregard it.

soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um número:'))
    if n%2 == 0:
        cont += 1
        soma += n 
print (f' A soma dos {cont} números pares é {soma}')
  
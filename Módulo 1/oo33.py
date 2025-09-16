# Write a program that reads three numbers and displays which one is the largest and which one is the smallest.


n1 = float(input(' Digite o primeiro número:'))
n2 = float(input(' Digite o segundo número:'))
n3 = float(input(' Digite o terceiro número:'))
maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
elif n2>n1 and n2>n3:
    maior = n2
# Calculating the smallest number:
menor = n1
if n2<n1 and n2<n3:
    menor=n2
elif n3<n1 and n3<n2:
    menor=n3
print(f'O maior número é {maior} e o menor é {menor}')
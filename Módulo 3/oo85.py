# Write a program where the user can input seven numbers and store them in a single list, keeping even and odd numbers separate. At the end, display the even and odd numbers in ascending order.

par = list()
impar = list()
lista = (par, impar)
for c in range (1,8):
    n = int(input(f'Digite o valor {c} valor'))
    if n % 2 == 0:
        par.append(n)
    else: 
        impar.append(n)
print(lista)
impar.sort()
par.sort()
print(f'Números pares são {par} e impares {impar}')
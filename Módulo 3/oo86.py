# Create a program that generates a 3x3 matrix and fills it with values read from the keyboard. At the end, display the matrix on the screen with proper formatting.

lista = list()
for c in range (0,9):
    n = input('Digite um número: ')
    lista.append(n)
print(f'| {lista[0]} | {lista[1]} | {lista[2]} |')
print(f'| {lista[3]} | {lista[4]} | {lista[5]} |')
print(f'| {lista[6]} | {lista[7]} | {lista[8]} |')
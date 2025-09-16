# Redo challenge 09, displaying the multiplication table of a number chosen by the user, but now using a for loop.

n = int(input('Digite um número:'))
for c in range (0,10):
    print(f'{n} x {c+1} = {n*(c+1)}')
    
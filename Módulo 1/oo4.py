# Write a program that reads input from the keyboard and displays its primitive type along with all possible information about it.

n1 = (input('Digite algo'))
print(' O tipo primitivo é:', type(n1))
print('Só tem espaços', n1.isspace())
print('É alfabético?', n1.isalnum())
print('É um número?', n1.isnumeric())
print('Esta em letra maiuscula?', n1.isupper())
print('Esta em letra minuscula?', n1.islower())
print('Esta capitalizada?', n1.istitle())


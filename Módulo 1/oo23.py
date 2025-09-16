# Write a program that reads a number from 0 to 9999 and displays the units, tens, hundreds, and thousands

cont = 0
numero = input('Digite um numero de 0 a 9999').zfill(4)
print (f'unidade: {numero[3]}') 
print(f'dezena: {numero[2]}')
print(f'centena: {numero[1]}')
print(f'milha: {numero[0]}') 

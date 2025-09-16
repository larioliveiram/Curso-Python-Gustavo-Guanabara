# Write a program that calculates the sum of all odd numbers that are multiples of three within the range from 1 to 500

soma = 0
for c in range (1, 501, 2): 
    if c % 3 == 0:
        cont = cont + 1 # contador de quantos números foram somados 
        soma = soma + c # acumular o valor + próximo começando do 0 
        # edentado para contar quantos números sao divisiveis por 3, caso contrátio contaria quantos numeros pares tem entre 1 e 500
print (f' A soma de todos os {cont} números solicitados é {soma}')
    
# Create a program that simulates the operation of an ATM. At the beginning, ask the user for the amount to be withdrawn (an integer), and the program will display how many bills of each denomination will be given.
# Note: Consider that the ATM has bills of R$50, R$20, R$10, and R$1.

from time import sleep
nota50 = saque = resto = nota10 = nota20 = nota1 = 0
while True:
    saque = int(input('Qual valor você quer sacar?'))
    nota50 = saque//50
    resto = saque%50
    print(f'Serão {nota50} notas de R$50')
    if resto > 0:
        nota20 = resto//20
        resto = resto%20
        print(f'{nota20} notas de R$20')
        if resto > 0: 
            nota10 = resto//10
            resto = resto%10
            print(f'{nota10} notas de R$10')
            if resto > 0:
                nota1 = resto
                print (f'e {nota1} notas de R$1')
    sleep(1)
    break
print('Obrigada pela preferência')
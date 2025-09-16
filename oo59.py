# Create a program that reads two values and displays a menu on the screen:
# [1] add [2] multiply [3] largest [4] new numbers [5] exit the program
# Your program should perform the requested operation in each case.

from time import sleep
valor1 = int(input('Digite o 1º valor:'))
valor2 = int(input('Digite o 2º valor:'))
opçao = 0
while opçao != 5:
    opçao = int(input('''[1] somar 
                  [2] multiplicar 
                  [3] maior 
                  [4] novos números 
                  [5] sair do programa
                      Qual a sua opção?'''))
    if opçao == 1:
        print(f'A soma entre {valor1} e {valor2} é {valor1 + valor2}')
    elif opçao == 2:
        print (f'O resultado de {valor1} x {valor2} é {valor1 * valor2}')
    elif opçao == 3:
        if valor1 > valor2:
            print (f'O maior valor entre {valor1} e {valor2} é {valor1}')
        if valor2 > valor1:
            print (f'O maior valor entre {valor1} e {valor2} é {valor2}')
        if valor1 == valor2:
            print (f'Os dois valores são iguais.')
    elif opçao == 4:
        valor1 = int(input('Digite o 1º valor:'))
        valor2 = int(input('Digite o 2º valor:'))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
sleep (2)
print('Fim do programa! Volte sempre!')

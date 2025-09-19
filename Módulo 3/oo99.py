# Create a program with a function called greater(), which receives several parameters with integer values. Your program must analyze all the values and indicate which one is the largest.

from time import sleep

def maior(*num): 
    for n in num:
        maior = menor = 0
        if n == 0: 
            maior = menor = num
        else:
            if n > maior:
                maior = num 
            elif n < menor:
                menor = num 
    print('Analizando os valores passados...')
    sleep(2)
    print(f'{num} Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')


maior (2, 5, 8, 4)
maior (4, 8, 5, 3, 10)


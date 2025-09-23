# Create a program with a function called readInt() that works similarly to Python’s input function, but validates the input to accept only numeric values.


def leiaint(msg): 
    valor = 0
    while True:
        n = str(input(msg)) 
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[0;31m ERRO! Digite um número inteiro valido.\033[m')
        
leiaint('qual numero')



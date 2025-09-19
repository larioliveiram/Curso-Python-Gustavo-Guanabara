# Create a program with a function called write(), which receives any text as a parameter and displays a message with an adaptable size.

def escreva(texto):
    print(f'{'~'*len(texto)}')
    print(texto)

escreva('Python é top')

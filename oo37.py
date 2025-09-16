# Write a program that reads any integer and asks the user to choose the conversion base:
# 1. for binary
# 2. for octal
# 3. for hexadecimal
# Display the result on the screen.

n = int(input('Digite um número inteiro:'))
print(''''Escolha uma das bases para conversão: 
 1 - Binário 
 2 - Octal 
 3 - Hexadecimal''') #pode-se utilizar ''' para criar uma string multilinha
modo = int(input('Sua opção:'))
if modo == 1:
    #divide o numero por 2, repete o processo até que o resto seja 0 ou 1 
    print(f'{n} convertido para binário é {bin(n)[2:]}')  # bin() converte para binário, [2:] remove o '0b' do início, ou seja, fatia e começa do terceiro caractere até o final
elif modo == 2:
    #divide o numero por 8, repete o processo até que o resto seja 0 ou 1
    print(f'{n} convertido para octal é{oct(n)[2:]}')
elif modo == 3:
    #divide o numero por 16, repete o processo até que o resto seja 0 ou 1
    print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('Opção inválida, tente um número entre 1 e 3.')
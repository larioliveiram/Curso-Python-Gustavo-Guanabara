# Write a program that reads two integers and compares them, displaying a message on the screen:
# 1. The first value is greater
# 2. The second value is greater
# 3. There is no greater value, both are equal

n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro número inteiro:'))
if n1>n2:
    print(f'O número {n1} é maior que o número {n2}')
elif n2>n1:
    print(f'O número {n2} é maior que o número {n1}')
else:
    print('Os dois números são iguais')
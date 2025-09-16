# Write a program that reads any integer n and displays the first n elements of a Fibonacci sequence. # Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
t1 = 0
t2 = 1
n = int(input('Quantos números da sequência de Fibonacci você quer ver? '))
print(f'{t1}  {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print (f' {t3}', end=' ') # mostrar antes de atualizar
    t1 = t2 = t3 # atualiza os valores de t1 e t2
    cont += 1
    if n <= 0:
        print('Por favor, digite um número inteiro positivo.')
print('****')
    
 
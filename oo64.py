# Create a program that reads several integers from the keyboard. The program will only stop when the user enters the value 999, which is the stop condition. At the end, display how many numbers were entered and the sum of them (excluding the flag).

soma = 0 
cont = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999: 
        break
    soma += n 
    cont += 1
print (f'Você digitou {cont} números e a soma entre eles é {soma}.')
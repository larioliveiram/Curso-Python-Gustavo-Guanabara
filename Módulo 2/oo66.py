# Create a program that reads several integers from the keyboard. The program will only stop when the user enters the value 999, which is the stop condition. At the end, display how many numbers were entered and the sum of them (excluding the stop value).

cont = soma = nun = 0
while True:
    nun = int(input('Digite um número (999 para parar): '))
    if nun == 999:
        break
    cont += 1
    soma += nun 
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
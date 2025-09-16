# Create a program that reads several integers from the keyboard. At the end of execution, display the average of all the values and which was the highest and lowest value entered. The program should ask the user whether they want to continue entering values or not.

soma = media = maior = menor = cont = 0
n = 1
while n > 0: 
    n = int(input('Digite um número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar: sim ou não? ')).strip().upper()[0]
    if resp == 'N':
            break
media = soma/cont
print(f'Você digitou {cont} números, a média foi {media}, o maior valor foi {maior} e o menor valor foi {menor}')
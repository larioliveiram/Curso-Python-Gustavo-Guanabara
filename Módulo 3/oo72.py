# Create a program that has a tuple fully filled with the numbers written out in words, from zero to twenty. Your program should read a number from the keyboard (between 0 and 20) and display it in words.

extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'once', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True: 
    teclado = int(input('Digite um número de 0 a 20: '))
    if 0 <= teclado <= 20:
        print(f'O número que você digitou se escreve {extenso[teclado]}.')
        pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if pergunta in 'N':
            break
        if pergunta not in 'SN':
            print('Tente novamente')
    else:
        print('Tente novamente')
print('Obrigada e volte sempre')
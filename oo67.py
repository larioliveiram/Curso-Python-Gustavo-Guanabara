# Write a program that displays the multiplication table of several numbers, one at a time, for each value entered by the user. The program will stop when a negative number is entered.

n = 1
while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    if n < 0 or str:
        print ('Você digitou um número negativo.')
        break
    for c in range (1,11):
       print(f'{n} x {c} = {n*c}')
    '''print(f' A tabuada de {n} é:
      {n} x 1 = {n*1}
      {n} x 2 = {n*2}
      {n} x 3 = {n*3}
      {n} x 4 = {n*4}
      {n} x 5 = {n*5}
      {n} x 6 = {n*6}
      {n} x 7 = {n*7}
      {n} x 8 = {n*8}
      {n} x 9 = {n*9}
      {n} x 10 = {n*10}'''
    resposta = str(input('Quer digitar outro número? [S/N]')).strip().upper()
    if resposta in 'S':
       continue
    if resposta in 'N':
      break
print('Programa encerrado. Volte sempre!')
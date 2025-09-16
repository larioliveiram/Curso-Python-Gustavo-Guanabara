# Write a program that reads any year and displays whether it is a leap year or not.


import datetime
ano = int(input('Em qual você nasceu?'))
if ano == 0:
    ano = datetime.date.today().year
if (ano%4) == 0 and ano%100!=0 or (ano%400) == 0:
    print('Você nasceu em um ano bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')
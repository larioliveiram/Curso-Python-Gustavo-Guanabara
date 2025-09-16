# Create a program that reads the birth year of seven people. At the end, display how many people are still minors and how many are already adults.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range (1,8):
    nasc = int(input('Em que ano você nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1 # se ela tiver 21 anos ou mais, acumula no grupo totmaior
    else: 
        totmenor = totmenor + 1 # se ela tiver menos de 21 anos, acumula no grupo totmenor
print(f'{totmaior} pessoas são maiores de idade e {totmenor} pessoas ainda não atingiram a maioridade')


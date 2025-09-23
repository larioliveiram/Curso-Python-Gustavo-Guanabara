# Create a program with a function called vote() that receives a person’s year of birth as a parameter, returning a literal value indicating whether the person’s vote is denied, optional, or mandatory in the elections. 

from datetime import date

def voto(ano_nasc):
    idade = date.today().year - ano_nasc
    if idade >= 18:
        print(f'Com {idade} anos: VOTO É OBRIGATÓRIO!') 
    elif 16 <= idade < 18 or idade > 65: 
        print(f'Com {idade} anos: VOTO É OPCIONAL!')
    else: 
        print(f'Com {idade} anos: VOTO É NEGADO!') 

ano = int(input('Em que ano você nasceu?'))
voto(ano)

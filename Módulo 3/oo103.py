# Faça um porgrama que tenah uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programador devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido infomado corretamente. 


def ficha (jogador = '', gols = '' ):
    if jogador == '':
        jogador = 'desconhecido'
    if gols == '':
        gols = 0
    print(f'O jogador {jogador} fez {gols} gols no campeonato')


nome = str(input('Nome do jogador: ')).strip().capitalize()
num = input('Número de gols: ')
ficha (nome, num)

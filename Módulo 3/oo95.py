# Enhance challenge 93 so that it works with multiple players, including a system to view the performance details of each player. 


time = list()
pergunta ='S'
totgol =  0
gols = list()
while pergunta == 'S':
    jogador = {}
    gols = []
    jogador ['nome'] = str(input('Qual o nome do jogador?: '))
    partidas = int(input('Quantas partidas ele jogou? '))

    for p in range(partidas): 
        gol = int(input(f'Quantos gols na partida {p+1}?'))
        gols.append(gol)

    jogador ['gols'] = gols[:]
    jogador ['total'] =  sum(gols)
    time.append(jogador.copy())
    
    pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if pergunta not in 'SN':
        pergunta = str(input('Não entendi. Sim ou não?')).strip().upper()[0]

print('='*30)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<5}')
for i, jogador in enumerate(time):
    print (f'{i} {jogador["nome"]:<5} {jogador["gols"]:^5} {jogador["total"]}')

while True:
    escolhido = str(input('Quer mostrar de qual jogador? ')).strip().capitalize()
    if escolhido == '999':
        break
    encontrado = False
    for jogador in time:
        if jogador['nome'] == escolhido:
            encontrado = True
            print(f' -- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
            for i, g in enumerate(jogador['gols']):
                print(f'   No jogo {i+1} fez {g} gols.')
    if not encontrado:
        print(f'ERRO! Jogador {escolhido} não encontrado.')

    
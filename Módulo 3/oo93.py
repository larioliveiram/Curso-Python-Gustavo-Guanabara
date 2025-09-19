# Create a program that manages the performance of a soccer player. The program will read the player’s name and how many matches he played. Then it will read the number of goals scored in each match. In the end, all this information will be stored in a dictionary, including the total number of goals scored during the championship. 

cadastro = {}
cadastro ['jogador'] = str(input('Qual o nome do jogador?: '))
cadastro ['partidas'] = int(input('Quantas partidas ele jogou? '))
p = totgol =  0
gols = []
for p in range(cadastro['partidas']): 
    golfeito = int(input(f'Quantos gols na partida {p+1}?'))
    gols.append(golfeito)
    totgol += golfeito
print (f' O jogador {cadastro ["jogador"]} jogou {cadastro ["partidas"]} partidas, totalizando {totgol} gols')
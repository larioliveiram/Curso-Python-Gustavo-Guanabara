# Create a tuple filled with the top 20 teams in the Brazilian Football Championship standings, in order of placement. Then display:
# A) Only the top 5 teams
# B) The last 4 teams in the standings
# C) A list of the teams in alphabetical order
# D) The position of the team Juventude in the standings

classificaçao = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo', 'Bragantino', 'Fluminense', 'Interncional', 'Ceara', 'Corinthians', 'Grêmio', 'Atlético', 'Vasco', 'Santos',  'Vitória', 'Juventude', 'Fortaleza', 'Sport Recife')
print(f'A) {classificaçao[:5]}')
print(f' B) {classificaçao[-4:]}')
print(f' C) {sorted(classificaçao)}')
print(f' D) Esta na {classificaçao.index('Juventude')+1}')
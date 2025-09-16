# Create a program that reads a person's name and tells whether they have "SILVA" in their name.

nome = input('Qual o seu nome?').strip().lower()
resposta = 'silva' in nome
print (f'Você faz parte da grande familia brasileira? {resposta}')
# Create a program that reads a person's full name and displays:
# 1. The name in all uppercase and lowercase letters
# 2. The total number of letters (excluding spaces)
# 3. The number of letters in the first name

nome = (input('Qual o seu nome?')).strip()
print('Analisando seu nome...')
print (f'Seu nome em maiuscula é {nome.upper()}')
print (f'Seu nome em minuscula é {nome.lower()}')
print (f'Seu nome tem, ao todo {len(nome) - nome.count(' ')} letras')
print (f' Seu primeiro nome tem {nome.find(' ')} letras')
print (f'Outra forma de resolver é primeiro nome {nome.split()[0]} tem {len(nome.split()[0])} letras')



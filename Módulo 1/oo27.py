# Write a program that reads a person's full name and then displays the first and last names separately

nome = str(input ('Qual o sue nome?').strip().title())
print (f'Muito prazer em te conhecer, {nome}!')
print(f'Seu primeiro nome é {nome.split()[0]} \n e o ultimo nome é {nome.split()[len(nome.split())-1]}')
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras')


# Write a program that reads a person's gender, but only accepts the values 'M' or 'F'. If the input is incorrect, keep asking until a valid value is entered. 

sexo = str(input('Digite seu sexo M ou F:')).upper().strip()[0]#pegar somente a primeira letra
while sexo not in 'MF':
        print('Dados inválidos. Por favor, digite novamente.')
        sexo = str(input('Digite seu sexo M ou F:')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso.')
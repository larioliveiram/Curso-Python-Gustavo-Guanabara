# Write a program that reads the weight of five people. At the end, display the highest and lowest weights recorded

maior = 0
menor = 0
for c in range (1,6):
    peso = float(input(f'Qual o peso da {c}ª pessoa? '))
    if c == 1 : # se for a primeira pessoa, tanto o maior quanto o menor peso recebem o peso dela
        maior = peso
        menor = peso
    else: # se não for a primeira pessoa, compara o peso dela com o maior e o menor peso já registrados
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print (f'O maior peso lido foi {maior}Kg e o menor peso lido foi {menor}Kg')

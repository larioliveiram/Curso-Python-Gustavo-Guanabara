# Create a program that reads the name and price of several products. The program should ask whether the user wants to continue or not. At the end, display:
# A) The total amount spent on the purchase.
# B) How many products cost more than R$1000.
# C) The name of the cheapest product.

nome = pergunta = ''
preço = total = menor = maior = cont = caros = 0 
while True:
    nome = str(input('Qual o nome do produto?')).strip().capitalize()
    preço = float(input('Qual o preço do produto? R$ '))
    cont += 1
    total += preço 
    pergunta = str(input('Quer continuar?')).strip().upper()[0]
    if pergunta == 'N':
        break
    if preço > 1000:
        caros += 1
    if cont == 1 or preço < menor:
        maior = menor = preço
        barato = nome
    pergunta = ''
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar?')).strip().upper()[0]
 
print(f'A compra ficou R${total}. Isso porque tem {caros} produtos acima de R$1.000,00 e o produto mais barato é {barato} e custa {menor:.2f}')   
   
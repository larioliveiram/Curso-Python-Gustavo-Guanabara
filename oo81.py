# Create a program that reads several numbers and stores them in a list. Ask if the user wants to continue. After that, display:
# A) How many numbers were entered
# B) The list of values sorted in descending order
# C) Whether the value 5 was entered and is in the list or not

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Que continuar? [S/N]')).strip().upper()[0]
    if pergunta in 'N':
        break
    if pergunta not in 'SN':
        pergunta = str(input('Não entendi. Sim ou não?'))
print(f'''A) Foram digitados {len(lista)} números  
      B) A lista decrescente é {sorted(lista,reverse=True)}''')
if 5 in lista:
    print(f'O valor 5 foi digitado e esta na posição {lista.index(5)+1}')
else:
    print('O valor 5 não esta na lista!')
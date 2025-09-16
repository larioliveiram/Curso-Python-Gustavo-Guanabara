# Create a program that reads several numbers and stores them in a list. After that, create two additional lists: one containing only the even numbers and the other containing only the odd numbers entered. At the end, display the contents of all three lists.

lista = []
pergunta = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
    if pergunta not in 'SN':
        pergunta = str(input('Não entendi. Sim ou não?'))
decrescente = sorted(lista,reverse=True)
crescente = sorted(lista)
print(f'A lista é {lista} \n decrescente fica {decrescente} e crescente fica {crescente}')
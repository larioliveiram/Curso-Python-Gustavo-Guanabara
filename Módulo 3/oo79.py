# Create a program where the user can enter several numerical values and register them in a list. If a number already exists in the list, it will not be added. At the end, display all the unique values entered in ascending order.
 
lista = []
while True:
    valores = int(input('Digite um valor:'))
    if valores in lista:
        print('Valor duplicado! Não vou adicionar')
    if valores not in lista:
        lista.append(valores)
        print('Valor adicionado com sucesso!')
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
    if resposta not in 'SN':
        resposta = str(input('Não entendi. Sim ou não?')).strip().upper()[0]
print(f'Você adicionou os valores {lista}')




# Create a program that has a single tuple with product names and their respective prices in sequence. At the end, display a price list, organizing the data in a tabular format. 

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20)
print('-'*30)
print(f'{'LISTAGEM DE PREÇO':^30}')
print('-'*30)
for c in range (0,10,2):
    print(f'{lista[c]:.<30} R${lista[c+1]:>4.2f}')
    c +=2

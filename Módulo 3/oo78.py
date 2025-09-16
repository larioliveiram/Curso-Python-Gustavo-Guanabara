# Write a program that reads 5 numerical values and stores them in a list. At the end, display the largest and smallest values entered and their respective positions in the list.

lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor:')))
print (f'O maior valor foi {max(lista)} na {lista.index(max(lista))+1} posição e o menor valor foi {min(lista)} na {lista.index(min(lista))+1} posição. ')
# Create a program where the user can enter five numerical values and insert them into a list in the correct position (without using sort()). At the end, display the ordered list on the screen.

lista = []
cont = ultimo = 0
for cont in range(0,5):
    valor = int(input(f'Digite o {(cont)+1}º valor: '))
    if cont == 0 or valor > lista[-1]: # se ele é o primeiro ou maior que o último, definindo posição 1 e 4 
        lista.append(valor)
    else: # para definifir números intermediários 
        while ultimo < len(lista):
            if valor <= lista [ultimo]:
                lista.insert(ultimo, valor)
                break
            ultimo += 1
print (f'OS valores digitados em ordem são {lista}')
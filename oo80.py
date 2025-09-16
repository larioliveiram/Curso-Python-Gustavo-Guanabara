# Create a program where the user can enter five numerical values and insert them into a list in the correct position (without using sort()). At the end, display the ordered list on the screen.

lista = []
cont = valor=maior=menor= 0
for cont in range(0,5):
    valor = int(input(f'Digite o {(cont)+1}º valor: '))
    if cont == 0:
        lista.insert(0,valor)
    else:
        if valor > lista[-1]:
            lista.insert(-1,valor) 
        if valor < lista[0]:
            lista.insert(0,valor)
        if lista[0] < valor < lista [-1]:
            if valor < lista [1]:
                lista.insert(1,valor)
            if valor > lista [-2]:
                lista.insert(-2,valor)
            else:
                lista.insert(2,valor)

print (f'OS valores digitados em ordem são {lista}')
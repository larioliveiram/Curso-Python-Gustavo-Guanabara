# Create a program with a function called area(), which receives the dimensions of a rectangular plot of land (width and length) and displays the area of the plot. 

def area(l,c):
    terreno = l*c
    print(f'{'Controle de Terreno':^20}')
    print('-'*20)
    print(f'LARGURA(m): {l}')
    print(f'COMPRIMENTO(m): {c}')
    print(f'A área de um terreno é {l}x{c} é de {terreno}m²')

area(3,5)
